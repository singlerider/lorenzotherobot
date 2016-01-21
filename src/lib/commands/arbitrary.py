# coding: utf8

import json
import random
import time

import requests

usage = "!arbitrary [emote/number]"


def emote():
    emote_url = "http://twitchemotes.com/api_cache/v2/global.json"
    emote_resp = requests.get(url=emote_url)
    emote = json.loads(emote_resp.content)
    emotes = emote["emotes"]
    random_emote = random.choice(emotes.keys())

    return random_emote


def number():
    num = range(1, 101)
    return num[random.randint(0, len(num) - 1)]


def arbitrary(args):

    if args[0] == "emote":
        return emote()

    elif args[0] == "number":
        return number()

    else:
        return usage
