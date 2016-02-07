server = 'irc.twitch.tv'
port = 6667
username = 'lorenzotherobot'
oauth_password = 'oauth:00ra162i9zh7la2prjm4sesocq291m' # get this from http://twitchapps.com/tmi/
channel = "#singlerider"

from twisted.internet import reactor
from twisted.words.protocols import irc
from twisted.internet.protocol import ClientFactory
import time

SERVER = server
NICKNAME = username
PASSWORD = oauth_password


class Bot(irc.IRCClient):

    def __init__(self):
        self.nickname = NICKNAME
        self.password = PASSWORD
        self.channel = channel

    def dataReceived(self, data):
        print(data)
        irc.IRCClient.dataReceived(self, data)

    def signedOn(self):
        print("\033[91m\n\nYOLO, I was signed on to the server!!!\n\033[0m")
        self.join(channel)

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        reactor.stop()

    def privmsg(self, user, channel, msg):
        """Called when the bot receives a message."""

        self.msg(channel, "hi" + "\r\n")


class BotFactory(ClientFactory):
    protocol = Bot


class Whisper(irc.IRCClient):

    def __init__(self):
        self.nickname = NICKNAME
        self.password = PASSWORD

    def dataReceived(self, data):
        print(data)
        irc.IRCClient.dataReceived(self, data)

    def signedOn(self):
        print("\033[91m\n\nShhhh!!! Whispers only!\n\033[0m")
        self.sendLine("CAP REQ :twitch.tv/commands")

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        reactor.stop()

    def whisper(self, user, msg):
    	'''global whisper_user, whisper_msg
        if "/mods" in msg:
            thread.start_new_thread(get_whisper_mods_msg, (self, user, msg))
        else:
            whisper_user = user
            whisper_msg = msg'''
        print msg


class WhisperFactory(ClientFactory):
    protocol = Whisper


if __name__ == "__main__":
    reactor.connectTCP(SERVER, 6667, BotFactory())
    reactor.connectTCP("52.223.240.119", 443, WhisperFactory())
    reactor.run()
