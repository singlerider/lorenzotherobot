import src.lib.commands.llama as llama_import
import globals
import requests
import json

usage = '!stream'

def stream():
    

    get_offline_status_url = 'https://api.twitch.tv/kraken/channels/' + \
        globals.channel
    get_offline_status_resp = requests.get(url=get_offline_status_url)
    offline_data = json.loads(get_offline_status_resp.content)

    try:
        return str(offline_data["status"]) + " | " + str(offline_data["display_name"]) + " playing " + str(offline_data["game"])
    except:
        return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"
