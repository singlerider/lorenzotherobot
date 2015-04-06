from src.lib.queries.pokemon_queries import *
import globals

usage = "!party [position/'members']"

def party(args):
    position = args[0]
    if position in ['1','2','3','4','5','6']:
        return get_battle_stats(globals.CURRENT_USER, position)
    elif args[0] == 'members':
        return get_user_party_info(globals.CURRENT_USER)
    else:
        return get_user_party_info(globals.CURRENT_USER)