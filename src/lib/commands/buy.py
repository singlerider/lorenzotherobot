from src.lib.queries.pokemon_queries import *


def buy(args, **kwargs):
    username = kwargs.get("username", "testuser")
    kind = args[0]
    id = args[1]
    if kind == "item":
        return buy_items(id, username)
    elif kind == "pokemon":
        return buy_pokemon(id, username)
    else:
        return "You gotta indicate if you want to !buy an \"item\" or a \"pokemon\""
