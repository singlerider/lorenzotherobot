from src.lib.queries.pokemon_queries import *

def release(args):
    usage = '!release [position_number] [your_username]'
    if args[1].lower() == globals.CURRENT_USER:
        position = args[0]
        return remove_user_pokemon(globals.CURRENT_USER,position)
    else:
        return usage