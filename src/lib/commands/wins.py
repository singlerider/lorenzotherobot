"""
Developed Shane Engelman <me@5h4n3.com>
"""
import json

import globals
from src.lib.queries.moderator_queries import get_moderator


def readWins(channel):
    try:
        with open("wins.json", "r+") as f:  # read changes.json
            previous = json.loads(f.read())
        count = previous.get(channel, None)
        if count is None:  # pragma: no cover
            previous[channel] = 0
            with open("wins.json", "w") as f:  # read changes.json
                f.write(json.dumps(previous))
        return previous
    except Exception as error:  # pragma: no cover
        print error
        with open("wins.json", "w") as f:
            f.write("{}")
        return {}


def wins(args):
    username = globals.CURRENT_USER
    channel = globals.CURRENT_CHANNEL
    if len(args) < 1:
        return "{0} has {1} BR wins now! curvyMLG".format(channel, readWins(
            channel)[channel])
    moderator = get_moderator(username, channel)
    if not moderator:
        return "You must be a moderator to do that."
    action = args[0]
    delta = args[1]
    try:
        delta = int(delta)
    except:
        return "The amount to change must be a number!"
    current = readWins(channel)
    exists = current.get(channel, None)
    if not exists:  # pragma: no cover
        current[channel] = 0
    if action == "add":
        print type(current[channel]), current[channel], type(delta), delta
        current[channel] += delta
    elif action == "remove":
        current[channel] -= delta
    elif action == "set":
        current[channel] = delta
    else:
        return "Action must be \"add\" \"edit\" or \"set\""
    with open("wins.json", "w") as f:  # read changes.json
        f.write(json.dumps(current))
    return "{0} has {1} BR wins now! curvyMLG".format(
        channel, current[channel])
