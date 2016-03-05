import json

import requests


def stream(**kwargs):
    channel = kwargs.get("channel", "testchannel")
    get_offline_status_url = 'https://api.twitch.tv/kraken/channels/' + \
        channel
    get_offline_status_resp = requests.get(url=get_offline_status_url)
    offline_data = json.loads(get_offline_status_resp.content)

    try:
        return str("".join(i for i in offline_data["status"] if ord(i) < 128)) + " | " + str(
            offline_data["display_name"]) + " playing " + str(offline_data["game"])
    except Exception as error:  # pragma: no cover
        print error
        return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"
