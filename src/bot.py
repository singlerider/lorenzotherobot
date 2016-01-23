"""
Intricate Chat Bot for Twitch.tv

By Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox and theepicsnail
"""

import os
import sys
import time

import globals
import lib.functions_commands as commands
import lib.irc as irc_
import src.lib.command_headers
import src.lib.cron as cron
import src.lib.twitch as twitch
from lib.functions_general import *
from src.lib.queries.command_queries import *
from src.lib.queries.message_queries import save_message
from src.lib.queries.points_queries import *
from src.lib.spam_detector import spam_detector
from src.lib.twitch import get_dict_for_users

reload(sys)
sys.setdefaultencoding("utf8")

END = False

PRIMARY_CHANNEL = "curvyllama"
BOT_USER = "lorenzotherobot"
SUPERUSER = "singlerider"
TEST_USER = "theepicsnail_"

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
        os.system("mkdir src/logs/{}".format(date))
        print str(error) + ": Creating new folder: " + str(date)
        write_to_log(channel, username, message)


class Roboraj(object):

    def __init__(self, config):
        self.config = config
        src.lib.command_headers.initalizeCommands(config)
        self.irc = irc_.irc(config)
        # start threads for channels that have cron messages to run
        cron.initialize(self.irc, self.config.get("cron", {}))

    def run(self):

        def check_for_sub(channel, username, message):
            try:
                message_split = message.rstrip("!").split()
                subbed_user = message_split[0]
                if message_split[1] == "just" and len(message_split) < 4:
                    modify_user_points(subbed_user, 100)
                    resp = "/me {0} treats for {1} for a first time subscription!".format(
                        100, subbed_user)
                    self.irc.send_message(channel, resp)
                    save_message(BOT_USER, channel, resp)
                elif message_split[1] == "subscribed" and len(message_split) < 9:
                    months_subbed = message_split[3]
                    modify_user_points(subbed_user, int(months_subbed) * 100)
                    resp = "/me {0} has just resubscribed for {1} months straight and is getting {2} treats for loyalty!".format(
                        subbed_user, months_subbed, int(months_subbed) * 100)
                    self.irc.send_message(channel, resp)
                    save_message(BOT_USER, channel, resp)
            except Exception as error:
                print error

        def return_custom_command(channel, message, username):
            chan = channel.lstrip("#")
            elements = get_custom_command_elements(
                chan, message[0])
            replacement_user = username
            if len(message) > 1:
                replacement_user = message[1]
            resp = elements[1].replace(
                "{}", replacement_user).replace("[]", str(elements[2] + 1))
            if elements[0] == "mod":
                user_dict, __ = get_dict_for_users()
                if username in user_dict["chatters"]["moderators"]:
                    self.irc.send_message(channel, resp)
                    increment_command_counter(chan, message[0])
                    save_message(BOT_USER, channel, resp)
            elif elements[0] == "reg":
                self.irc.send_message(channel, resp)
                increment_command_counter(chan, message[0])
                save_message(BOT_USER, channel, resp)

        def ban_for_spam(channel, user):
            ban = "/ban {0}".format(user)
            unban = "/unban {0}".format(user)
            print ban, unban
            self.irc.send_message(channel, ban)
            self.irc.send_message(channel, unban)
            save_message(BOT_USER, channel, message)

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
                if channel == "#" + PRIMARY_CHANNEL or channel == "#" + SUPERUSER:
                    write_to_log(channel, username, message)
                    # check for sub message
                    if username == "twitchnotify":
                        check_for_sub(channel, username, message)
                    if spam_detector(username, message) is True:
                        ban_for_spam(channel, user)
                chan = channel.lstrip("#")
                if message[0] == "!":
                    message_split = message.split()
                    fetch_command = get_custom_command(chan, message_split[0])
                    if len(fetch_command) > 0:
                        if message_split[0] == fetch_command[0][1]:
                            return_custom_command(
                                channel, message_split, username)
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
            pass
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
        if commands.check_has_user_cooldown(command):
            if commands.is_on_user_cooldown(command, channel, username):
                return
            commands.update_user_last_used(command, channel, username)
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
            user_data, __ = twitch.get_dict_for_users(channel)
            try:
                if username not in user_data["chatters"]["moderators"]:
                    if username != SUPERUSER:
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
        approved_channels = [PRIMARY_CHANNEL, BOT_USER, SUPERUSER, TEST_USER]
        if globals.global_channel not in approved_channels:
            print globals.global_channel
            prevented_list = ['songrequest', 'request', 'shots', 'donation',
                              'welcome', 'rules', 'poll', 'vote', 'gt',
                              'llama', 'loyalty', 'uptime', 'highlight',
                              'weather', 'poll', 'treats', 'vote']
            if command.lstrip("!") in prevented_list:
                return
        result = commands.pass_to_function(command, args)
        commands.update_last_used(command, channel)
        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            self.irc.send_message(channel, resp)
            if channel == "#" + PRIMARY_CHANNEL:
                write_to_log(channel, "[BOT]", resp)
            save_message(BOT_USER, channel, resp)
