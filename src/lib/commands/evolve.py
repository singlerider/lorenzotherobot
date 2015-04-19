from src.lib.queries.pokemon_queries import *
import globals

def evolve(args):
    position = args[0]
    try:
        return apply_evolution(globals.CURRENT_USER, position)
    except:
        return "It doesn't look like your Pokemon can evolve now. Sorry."