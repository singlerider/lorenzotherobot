import src.lib.commands.llama as llama_import
import globals
from src.lib.commands.pokedex import pokedex
from src.lib.queries.pokemon_queries import *


def catch():
    pokemon_trainer = globals.CURRENT_USER
    open_position = find_open_party_positions(pokemon_trainer)
    desired_level = 5
    pokemon_id = get_pokemon_id_from_name(globals.POKEMON)
    print pokemon_id
    if len(open_position) > 0:
        return insert_user_pokemon(pokemon_trainer, pokemon_trainer, open_position[0], pokemon_id, desired_level, globals.POKEMON, None, None)
    else:
        return "No open slots in your party."