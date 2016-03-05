from src.lib.queries.pokemon_queries import *


def use(args, **kwargs):
    item = args[0]
    position = args[1]
    return use_item(kwargs.get("username", "testuser"), item, position)
