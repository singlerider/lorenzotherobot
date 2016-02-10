from threading import Thread

from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./eg/brain")
bot.sort_replies()


class Conversation(Thread):

    def __init__(self, chat):
        self.thread = Thread.__init__(self)
        self.daemon = True
        self.chat = chat

    def run(self, user, username, message):
        # :singlerider!singlerider@singlerider.tmi.twitch.tv WHISPER lorenzotherobot :yo
        user = "{user}!{user}@{user}.tmi.twitch.tv".format(user=user)
        line = ":%s PRIVMSG #jtv :/w %s %s" % (user, username, message)
        reply = bot.reply(username, message)
        if reply == "[ERR: No reply matched]":
            return
        #self.sendLine(line)
        #self.chat.msg(username, reply)
        return str(reply)
