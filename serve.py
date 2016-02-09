#!/usr/bin/env python2.7
from twisted.internet import reactor
from src.bot import BotFactory
from src.config.config import config

SERVER = config["server"]

if __name__ == '__main__':
    c = BotFactory("#singlerider", "chat")
    w = BotFactory("#singlerider", "whisper")
    chat = reactor.connectTCP(SERVER, 6667, c)
    whisper = reactor.connectTCP("52.223.240.119", 443, w)
    reactor.run()
