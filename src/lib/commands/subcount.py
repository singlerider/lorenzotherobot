import json

import requests
from src.lib.queries.sub_queries import get_oauth


def subcount(**kwargs):
    channel = kwargs.get("channel").lstrip("#")
    oauth = get_oauth(channel)
    if oauth is None:
        return "This channel needs to be authenticated by visiting shane.gg/twitch/authorize"
    oauth = oauth[0]
    url = "https://api.twitch.tv/kraken/channels/" + \
        channel + "/subscriptions"
    headers = {
        "Accept": "application/vnd.twitchtv.v3+json",
        "Authorization": "OAuth {token}".format(token=oauth)
    }
    params = {"limit": 1}
    try:
        resp = requests.get(url=url, headers=headers, params=params)
        data = json.loads(resp.content)
        total = data["_total"]
        return channel.lstrip("#") + " has a total of {0}".format(total) + \
            " subs! Keep it up!"
    except Exception as error:
        print error
        return "There was a problem with retrieving the subcount. Lame."
