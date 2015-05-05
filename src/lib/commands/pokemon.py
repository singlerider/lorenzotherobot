'''
Developed by Shane Engelman <me@5h4n3.com>

Pokemon Intellectual Property owned by Nintendo and Game Freak <3
'''

import random
import globals
from src.lib.commands.pokedex.pokedata import *
from src.lib.commands.pokedex import pokedex
from src.lib.queries.pokemon_queries import *

usage = '!pokemon <action (battle/me)>'

def randomPokemon():
    rarity_list = []
    for poke in master_pokemon_dict:
        for number in range(master_pokemon_dict[poke]['rarity']):
            rarity_list.append(poke)
    return rarity_list

def cron(a=None): #todo remove this arg requirement.
    globals.CAUGHT = False
    pocket_monster = random.choice(randomPokemon())
    globals.POKEMON = pocket_monster
    return "A wild " + pocket_monster + " appeared!"

def shedeviil_09_cron(a=None): #todo remove this arg requirement.
    globals.shedeviil_09_CAUGHT = False
    pocket_monster = random.choice(randomPokemon())
    globals.shedeviil_09_POKEMON = pocket_monster
    print "trying"
    return "A wild " + pocket_monster + " appeared!"

def lycomedesgames_cron(a=None): #todo remove this arg requirement
    globals.lycomedesgames_CAUGHT = False
    pocket_monster = random.choice(randomPokemon())
    globals.lycomedesgames_POKEMON = pocket_monster
    print "trying"
    return "A wild " + pocket_monster + " appeared!"

#!pokemon battle
def battle():
    # Establishes two randomly selected pokemon as independent variables
    pokemon_1 = randomPokemon()
    pokemon_2 = randomPokemon()

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
    

    action = args[0]

    if action == "battle":
        return battle()

    
    else:
        try:
            return get_user_party_info(action)
        except Exception as err:
            print Exception, err
            return "Usage: " + usage.replace('<', '').replace('>', '')
