from src.lib.queries.pokemon_queries import *


def release(args, **kwargs):
    username = kwargs.get("username", "testuser")
    if args[1].lower().lstrip("@") == username:
        position = args[0]
        return remove_user_pokemon(username.lstrip("@"), position)
    else:
        raise ValueError
