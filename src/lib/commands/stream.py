import json

import requests

import globals
import src.lib.commands.llama as llama_import

usage = '!stream'


def stream():
    get_offline_status_url = 'https://api.twitch.tv/kraken/channels/' + \
        globals.CURRENT_CHANNEL
    get_offline_status_resp = requests.get(url=get_offline_status_url)
    offline_data = json.loads(get_offline_status_resp.content)

    try:
        return str("".join(i for i in offline_data["status"] if ord(i) < 128)) + " | " + str(
            offline_data["display_name"]) + " playing " + str(offline_data["game"])
    except Exception as error:
        print error
        return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"
