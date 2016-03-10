"""
Intricate Chat Bot for Twitch.tv with Whispers

By Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox and theepicsnail
"""

import json
import re
import sys
import time

import globals
import lib.functions_commands as commands
import requests
import src.lib.command_headers
import src.lib.rive as rive
import src.lib.twitch as twitch
from lib.functions_general import *
from src.config.config import channels_to_join, config
from src.lib.queries.command_queries import *
from src.lib.queries.message_queries import save_message
from src.lib.queries.moderator_queries import get_moderator
from src.lib.queries.points_queries import *
from src.lib.twitch import get_dict_for_users
from twisted.internet import reactor, task, threads
from twisted.internet.protocol import ClientFactory
from twisted.words.protocols import irc

pattern = re.compile('[\W_]+')

reload(sys)
sys.setdefaultencoding("utf8")

PRIMARY_CHANNEL = "curvyllama"
BOT_USER = "lorenzotherobot"
SUPERUSER = "singlerider"
TEST_USER = "theepicsnail_"
EXTRA_CHANNEL = "newyork_triforce"

CHANNEL = "#singlerider"
SERVER = config["server"]
NICKNAME = config["username"]
PASSWORD = config["oauth_password"]

ECHOERS = {}


def ban_for_spam(channel, user):
    ban = "/ban {0}".format(user)
    unban = "/unban {0}".format(user)
    self.msg(channel, ban)
    self.msg(channel, unban)
    save_message(BOT_USER, channel, message)


