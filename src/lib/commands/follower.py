from src.lib.twitch import *


def follower(args, **kwargs):
    username = args[0]
    channel = kwargs.get("channel", "testchannel")
    try:
        return get_follower_status(username=username, channel=channel)
    except:
        return "It doesn't look like your Pokemon can evolve now. Sorry."
