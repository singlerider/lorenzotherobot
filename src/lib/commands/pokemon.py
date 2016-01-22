'''
Developed by Shane Engelman <me@5h4n3.com>

Pokemon Intellectual Property owned by Nintendo and Game Freak <3
'''

import random

import globals
from src.lib.commands.pokedex.pokedata import master_pokemon_dict
from src.lib.queries.pokemon_queries import *


def randomPokemon():
    rarity_list = []
    for poke in master_pokemon_dict:
        for number in range(master_pokemon_dict[poke]['rarity']):
            rarity_list.append(poke)
    return rarity_list


def cron(channel):  # todo remove this arg requirement.
    channel = channel.lstrip('#')
    globals.channel_info[channel]['caught'] = False
    pocket_monster = random.choice(randomPokemon())
    globals.channel_info[channel]['pokemon'] = pocket_monster
    return "A wild " + pocket_monster + " appeared!"


def pokemon(args):
    action = args[0]
    if action == "battle":
        return battle()
    else:
        return get_user_party_info(action)
