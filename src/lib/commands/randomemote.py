# coding: utf8

import random
import json
import requests

usage = "!randomemote"

def randomemote():

    emote_url = "http://twitchemotes.com/api_cache/v2/global.json"
    emote_resp = requests.get(url=emote_url)
    emote = json.loads(emote_resp.content)
    emotes = emote["emotes"]
    random_emote = random.choice(emotes.keys())

    return random_emote
