from src.lib.queries.pokemon_queries import *


def evolve(args, **kwargs):
    position = args[0]
    try:
        return apply_evolution(kwargs.get("username", "testuser"), position)
    except:
        return "It doesn't look like your Pokemon can evolve now. Sorry."
