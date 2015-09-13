from src.lib.queries.pokemon_queries import *
import globals


def nickname(args):
    position = args[0]
    nick = args[1]

    try:
        update_nickname(nick, globals.CURRENT_USER, position)
        return nick + " 's nickname has been updated! :D"
    except:
        return "Something bad happened. You killed everyone's Pokemon :O"
