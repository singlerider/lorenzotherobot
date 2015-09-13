from src.lib.queries.pokemon_queries import *
import globals


def buy(args):

    id = args[0]

    return buy_items(id, globals.CURRENT_USER)
