#!/usr/bin/env python2.7
import json

import requests
from src.bot import BotFactory
from src.config.config import config
from twisted.internet import reactor

SERVER = config["server"]
whisper_url = "http://tmi.twitch.tv/servers?cluster=group"
whisper_resp = requests.get(url=whisper_url)
whisper_data = json.loads(whisper_resp.content)
socket = whisper_data["servers"][0].split(":")
WHISPER = [str(socket[0]), int(socket[1])]

if __name__ == '__main__':
    whisper = reactor.connectTCP(WHISPER[0], WHISPER[1], BotFactory("whisper"))
    chat = reactor.connectTCP(SERVER, 6667, BotFactory("chat"))
    reactor.run()
