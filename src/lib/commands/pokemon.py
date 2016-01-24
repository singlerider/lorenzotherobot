import random

import globals
from src.lib.commands.pokedex.pokedata import master_pokemon_dict
from src.lib.queries.pokemon_queries import *


def random_pokemon():
    rarity_list = []
    for poke in master_pokemon_dict:
        for number in range(master_pokemon_dict[poke]['rarity']):
            rarity_list.append(poke)
    return rarity_list


def cron(channel):  # todo remove this arg requirement.
    channel = channel.lstrip('#')
    globals.CHANNEL_INFO[channel]['caught'] = False
    pocket_monster = random.choice(random_pokemon())
    globals.CHANNEL_INFO[channel]['pokemon'] = pocket_monster
    return "A wild " + pocket_monster + " appeared!"
