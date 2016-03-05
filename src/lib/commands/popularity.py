from src.lib.twitch import *


def popularity(args, **kwargs):
    game = args[0]
    return get_game_popularity(game)
