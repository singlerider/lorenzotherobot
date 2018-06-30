"""
Intricate Chat Bot for Twitch.tv with Whispers

By Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox and theepicsnail
"""

import sys
from threading import Thread

import lib.functions_commands as commands
import src.lib.command_headers as command_headers
import src.lib.cron as cron
import src.lib.rive as rive
import src.lib.twitch as twitch
from lib.functions_general import *
from src.lib.spam_detector import spam_detector
from src.config.config import config
from src.lib.irc import IRC
from src.lib.queries.blacklist_queries import check_for_blacklist
from src.lib.queries.command_queries import *
from src.lib.queries.message_queries import save_message
from src.lib.queries.moderator_queries import get_moderator
from src.lib.queries.points_queries import *

reload(sys)
sys.setdefaultencoding("utf8")

PRIMARY_CHANNEL = "curvyllama"
BOT_USER = config["username"]
SUPERUSER = "singlerider"
TEST_USER = "theepicsnail_"
EXTRA_CHANNEL = "newyork_triforce"

NICKNAME = config["username"]
PASSWORD = config["oauth_password"]

ECHOERS = {}


class Bot(object):

    def __init__(self):
        self.IRC = IRC(config)
        self.nickname = NICKNAME
        self.password = PASSWORD
        self.config = config
        self.crons = self.config.get("cron", {})
        cron.initialize(self.IRC, self.crons)
        command_headers.initalize_commands(config)
        self.run()

    def return_custom_command(self, channel, message, username):
        chan = channel.lstrip("#")
        elements = get_custom_command_elements(
            chan, message[0])
        replacement_user = username
        if len(message) > 1:
            replacement_user = message[1]
        resp = elements[1].replace(
            "{}", replacement_user).replace("[]", str(elements[2] + 1))
        if elements[0] == "mod":
            moderator = get_moderator(username, chan)
            if moderator:
                increment_command_counter(chan, message[0])
                save_message(BOT_USER, channel, resp)
                print("!-> " + resp)
                return resp
        elif elements[0] == "reg":
            increment_command_counter(chan, message[0])
            save_message(BOT_USER, channel, resp)
            print("!-> " + resp)
            return resp

    def ban_for_spam(self, channel, user, message):
        timeout = "/timeout {0} 1".format(user)
        self.IRC.send_message(channel, timeout)
        save_message(BOT_USER, channel, message)

    def privmsg(self, username, channel, message):
        if spam_detector(username, message) is True:
            #  # uncomment the line below to enable spam_detector
            # self.ban_for_spam(channel, username, message)
            pass
        chan = channel.lstrip("#")
        if message[0] == "!":
            message_split = message.split()
            fetch_command = get_custom_command(chan, message_split[0])
            if len(fetch_command) > 0:
                if message_split[0] == fetch_command[0][1]:
                    resp = self.return_custom_command(
                        channel, message_split, username)
                    if resp:
                        self.IRC.send_message(channel, resp)
        save_message(username, channel, message)
        part = message.split(' ')[0]
        valid = False
        if commands.is_valid_command(message):
            valid = True
        if commands.is_valid_command(part):
            valid = True
        if not valid:
            return
        resp = self.handle_command(
            part, channel, username, message)
        if resp:
            self.IRC.send_message(channel, resp)
        return

    def privmsg_chatroom(
            self, username, channel, channel_id, chatroom_uid, message):
        chan = channel.lstrip("#")
        if message[0] == "!":
            message_split = message.split()
            fetch_command = get_custom_command(chan, message_split[0])
            if len(fetch_command) > 0:
                if message_split[0] == fetch_command[0][1]:
                    resp = self.return_custom_command(
                        channel, message_split, username)
                    if resp:
                        self.IRC.send_message(channel, resp)
        save_message(username, channel, message)
        part = message.split(' ')[0]
        valid = False
        if commands.is_valid_command(message):
            valid = True
        if commands.is_valid_command(part):
            valid = True
        if not valid:
            return
        resp = self.handle_command(
            part, channel, username, message)
        if resp:
            self.IRC.send_chatroom_message(channel_id, chatroom_uid, resp)
        return

    def whisper(self, username, channel, message):
        if check_for_blacklist(username):
            return
        message = str(message.lstrip("!"))
        resp = rive.Conversation(self).run(username, message)[:350]
        if resp[0] == "[":
            resp = "DansGame"
        save_message(username, "WHISPER", message)
        if resp:
            print resp
            save_message(BOT_USER, "WHISPER", resp)
            self.IRC.send_whisper(username, str(resp))
            return

    def join_part(self, action, channel):
        if action == "join":
            self.IRC.join_channels(
                self.IRC.channels_to_string([channel]), "chat")
            command_headers.initalize_commands_after_runtime(channel)
            self.IRC.send_message(channel, "Hi HeyGuys")
            print "JOINING", channel
        if action == "leave":
            self.IRC.send_message(channel, "Bye HeyGuys")
            self.IRC.leave_channels(
                self.IRC.channels_to_string([channel]), "chat")
            command_headers.deinitialize_commands_after_runtime(channel)
            print "LEAVING", channel

    def handle_command(self, command, channel, username, message):
        if command == message:
            args = []
        elif command == message and command in commands.keys():  # pragma: no cover
            pass
        else:
            args = [message[len(command) + 1:]]
        if not commands.check_is_space_case(command) and args:
            args = args[0].split(" ")
        if (command == "!join" or command == "!leave") and channel == "#" + BOT_USER:
            self.join_part(command.lstrip("!"), "#" + username)
        if commands.is_on_cooldown(command, channel):
            pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
                command, username, commands.get_cooldown_remaining(
                    command, channel)), channel)
            self.IRC.send_whisper(
                username, "Sorry! " + command +
                " is on cooldown for " + str(
                    commands.get_cooldown_remaining(
                        command, channel)
                ) + " more seconds in " + channel.lstrip("#") +
                ". Can I help you?")
            return
        if commands.check_has_user_cooldown(command):
            if commands.is_on_user_cooldown(command, channel, username):
                self.IRC.send_whisper(
                    username, "Slow down! Try " + command +
                    " in " + channel.lstrip("#") + " in another " + str(
                        commands.get_user_cooldown_remaining(
                            command, channel, username)) + " seconds or just \
ask me directly?")
                return
            commands.update_user_last_used(command, channel, username)
        if check_for_blacklist(username):
            return
        pbot('Command is valid and not on cooldown. (%s) (%s)' %
             (command, username), channel)
        cmd_return = commands.get_return(command)
        if cmd_return != "command":
            resp = '(%s) : %s' % (username, cmd_return)
            commands.update_last_used(command, channel)
            self.IRC.send_message(channel, resp)
            return
        command_has_ul = commands.check_has_ul(username, command)
        if command_has_ul:
            user_data, __ = twitch.get_dict_for_users(channel)
            if command_has_ul == "superuser":
                if username == SUPERUSER:
                    return commands.pass_to_function(
                        command, args, username=username,
                        channel=channel.lstrip("#"))
                else:
                    return
            try:
                moderator = get_moderator(username, channel.lstrip("#"))
                if not moderator and username != SUPERUSER:
                    resp = '(%s) : %s' % (
                        username, "This is a moderator-only command!")
                    pbot(resp, channel)
                    self.IRC.send_whisper(username, resp)
                    return
            except Exception as error:  # pragma: no cover
                with open("errors.txt", "a") as f:
                    error_message = "{0} | {1} : {2}\n{3}\n{4}".format(
                        username, channel, command, user_data, error)
                    f.write(error_message)
        approved_channels = [
            PRIMARY_CHANNEL, BOT_USER, SUPERUSER, TEST_USER, EXTRA_CHANNEL]
        if channel.lstrip("#") not in approved_channels:
            prevented_list = ['songrequest', 'request', 'shots', 'donation',
                              'welcome', 'rules', 'gt',
                              'llama', 'loyalty', 'uptime', 'highlight',
                              'weather', 'treats', 'wins', 'subcount']
            if command.lstrip("!") in prevented_list:
                return
        result = commands.pass_to_function(
            command, args, username=username, channel=channel.lstrip("#"))
        commands.update_last_used(command, channel)
        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            save_message(BOT_USER, channel, resp)  # pragma: no cover
            return resp[:350]

    def run(self):

        def get_incoming_data(kind):
            while True:
                try:
                    data = self.IRC.nextMessage(kind)
                    message = ""
                    chatroom_message = False
                    message_received = False
                    if kind == "chat":
                        if self.IRC.check_for_message(data):
                            message_received = True
                        elif self.IRC.check_for_chatroom_message(data):
                            message_received = True
                            chatroom_message = True
                    elif kind == "whisper":
                        message_received = self.IRC.check_for_whisper(data)
                    if not message_received:
                        continue
                    else:
                        if not chatroom_message:
                            if kind == "chat":
                                data = self.IRC.get_message(data)
                            elif kind == "whisper":
                                data = self.IRC.get_whisper(data)
                            message_dict = data
                            channel = message_dict.get('channel')
                            message = message_dict.get('message')
                            username = message_dict.get('username')
                            print("->*", username, channel, message)
                            if message and kind == "chat":
                                Thread(target=self.privmsg, args=(
                                    username, channel, message)).start()
                            elif message and kind == "whisper":
                                Thread(target=self.whisper, args=(
                                    username, channel, message)).start()
                        else:  # This is a chatroom message
                            data = self.IRC.get_chatroom_message(data)
                            message_dict = data
                            channel_id = message_dict.get('channel_id')
                            channel = self.config.get(
                                "user_id_map", {}).get(channel_id)
                            chatroom_uid = message_dict.get('chatroom_uid')
                            message = message_dict.get('message')
                            username = message_dict.get('username')
                            print(
                                "->*", username, channel, channel_id,
                                chatroom_uid, message
                            )
                            if message:
                                Thread(target=self.privmsg_chatroom, args=(
                                    username, channel, channel_id,
                                    chatroom_uid, message
                                )).start()
                    continue
                except Exception as error:
                    print error

        Thread(target=get_incoming_data, args=("whisper",)).start()
        Thread(target=get_incoming_data, args=("chat",)).start()
