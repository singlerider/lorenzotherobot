# encoding=utf8
import json
import re
import socket
import sys
import time

import requests
from functions_general import *

threshold = 5 * 60  # five minutes, make this whatever you want


class IRC:

    def __init__(self, config):
        self.sock = {}
        self.config = config
        self.ircBuffer = {}
        self.ircBuffer["whisper"] = ""
        self.ircBuffer["chat"] = ""
        self.connect("whisper")
        self.connect("chat")

    def nextMessage(self, kind):
        if "\r\n" not in self.ircBuffer[kind]:
            read = self.sock[kind].recv(1024)
            if not read:
                print "Connection was lost"
                self.sock[kind].shutdown
                self.sock[kind].close
                self.connect(kind)
            else:
                self.ircBuffer[kind] += read

        line, self.ircBuffer[kind] = self.ircBuffer[kind].split("\r\n", 1)

        if line is not None:
            if line.startswith("PING"):
                self.sock[kind].send(line.replace("PING", "PONG") + "\r\n")
            return line

    def check_for_message(self, data):
        if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data):
            return True

    def check_for_whisper(self, data):
        if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) WHISPER [a-zA-Z0-9_]+ :.+$', data):
            return True

    def check_for_join(self, data):
        if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) JOIN #[a-zA-Z0-9_]', data):
            return True

    def check_for_part(self, data):
        if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PART #[a-zA-Z0-9_]', data):
            return True

    def check_is_command(self, message, valid_commands):
        for command in valid_commands:
            if command == message:
                return True

    def check_for_connected(self, data):
        if re.match(r'^:.+ 001 .+ :connected to TMI$', data):
            return True

    def get_logged_in_users(self, data):
        if data.find('353'):
            return True

    def check_for_ping(self, data, kind):
        last_ping = time.time()
        if data.find('PING') != -1:
            self.sock[kind].send('PONG ' + data.split()[1] + '\r\n')
            last_ping = time.time()
        if (time.time() - last_ping) > threshold:
            sys.exit()

    def get_message(self, data):
        return re.match(r'^:(?P<username>.*?)!.*?PRIVMSG (?P<channel>.*?) :(?P<message>.*)', data).groupdict()

    def get_whisper(self, data):
        return re.match(r'^:(?P<username>.*?)!.*?WHISPER (?P<channel>.*?) :(?P<message>.*)', data).groupdict()

    def check_login_status(self, data):
        if re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data):
            return False
        else:
            return True

    def send_message(self, channel, message):
        if not message:
            return

        if isinstance(message, basestring):
            self.sock["chat"].send('PRIVMSG %s :%s\r\n' % (channel, message))

        if type(message) == list:
            for line in message.decode("utf8"):
                self.send_message(channel, line)

    def send_whisper(self, recipient, message):
        if not message:
            return

        if isinstance(message, basestring):
            self.sock["whisper"].send(
                'PRIVMSG #jtv :/w %s %s\r\n' % (recipient, message))

        if type(message) == list:
            for line in message.decode("utf8"):
                self.send_message(recipient, str(time.time()))

    def connect(self, kind):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(0)
        sock.settimeout(10)
        port = 6667
        if kind == "whisper":
            server = "irc.chat.twitch.tv"
            print "Connecting to {0}:{1}".format(server, port)
            self.connect_phases(sock, server, port, kind)
            self.join_channels([], kind)
        if kind == "chat":
            server = "irc.chat.twitch.tv"
            print "Connecting to {0}:{1}".format(server, port)
            self.connect_phases(sock, server, port, kind)
            self.join_channels(self.channels_to_string(
                self.config['channels']), kind)

        sock.settimeout(None)

    def connect_phases(self, sock, server, port, kind):
        sock.connect((server, port))
        pp("Sending Username " + self.config["username"])
        sock.send('USER %s\r\n' % self.config['username'])
        pp("Sending Password " + self.config["oauth_password"])
        sock.send('PASS %s\r\n' % self.config['oauth_password'])
        pp("Sending Nick " + self.config["username"])
        sock.send('NICK %s\r\n' % self.config['username'])
        self.sock[kind] = sock
        loginMsg = self.nextMessage(kind)
        if kind == "chat":
            if "376" not in self.nextMessage(kind):
                pass

    def channels_to_string(self, channel_list):
        return ','.join(channel_list)

    def join_channels(self, channels, kind):
        if kind == "chat":
            pp('Joining channels %s.' % channels)
            self.sock[kind].send('JOIN %s\r\n' % channels)
        if kind == "whisper":
            pp("Joining whisper server")
            self.sock[kind].send("CAP REQ :twitch.tv/commands\r\n")
        pp('Joined channels.')

    def leave_channels(self, channels, kind):
        pp('Leaving channels %s,' % channels)
        if kind == "chat":
            self.sock[kind].send('PART %s\r\n' % channels)
        pp('Left channels.')
