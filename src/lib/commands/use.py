from src.lib.queries.pokemon_queries import *
import globals


def use(args):
    item = args[0]
    position = args[1]

    return use_item(globals.CURRENT_USER, item, position)
