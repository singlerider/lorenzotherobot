from src.lib.queries.pokemon_queries import *


def buy(args, **kwargs):
    id = args[0]
    return buy_items(id, kwargs.get("username", "testuser"))
