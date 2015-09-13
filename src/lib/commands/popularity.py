from src.lib.twitch import *


def popularity(args):

    game = args[0]

    return get_game_popularity(game)
