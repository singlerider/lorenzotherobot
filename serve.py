#!/usr/bin/env python2.7
from twisted.internet import reactor
from src.bot import BotFactory
from src.config.config import config

SERVER = config["server"]

if __name__ == '__main__':
    whisper = reactor.connectTCP("52.223.240.119", 443, BotFactory("whisper"))
    chat = reactor.connectTCP(SERVER, 6667, BotFactory("chat"))
    reactor.run()
