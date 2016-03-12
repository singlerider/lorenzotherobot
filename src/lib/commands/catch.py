import globals
from src.lib.queries.points_queries import *
from src.lib.queries.pokemon_queries import *


def catch(**kwargs):
    channel = kwargs.get("channel", "testchannel")
    if globals.CHANNEL_INFO[channel]['caught'] is False:
        pokemon_trainer = kwargs.get("username", "testuser")
        # This is here for if the user is brand new. This creates an entry in
        # the users table, which userpokemon is dependent on
        modify_user_points(pokemon_trainer, 0)
        open_position, occupied_positions = find_open_party_positions(
            pokemon_trainer)
        desired_level = 5
        pokemon_id = get_pokemon_id_from_name(
            globals.CHANNEL_INFO[channel]['pokemon'])
        if pokemon_id is None:
            return "Pokemon not found! Check your spelling"
        if len(open_position) > 0:
            globals.CHANNEL_INFO[channel]['caught'] = True
            return insert_user_pokemon(
                pokemon_trainer, pokemon_trainer, open_position[0],
                pokemon_id, desired_level,
                globals.CHANNEL_INFO[channel]['pokemon'],
                None, None)
        else:
            return "No open slots in your party."
    else:
        return "Too slow!"
