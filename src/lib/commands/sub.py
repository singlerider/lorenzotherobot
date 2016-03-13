import json

import requests
from src.lib.queries.moderator_queries import get_moderator
from src.lib.queries.sub_queries import get_oauth


def sub(args, **kwargs):
    """
    Handled via whispers. Moderator status and usage must be handled here
    """
    usage = "sub [channel] [username]"
    if len(args) < 2:
        return usage
    channel = args[0]
    username = args[1]
    inquirer = args[2]
    moderator = get_moderator(inquirer, channel)
    if moderator is None:
        return "You must be a moderator to check sub status."
    oauth = get_oauth(channel)
    if oauth is None:
        return "This channel needs to be authenticated by visiting shane.gg/twitch/authorize"
    oauth = oauth[0]
    url = "https://api.twitch.tv/kraken/channels/" + \
        channel + "/subscriptions/" + username
    headers = {
        "Accept": "application/vnd.twitchtv.v3+json",
        "Authorization": "OAuth {token}".format(token=oauth)
    }
    try:
        resp = requests.get(url=url, headers=headers)
        data = json.loads(resp.content)
        since = data.get("created_at", None)
        if since is not None:
            return username + " has been subbed to " + channel + " since " + since + "."
        else:
            return username + " is not currently subbed to " + channel + "."
    except Exception as error:
        print error
        return "There was a problem."
