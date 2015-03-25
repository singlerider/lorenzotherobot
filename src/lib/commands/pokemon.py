'''
Developed by Shane Engelman <me@5h4n3.com>

Pokemon Intellectual Property owned by Nintendo and Game Freak <3
'''

import random
import globals
from src.lib.commands.pokedex.pokedata import *
from src.lib.commands.pokedex import pokedex

#!pokemon battle
def battle():
    # Establishes two randomly selected pokemon as independent variables
    pokemon_1 = random.choice(master_pokemon_dict.keys())
    pokemon_2 = random.choice(master_pokemon_dict.keys())

    versus_list = [pokemon_1, pokemon_2]
    winner = random.choice(versus_list)

    p1_type = master_pokemon_dict[pokemon_1]["type1"]
    p2_type = master_pokemon_dict[pokemon_2]["type1"]

    p1_to_p2_mod = multipliers[p1_type].get(p2_type, None)
    p2_to_p1_mod = multipliers[p2_type].get(p1_type, None)

    NO_MODS = "Neither Pokemon adversely affects the other! It's {} vs {}! And the winner is {}!"
    ONE_MOD = "{} has a dammage mod of {}. {} has no mods! An exciting battle gives {} a win!"
    TWO_MODS = "{} has a mod of {}. {} has a mod of {}. After a long battle {} is the winner!"

    if p1_to_p2_mod is None:
        if p2_to_p1_mod is None:
            return NO_MODS.format(pokemon_1, pokemon_2, winner)
        else:
            return  ONE_MOD.format(pokemon_2, p2_to_p1_mod, pokemon_1, winner)
    else:
        if p2_to_p1_mod is None:
            return ONE_MOD.format(pokemon_1, p1_to_p2_mod, pokemon_2, winner)
        else:
            return TWO_MODS.format(pokemon_1, p1_to_p2_mod, pokemon_2, p2_to_p1_mod, winner)


def pokemon(args):
    usage = '!pokemon <action (battle/me)>'

    action = args[0]

    if action == "battle":
        return battle()

    if action == "me":
        pokemon = pokedex.getPokemon(globals.CURRENT_USER)

        if pokemon is not None:
            return "Your current pokemon: " + pokemon
        else:
            return "You gotta catch something first, ya dope"

    return "Usage: " + usage.replace('<', '').replace('>', '')
