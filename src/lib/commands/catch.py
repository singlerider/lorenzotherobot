import src.lib.commands.llama as llama_import
import globals
from src.lib.commands.pokedex import pokedex
from src.lib.queries.pokemon_queries import *
from src.lib.queries.points_queries import *


def catch():
    if globals.channel_info[globals.global_channel]['caught'] == False:
        pokemon_trainer = globals.CURRENT_USER
        # This is here for if the user is brand new. This creates an entry in
        # the users table, which userpokemon is dependent on
        modify_user_points(globals.CURRENT_USER, 0)
        open_position, occupied_positions = find_open_party_positions(
            pokemon_trainer)
        desired_level = 5
        pokemon_id = get_pokemon_id_from_name(
            globals.channel_info[globals.global_channel]['pokemon'])
        print pokemon_id
        if len(open_position) > 0:
            globals.channel_info[globals.global_channel]['caught'] = True
            print globals.channel_info[globals.global_channel]
            return insert_user_pokemon(pokemon_trainer, pokemon_trainer, open_position[0], pokemon_id, desired_level, globals.channel_info[globals.global_channel]['pokemon'], None, None)
        else:
            return "No open slots in your party."
    else:
        return "Too slow!"
