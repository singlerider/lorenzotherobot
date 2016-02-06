import sys
from threading import Thread

from rivescript import RiveScript

import globals

bot = RiveScript()
bot.load_directory("./eg/brain")
bot.sort_replies()

class Conversation(Thread):

    def __init__(self, irc, channel):
        self.thread = Thread.__init__(self)
        self.daemon = True
        self.irc = irc
        self.channel = channel

    def run(self, username, message):
        message = " ".join(message.split()[1:])
        reply = bot.reply(username, message)
        if reply == "[ERR: No reply matched]":
            return
        self.irc.send_message(self.channel, reply)
        print 'Bot>', reply
        return
