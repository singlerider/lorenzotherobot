from src.lib.twitch import *


def follower(args):
    user = args[0]
    try:
        return get_follower_status(user)
    except:
        return "It doesn't look like your Pokemon can evolve now. Sorry."
