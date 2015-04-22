import src.lib.commands.llama as llama_import
import globals
from src.lib.commands.pokedex import pokedex
from src.lib.queries.pokemon_queries import *
from src.lib.queries.points_queries import *


def catch():
    
    #print "globals.global_channel: ", globals.global_channel
    
    if globals.global_channel == "shedeviil_09":
        #print "globals.global_channel == shedeviil_09"
        
        if globals.shedeviil_09_CAUGHT == False:
            pokemon_trainer = globals.CURRENT_USER
            modify_user_points(globals.CURRENT_USER, 0) # This is here for if the user is brand new. This creates an entry in the users table, which userpokemon is dependent on
            open_position, occupied_positions = find_open_party_positions(pokemon_trainer)
            desired_level = 5
            pokemon_id = get_pokemon_id_from_name(globals.shedeviil_09_POKEMON)
            print pokemon_id
            if len(open_position) > 0:
                globals.shedeviil_09_CAUGHT = True
                return insert_user_pokemon(pokemon_trainer, pokemon_trainer, open_position[0], pokemon_id, desired_level, globals.shedeviil_09_POKEMON, None, None)
            else:
                return "No open slots in your party."
        else:
            return "Too slow!"
        
    else:
        #print "globals.global_channel: ", globals.global_channel
        if globals.CAUGHT == False:
            pokemon_trainer = globals.CURRENT_USER
            modify_user_points(globals.CURRENT_USER, 0) # This is here for if the user is brand new. This creates an entry in the users table, which userpokemon is dependent on
            open_position, occupied_positions = find_open_party_positions(pokemon_trainer)
            desired_level = 5
            pokemon_id = get_pokemon_id_from_name(globals.POKEMON)
            print pokemon_id
            if len(open_position) > 0:
                globals.CAUGHT = True
                return insert_user_pokemon(pokemon_trainer, pokemon_trainer, open_position[0], pokemon_id, desired_level, globals.POKEMON, None, None)
            else:
                return "No open slots in your party."
        else:
            return "Too slow!"