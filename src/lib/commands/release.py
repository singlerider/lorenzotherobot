import globals
from src.lib.queries.pokemon_queries import *


def release(args):
    if args[1].lower().lstrip("@") == globals.CURRENT_USER:
        position = args[0]
        return remove_user_pokemon(globals.CURRENT_USER.lstrip("@"), position)
    else:
        raise ValueError
