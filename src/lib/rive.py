import sys
from threading import Thread
import globals


class Conversation(Thread):

    def __init__(self, irc, channel):
        self.thread = Thread.__init__(self)
        self.daemon = True
        self.irc = irc
        self.channel = channel

    def run(self, username, message, bot):
        message = " ".join(message.split()[1:])
        reply = bot.reply(username, message)
        self.irc.send_message(self.channel, reply)
        print 'Bot>', reply
        return
