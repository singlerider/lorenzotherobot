import globals
from src.lib.queries.points_queries import *
from src.lib.queries.pokemon_queries import *


def catch():
    if globals.CHANNEL_INFO[globals.CURRENT_CHANNEL]['caught'] is False:
        pokemon_trainer = globals.CURRENT_USER
        # This is here for if the user is brand new. This creates an entry in
        # the users table, which userpokemon is dependent on
        modify_user_points(globals.CURRENT_USER, 0)
        open_position, occupied_positions = find_open_party_positions(
            pokemon_trainer)
        desired_level = 5
        pokemon_id = get_pokemon_id_from_name(
            globals.CHANNEL_INFO[globals.CURRENT_CHANNEL]['pokemon'])
        if len(open_position) > 0:
            globals.CHANNEL_INFO[globals.CURRENT_CHANNEL]['caught'] = True
            return insert_user_pokemon(
                pokemon_trainer, pokemon_trainer, open_position[0],
                pokemon_id, desired_level,
                globals.CHANNEL_INFO[globals.CURRENT_CHANNEL]['pokemon'],
                None, None)
        else:
            return "No open slots in your party."
    else:
        return "Too slow!"