class Bot(irc.IRCClient):

    def __init__(self):
        self.nickname = NICKNAME
        self.password = PASSWORD
        self.config = config
        self.crons = self.config.get("cron", {})
        src.lib.command_headers.initalizeCommands(config)

    def dataReceived(self, data):
        if data.split()[0] != "PING" and data.split()[1] != "PONG":
            print("->*" + data)
        if data.split()[1] == "WHISPER":
            user = data.split()[0].lstrip(":")
            channel = user.split("!")[0]
            msg = " ".join(data.split()[3:]).lstrip(":")
            self.whisper(user, channel, msg)
        irc.IRCClient.dataReceived(self, data)

    def signedOn(self):
        print("\033[91mYOLO, I was signed on to the server!!!\033[0m")
        if self.factory.kind == "whisper":
            self.sendLine("CAP REQ :twitch.tv/commands")
        if self.factory.kind == "chat":
            for channel in channels_to_join:
                self.joinChannel(channel)
        ECHOERS[self.factory.kind] = self

    def joinChannel(self, channel):
        self.join(channel)
        return

    def joined(self, channel):
        if self.factory.kind == "chat":
            self.cron_initialize(BOT_USER, channel)

    def action(self, user, channel, data):
        pass

    def privmsg(self, user, channel, message):
        """Called when the bot receives a message."""
        username = user.split("!")[0].lstrip(":")
        chan = channel.lstrip("#")
        if message == "shutdown":
            reactor.stop()
        print username, channel, message
        chan = channel.lstrip("#")
        if (channel == "#" + PRIMARY_CHANNEL or
                channel == "#" + SUPERUSER or
                channel == "#" + TEST_USER):
            if username == "twitchnotify":
                self.check_for_sub(channel, username, message)
            # TODO add spam detector here
        chan = channel.lstrip("#")
        if message[0] == "!":
            message_split = message.split()
            fetch_command = get_custom_command(chan, message_split[0])
            if len(fetch_command) > 0:
                if message_split[0] == fetch_command[0][1]:
                    self.return_custom_command(
                        channel, message_split, username)
                    return
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
            self.msg(channel, str(resp).replace(
                "\n", "").replace("\r", "") + "\r\n")

    def whisper(self, user, channel, msg):
        msg = msg.lstrip("!")
        if "!" not in user:
            channel = user
            resp = msg
            username = user
        else:
            username = user.split("!")[0].lstrip(":")
            resp = rive.Conversation(self).run(BOT_USER, username, msg)[:350]
        save_message(username, "WHISPER", msg)
        if resp:
            save_message(BOT_USER, "WHISPER", resp)
            sender = "{user}!{user}@{user}.tmi.twitch.tv".format(user=BOT_USER)
            line = ":%s PRIVMSG #jtv :/w %s %s" % (sender, channel, resp)
            echoer = ECHOERS["whisper"]
            echoer.sendLine(line)
            return line

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
            user_dict, __ = get_dict_for_users()
            moderator = get_moderator(username, chan)
            if moderator:
                self.msg(channel, resp)
                increment_command_counter(chan, message[0])
                save_message(BOT_USER, channel, resp)
                print("!->" + resp)
                return
        elif elements[0] == "reg":
            self.msg(channel, resp)
            increment_command_counter(chan, message[0])
            save_message(BOT_USER, channel, resp)
            print("!->" + resp)
            return

    def check_for_sub(self, channel, username, message):
        try:
            message_split = message.rstrip("!").split()
            subbed_user = message_split[0]
            if message_split[1] == "just" and len(message_split) < 4:
                modify_user_points(subbed_user, 100)
                resp = "/me {0} treats for {1} for a first \
time subscription!".format(100, subbed_user)
                self.msg(channel, resp)
                save_message(BOT_USER, channel, resp)
            elif message_split[1] == "subscribed" and len(message_split) < 9:
                months_subbed = message_split[3]
                modify_user_points(subbed_user, int(months_subbed) * 100)
                resp = "/me {0} has just resubscribed for {1} \
months straight and is getting {2} treats for loyalty!".format(
                    subbed_user, months_subbed, int(months_subbed) * 100)
                self.msg(channel, resp)
                save_message(BOT_USER, channel, resp)
        except Exception as error:  # pragma: no cover
            print error

    def cron_initialize(self, user, channel):
        crons = self.crons.get(channel, None)
        if crons:
            for job in crons:
                if job[1]:
                    kwargs = {"delay": job[0], "callback": job[
                        2], "channel": channel}

                    def looping_call(kwargs):
                        time.sleep(kwargs["delay"])
                        task.LoopingCall(self.cron_job, kwargs).start(
                            kwargs["delay"])
                    threads.deferToThread(looping_call, kwargs)
                    continue

    def cron_job(self, kwargs):
        channel = kwargs["channel"]
        resp = kwargs["callback"](kwargs["channel"])
        if resp:
            user = "{user}!{user}@{user}.tmi.twitch.tv".format(user=BOT_USER)
            line = ":{user} PRIVMSG {channel} :{message}".format(
                user=user, channel=channel, message=resp)
            print "<*>" + line
            self.transport.write(line + "\r\n")

    def handle_command(self, command, channel, username, message):
        if command == message:
            args = []
        elif command == message and command in commands.keys():  # pragma: no cover
            pass
        else:
            args = [message[len(command) + 1:]]
        if not commands.check_is_space_case(command) and args:
            args = args[0].split(" ")
        if commands.is_on_cooldown(command, channel):
            pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
                command, username, commands.get_cooldown_remaining(
                    command, channel)), channel)
            self.whisper(
                username, channel,  "Sorry! " + command +
                " is on cooldown for " + str(
                    commands.get_cooldown_remaining(
                        command, channel)
                ) + " more seconds in " + channel.lstrip("#") +
                ". Can I help you?")
            return
        if commands.check_has_user_cooldown(command):
            if commands.is_on_user_cooldown(command, channel, username):
                self.whisper(
                    username, channel, "Slow down! Try " + command +
                    " in " + channel.lstrip("#") + " in another " + str(
                        commands.get_user_cooldown_remaining(
                            command, channel, username)) + " seconds or just \
ask me directly?")
                return
            commands.update_user_last_used(command, channel, username)
        pbot('Command is valid and not on cooldown. (%s) (%s)' %
             (command, username), channel)
        cmd_return = commands.get_return(command)
        if cmd_return != "command":
            resp = '(%s) : %s' % (username, cmd_return)
            commands.update_last_used(command, channel)
            self.msg(channel, resp)
            return
        if commands.check_has_ul(username, command):
            user_data, __ = twitch.get_dict_for_users(channel)
            try:
                moderator = get_moderator(username, channel.lstrip("#"))
                if not moderator and username != SUPERUSER:
                    resp = '(%s) : %s' % (
                        username, "This is a moderator-only command!")
                    pbot(resp, channel)
                    self.msg(channel, resp)
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
                              'weather', 'treats', 'wins']
            if command.lstrip("!") in prevented_list:
                return
        result = commands.pass_to_function(
            command, args, username=username, channel=channel.lstrip("#"))
        commands.update_last_used(command, channel)
        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            return resp[:350]
            save_message(BOT_USER, channel, resp)  # pragma: no cover


class BotFactory(ClientFactory):

    def __init__(self, kind):
        self.kind = kind

    def buildProtocol(self, addr):
        bot = Bot()
        bot.factory = self
        return bot

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        print "disconnected:", reason
        if self.kind == "whisper":
            whisper_url = "http://tmi.twitch.tv/servers?cluster=group"
            whisper_resp = requests.get(url=whisper_url)
            whisper_data = json.loads(whisper_resp.content)
            socket = whisper_data["servers"][0].split(":")
            WHISPER = [str(socket[0]), int(socket[1])]
            reactor.connectTCP(WHISPER[0], WHISPER[1], BotFactory("whisper"))
            self.clientConnection.disconnect()
            connector.connect()
        else:
            self.clientConnection.disconnect()
            connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        connector.connect()
