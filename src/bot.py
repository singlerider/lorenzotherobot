"""
Intricate Chat Bot for Twitch.tv

By Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox and theepicsnail
"""

from src.lib.queries.message_queries import save_message
from src.lib.queries.points_queries import *
from src.lib.queries.command_queries import *
from lib.functions_general import *
from src.lib.twitch import get_dict_for_users
from src.lib.spam_detector import spam_detector
import lib.irc as irc_
import lib.functions_commands as commands
import src.lib.command_headers
import src.lib.twitch as twitch
import src.lib.user_data as info
import src.lib.cron as cron
import sys
import datetime
import traceback
import sched
import time
import threading
import os
import globals

END = False


class Roboraj(object):

    def __init__(self, config):
        self.config = config
        src.lib.command_headers.initalizeCommands(config)
        self.irc = irc_.irc(config)
        # start threads for channels that have cron messages to run
        cron.initialize(self.irc, self.config.get("cron", {}))

    def run(self):

        def check_for_sub(channel, username, message):
            # >> :twitchnotify!twitchnotify@twitchnotify.tmi.twitch.tv PRIVMSG #curvyllama :KiefyWonder subscribed for 5 months in a row!
            # >> :twitchnotify!twitchnotify@twitchnotify.tmi.twitch.tv PRIVMSG #curvyllama :KiefyWonder has just subscribed!
            # first sub points = 100
            # resub = 50
            try:
                message_split = message.rstrip("!").split()
                subbed_user = message_split[0]
                if message_split[1] == "has":
                    modify_user_points(subbed_user, 100)
                    resp = "{0} has just subscribed for the first time!".format(
                        subbed_user)
                    self.irc.send_message(channel, resp)
                elif message_split[1] == "subscribed":
                    months_subbed = message_split[3]
                    modify_user_points(subbed_user, int(months_subbed) * 100)
                    resp = "{0} has just resubscribed for {1} months straight!".format(subbed_user, months_subbed)
                    self.irc.send_message(channel, resp)
            except Exception as error:
                print error

        def return_custom_command(channel, message, username):
            elements = get_custom_command_elements(message)
            resp = elements[1].replace("{}", username)
            if elements[0] == "mod":
                user_dict, __ = get_dict_for_users()
                if username in user_dict["chatters"]["moderators"]:
                    self.irc.send_message(channel, resp)
                    increment_command_counter(message)
            elif elements[0] == "reg":
                self.irc.send_message(channel, resp)
                increment_command_counter(message)

        def ban_for_spam(channel, user):
            ban = "/ban {0}".format(user)
            unban = "/unban {0}".format(user)
            print ban, unban
            self.irc.send_message(channel, ban)
            self.irc.send_message(channel, unban)

        def write_to_log(channel, username, message):
            date = time.strftime('%Y_%m_%d', time.gmtime())
            filename = 'src/logs/{}/{}.txt'.format(date, channel.lstrip("#"))
            timestamp = time.strftime("%H:%M:%SZ", time.gmtime())
            message = "".join(i for i in message if ord(i) < 128)  # fix up non ascii
            try:
                pass
                with open(filename, 'a') as f:
                    f.write("{} | {} : {}\n".format(
                        username, timestamp, str(message)))
            except Exception as error:
                foldername = 'src/logs/{}_{}'.format(
                    channel.lstrip("#"), time.strftime('%Y_%m_%d'))
                os.system("mkdir src/logs/{}".format(date))
                print str(error) + ": Creating new folder: " + str(date)
                write_to_log(channel, username, message)

        config = self.config

        while True:
            try:
                data = self.irc.nextMessage()
                if not self.irc.check_for_message(data):
                    continue
                message_dict = self.irc.get_message(data)
                channel = message_dict['channel']
                globals.global_channel = channel.lstrip('#')
                message = message_dict['message']  # .lower()
                username = message_dict['username']
                globals.CURRENT_USER = username
                if channel == "#curvyllama" or channel == "#singlerider":
                    write_to_log(channel, username, message)
                    if message[0] == "!":
                        print message
                    fetch_command = get_custom_command(message)
                    if len(fetch_command) > 0:
                        if message == fetch_command[0][1]:
                            return_custom_command(
                                channel, message, username)
                    # check for sub message
                    if username == "twitchnotify":
                        check_for_sub(channel, username, message)
                    if spam_detector(username, message) == True:
                        ban_for_spam(channel, user)
                save_message(username, channel, message)
                # check if message is a command with no arguments
                part = message.split(' ')[0]
                valid = False
                if commands.is_valid_command(message):
                    valid = True
                if commands.is_valid_command(part):
                    valid = True
                if not valid:
                    continue
                self.handleCommand(part, channel, username, message)
            except Exception as error:
                print error

    def handleCommand(self, command, channel, username, message):
        # parse arguments
        # if command is space case then
        #   !foo bar baz
        # turns into
        #   command = "!foo", args=["bar baz"]
        # otherwise it turns into
        #   command = "!foo", args=["bar", "baz:]
        # print("Inputs:", command, channel, username, message)
        if command == message:
            args = []

        elif command == message and command in commands.keys():
            print "Yes, it is in commands"

        else:
            # default to args = ["bar baz"]
            args = [message[len(command) + 1:]]

        if not commands.check_is_space_case(command) and args:
            # if it's not space case, break the arg apart
            args = args[0].split(" ")
        if commands.is_on_cooldown(command, channel):
            pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
                command, username, commands.get_cooldown_remaining(
                    command, channel)), channel)
            return
        pbot('Command is valid and not on cooldown. (%s) (%s)' %
             (command, username), channel)

        # Check for and handle the simple non-command case.
        cmd_return = commands.get_return(command)
        if cmd_return != "command":
            # it's a return = "some message here" kind of function
            resp = '(%s) : %s' % (username, cmd_return)
            commands.update_last_used(command, channel)
            self.irc.send_message(channel, resp)
            return

        # if there's a required userlevel, validate it.
        if commands.check_has_ul(username, command):
            user_data = twitch.get_dict_for_users_mods_hack(channel)
            try:
                if username not in user_data["chatters"]["moderators"]:
                    if username != 'singlerider':
                        resp = '(%s) : %s' % (
                            username, "This is a moderator-only command!")
                        pbot(resp, channel)
                        self.irc.send_message(channel, resp)
                        return
            except Exception as error:
                with open("errors.txt", "a") as f:
                    error_message = "{0} | {1} : {2}\n{3}\n{4}".format(
                        username, channel, command, user_data, error)
                    f.write(error_message)

        approved_channels = ["curvyllama", "lorenzotherobot", "singlerider"]
        if globals.global_channel not in approved_channels:
            print globals.global_channel
            prevented_list = ['songrequest', 'request', 'shots', 'donation',
                              'welcome', 'rules', 'poll', 'vote', 'gt',
                              'add', 'rem']
            if command.lstrip("!") in prevented_list:
                return

        result = commands.pass_to_function(command, args)
        commands.update_last_used(command, channel)

        # pbot("Command %s(%s) had a result of %s" % (
        #         command, args, result), channel)
        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            self.irc.send_message(channel, resp)
            if channel == "#curvyllama":
                write_to_log(channel, "[BOT]", resp)
            save_message("lorenzotherobot", channel, resp)
