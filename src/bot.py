"""
Simple IRC Bot for Twitch.tv

Originally developed by Aidan Thomson <aidraj0@gmail.com>

Forked and modified by Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox

Rekt by theepicsnail
"""

import lib.irc as irc_
from lib.functions_general import *
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
            except Exception as err:
                raise
                traceback.print_exc(file=self.log)

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
            
        ######TEMPORARY COMMAND IGNORES FOR shedeviil_09
        
        elif command == message and command in commands.keys():
            print "Yes, it is in commands"
            
        else:
            args = [message[len(command)+1:]] # default to args = ["bar baz"]

        if not commands.check_is_space_case(command) and args:
            # if it's not space case, break the arg apart
            args = args[0].split(" ")

        # print("Command:", command, "args", args)

        # check cooldown.
        if commands.is_on_cooldown(command, channel):
            pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
                command, username, commands.get_cooldown_remaining(command, channel)),
                channel
            )
            return
        pbot('Command is valid and not on cooldown. (%s) (%s)' %
                (command, username) ,channel)

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
            user_dict, all_users = twitch.get_dict_for_users()
            if username not in user_dict["chatters"]["moderators"]:
                if username != 'singlerider':
                    resp = '(%s) : %s' % (
                        username, "This is a moderator-only command!")
                    pbot(resp, channel)
                    self.irc.send_message(channel, resp)
                    return
                
        if globals.global_channel != "curvyllama":
            if globals.global_channel != "lorenzotherobot":
                print globals.global_channel
                prevented_list = ['songrequest', 'request', 'llama', 'shots', 'treats', 'welcome', 'rules']
            #print command
                if command.replace("!","") in prevented_list:
                    return
            
        result = commands.pass_to_function(command, args)
        commands.update_last_used(command, channel)

        #pbot("Command %s(%s) had a result of %s" % (command, args, result), channel)
        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            self.irc.send_message(channel, resp)
