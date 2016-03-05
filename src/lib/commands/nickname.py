from src.lib.queries.pokemon_queries import *


def nickname(args, **kwargs):
    position = args[0]
    username = kwargs.get("username", "testuser")
    nick = args[1]
    try:
        update_nickname(nick, username, position)
        return nick + " 's nickname has been updated! :D"
    except:
        return "Something bad happened. You killed everyone's Pokemon :O"
