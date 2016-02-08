#!/usr/bin/env python2.7
from twisted.internet import reactor
from src.bot import BotFactory, WhisperFactory
from src.config.config import config

SERVER = config["server"]
NICKNAME = config["username"]
PASSWORD = config["oauth_password"]

chat = reactor.connectTCP(SERVER, 6667, BotFactory())
whisper = reactor.connectTCP("52.223.240.119", 443, WhisperFactory())
reactor.run()
