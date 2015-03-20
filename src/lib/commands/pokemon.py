'''
Developed by Shane Engelman <me@5h4n3.com>

Pokemon Intellectual Property owned by Nintendo and Game Freak <3
'''

import random
import time
import re
import src.lib.commands.capture as capture_import
import globals

# Pokemon name,their type(s), and a grouping for their evolution order, in the form of a list


#evolution_set = 0: , evolution_position = 0:2, rarity = 0:3 (0:3 - higher number, more common; 3 - does not spawn)
#time = 0:3 (time quadrants in 6-hour blocks for spawning), evolution_level = some_requirement_for_evolution (moon_stone, int(level number), etc)
#attack = int(number), special_attack = int(number), defense = int(number), special_defense = int(number), health = int(number), speed = int(number)
#above ints will act as preliminary modifiers for power - current_level will be assigned in database

master_pokemon_dict = {
  'Bulbasaur': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 1,
    'evolution_position': 1,
    'rarity': 2,
    'time': 3,
    'evolution_level': 16,
    'attack': 49,
    'sp_atk': 65,
    'defense': 49,
    'sp_def': 65,
    'hp': 45,
    'speed': 45
  },
  'Ivysaur': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 1,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'evolution_level': 32,
    'attack': 62,
    'sp_atk': 65,
    'defense': 63,
    'sp_def': 80,
    'hp': 60,
    'speed': 60
  },
  'Venusaur': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 1,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 82,
    'sp_atk': 100,
    'defense': 83,
    'sp_def': 100,
    'hp': 80,
    'speed': 80
  },
  'Charmander': {
    'type1': "Fire",
    'evolution_set': 2,
    'evolution_position': 1,
    'rarity': 2,
    'time': 3,
    'evolution_level': 16,
    'attack': 39,
    'sp_atk': 60,
    'defense': 43,
    'sp_def': 50,
    'hp': 39,
    'speed': 65
  },
  'Charmeleon': {
    'type1': "Fire",
    'evolution_set': 2,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'evolution_level': 32,
    'attack': 64,
    'sp_atk': 80,
    'defense': 58,
    'sp_def': 65,
    'hp': 58,
    'speed': 80
  },
  'Charizard': {
    'type1': "Fire",
    'type2': "Flying",
    'evolution_set': 2,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 84,
    'sp_atk': 109,
    'defense': 78,
    'sp_def': 85,
    'hp': 78,
    'speed': 100
  },
  'Squirtle': {
    'type1': "Water",
    'evolution_set': 3,
    'evolution_position': 1,
    'rarity': 2,
    'time': 3,
    'evolution_level': 16,
    'attack': 48,
    'sp_atk': 50,
    'defense': 65,
    'sp_def': 64,
    'hp': 44,
    'speed': 43
  },
  'Wartortle': {
    'type1': "Water",
    'evolution_set': 3,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'evolution_level': 32,
    'attack': 63,
    'sp_atk': 65,
    'defense': 80,
    'sp_def': 80,
    'hp': 59,
    'speed': 58
  },
  'Blastoise': {
    'type1': "Water",
    'evolution_set': 3,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 83,
    'sp_atk': 85,
    'defense': 100,
    'sp_def': 105,
    'hp': 79,
    'speed': 78
  },
  'Caterpie': {
    'type1': "Bug",
    'evolution_set': 4,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 7,
    'attack': 30,
    'sp_atk': 20,
    'defense': 35,
    'sp_def': 20,
    'hp': 45,
    'speed': 45
  },
  'Metapod': {
    'type1': "Bug",
    'evolution_set': 4,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'evolution_level': 11,
    'attack': 50,
    'sp_atk': 25,
    'defense': 55,
    'sp_def': 25,
    'hp': 50,
    'speed': 30
  },
  'Butterfree': {
    'type1': "Bug",
    'type2': "Flying",
    'evolution_set': 4,
    'evolution_position': 3,
    'rarity': 1,
    'time': 3,
    'attack': 45,
    'sp_atk': 90,
    'defense': 50,
    'sp_def': 80,
    'hp': 60,
    'speed': 70
  },
  'Weedle': {
    'type1': "Bug",
    'type2': "Poison",
    'evolution_set': 5,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 7,
    'attack': 35,
    'sp_atk': 20,
    'defense': 30,
    'sp_def': 20,
    'hp': 40,
    'speed': 50
  },
  'Kakuna': {
    'type1': "Bug",
    'type2': "Poison",
    'evolution_set': 5,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'evolution_level': 10,
    'attack': 25,
    'sp_atk': 25,
    'defense': 50,
    'sp_def': 25,
    'hp': 45,
    'speed': 35
  },
  'Beedrill': {
    'type1': "Bug",
    'type2': "Poison",
    'evolution_set': 5,
    'evolution_position': 3,
    'rarity': 2,
    'time': 3,
    'attack': 90,
    'sp_atk': 45,
    'defense': 40,
    'sp_def': 80,
    'hp': 65,
    'speed': 75
  },
  'Pidgey': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 6,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 18,
    'attack': 45,
    'sp_atk': 35,
    'defense': 40,
    'sp_def': 35,
    'hp': 40,
    'speed': 56
  },
  'Pidgeotto': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 6,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 36,
    'attack': 60,
    'sp_atk': 50,
    'defense': 55,
    'sp_def': 50,
    'hp': 63,
    'speed': 71
  },
  'Pidgeot': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 6,
    'evolution_position': 3,
    'rarity': 1,
    'time': 3,
    'attack': 80,
    'sp_atk': 70,
    'defense': 75,
    'sp_def': 70,
    'hp': 83,
    'speed': 101
  },
  'Rattata': {
    'type1': "Normal",
    'evolution_set': 7,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 20,
    'attack': 56,
    'sp_atk': 25,
    'defense': 35,
    'sp_def': 35,
    'hp':30,
    'speed': 72
  },
  'Raticate': {
    'type1': "Normal",
    'evolution_set': 7,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 81,
    'sp_atk': 50,
    'defense': 60,
    'sp_def': 70,
    'hp': 55,
    'speed': 97
  },
  'Spearow': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 8,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 20,
    'attack': 60,
    'sp_atk': 31,
    'defense': 30,
    'sp_def': 31,
    'hp': 40,
    'speed': 70
  },
  'Fearow': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 8,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'attack': 90,
    'sp_atk': 61,
    'defense': 65,
    'sp_def': 61,
    'hp': 65,
    'speed': 100
  },
  'Ekans': {
    'type1': "Poison",
    'evolution_set': 9,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 22,
    'attack': 60,
    'sp_atk': 40,
    'defense': 44,
    'sp_def': 54,
    'hp': 35,
    'speed': 55
  },
  'Arbok': {
    'type1': "Poison",
    'evolution_set': 9,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'attack': 85,
    'sp_atk': 65,
    'defense': 69,
    'sp_def': 79,
    'hp': 60,
    'speed': 80
  },
  'Pikachu': {
    'type1': "Electric",
    'evolution_set': 10,
    'evolution_position': 1,
    'rarity': 2,
    'time': 3,
    'evolution_level': 16,
    'evolution_item': 'Thunderstone',
    'attack': 55,
    'sp_atk': 50,
    'defense': 40,
    'sp_def': 50,
    'hp': 35,
    'speed': 90
  },
  'Raichu': {
    'type1': "Electric",
    'evolution_set': 10,
    'evolution_position': 2,
    'rarity': 0,
    'time': 3,
    'attack': 90,
    'sp_atk': 90,
    'defense': 55,
    'sp_def': 80,
    'hp': 60,
    'speed': 110
  },
  'Sandshrew': {
    'type1': "Ground",
    'evolution_set': 11,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 22,
    'attack': 75,
    'sp_atk': 20,
    'defense': 85,
    'sp_def': 30,
    'hp': 50,
    'speed': 40
  },
  'Sandslash': {
    'type1': "Ground",
    'evolution_set': 11,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 100,
    'sp_atk': 45,
    'defense': 110,
    'sp_def': 55,
    'hp': 75,
    'speed': 65
  },
  'Nidoran Female': {
    'type1': "Poison",
    'evolution_set': 12,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 16,
    'attack': 47,
    'sp_atk': 40,
    'defense': 52,
    'sp_def': 40,
    'hp': 55,
    'speed': 41
  },
  'Nidorina': {
    'type1': "Poison",
    'evolution_set': 12,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Moon Stone',
    'attack': 62,
    'sp_atk': 55,
    'defense': 67,
    'sp_def': 55,
    'hp': 70,
    'speed': 56
  },
  'Nidoqueen': {
    'type1': "Poison",
    'type2': "Ground",
    'evolution_set': 12,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 92,
    'sp_atk': 75,
    'defense': 87,
    'sp_def': 85,
    'hp': 90,
    'speed': 76
  },
  'Nidoran Male': {
    'type1': "Poison",
    'evolution_set': 13,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 16,
    'attack': 46,
    'sp_atk': 40,
    'defense': 57,
    'sp_def': 40,
    'hp': 46,
    'speed': 50
  },
  'Nidorino': {
    'type1': "Poison",
    'evolution_set': 13,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Moon Stone',
    'attack': 72,
    'sp_atk': 55,
    'defense': 57,
    'sp_def': 55,
    'hp': 61,
    'speed': 65
  },
  'Nidoking': {
    'type1': "Poison",
    'type2': "Ground",
    'evolution_set': 13,
    'evolution_position': 3,
    'rarity': 3,
    'time': 3,
    'attack': 102,
    'sp_atk': 85,
    'defense': 77,
    'sp_def': 75,
    'hp': 81,
    'speed': 85
  },
  'Clefairy': {
    'type1': "Fairy",
    'evolution_set': 14,
    'evolution_position': 1,
    'rarity': 1,
    'time': 3,
    'evolution_level': 16,
    'attack': 70,
    'sp_atk': 60,
    'defense': 48,
    'sp_def': 65,
    'hp': 70,
    'speed': 35
  },
  'Clefable': {
    'type1': "Fairy",
    'evolution_set': 14,
    'evolution_position': 2,
    'rarity': 0,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Moon Stone',
    'attack': 70,
    'sp_atk': 95,
    'defense': 73,
    'sp_def': 90,
    'hp': 95,
    'speed': 60
  },
  'Vulpix': {
    'type1': "Fire",
    'evolution_set': 15,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 30,
    'evolution_item': 'Fire Stone',
    'attack': 41,
    'sp_atk': 50,
    'defense': 40,
    'sp_def': 65,
    'hp': 38,
    'speed': 65
  },
  'Ninetales': {
    'type1': "Fire",
    'evolution_set': 15,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'attack': 76,
    'sp_atk': 81,
    'defense': 75,
    'sp_def': 100,
    'hp': 73,
    'speed': 100
  },
  'Jigglypuff': {
    'type1': "Normal",
    'type2': "Fairy",
    'evolution_set': 16,
    'evolution_position': 1,
    'rarity': 1,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Moon Stone',
    'attack': 45,
    'sp_atk': 45,
    'defense': 20,
    'sp_def': 25,
    'hp': 115,
    'speed': 20
  },
  'Wigglytuff': {
    'type1': "Normal",
    'type2': "Fairy",
    'evolution_set': 16,
    'evolution_position': 2,
    'rarity': 0,
    'time': 3,
    'attack': 70,
    'sp_atk': 85,
    'defense': 45,
    'sp_def': 50,
    'hp': 140,
    'speed': 45
  },
  'Zubat': {
    'type1': "Poison",
    'type2': "Flying",
    'evolution_set': 17,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 22,
    'attack': 45,
    'sp_atk': 30,
    'defense': 35,
    'sp_def': 40,
    'hp': 40,
    'speed': 55
  },
  'Golbat': {
    'type1': "Poison",
    'type2': "Flying",
    'evolution_set': 17,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 75,
    'sp_atk': 65,
    'defense': 70,
    'sp_def': 75,
    'hp': 75,
    'speed': 90
  },
  'Oddish': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 18,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 21,
    'attack': 50,
    'sp_atk': 75,
    'defense': 55,
    'sp_def': 65,
    'hp': 45,
    'speed': 30
  },
  'Gloom': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 18,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Leaf Stone',
    'attack': 65,
    'sp_atk': 85,
    'defense': 70,
    'sp_def': 75,
    'hp': 60,
    'speed': 40
  },
  'Vileplume': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 18,
    'evolution_position': 3,
    'rarity': 1,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 75,
    'sp_atk': 110,
    'defense': 85,
    'sp_def': 90,
    'hp': 75,
    'speed': 50
  },
  'Paras': {
    'type1': "Bug",
    'type2': "Grass",
    'evolution_set': 19,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 24,
    'attack': 70,
    'sp_atk': 45,
    'defense': 55,
    'sp_def': 55,
    'hp': 35,
    'speed': 25
  },
  'Parasect': {
    'type1': "Bug",
    'type2': "Grass",
    'evolution_set': 19,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 95,
    'sp_atk': 60,
    'defense': 80,
    'sp_def': 80,
    'hp': 60,
    'speed': 30
  },
  'Venonat': {
    'type1': "Bug",
    'type2': "Poison",
    'evolution_set': 20,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 31,
    'attack': 55,
    'sp_atk': 40,
    'defense': 50,
    'sp_def': 55,
    'hp': 60,
    'speed': 45
  },
  'Venomoth': {
    'type1': "Bug",
    'type2': "Poison",
    'evolution_set': 20,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 70,
    'sp_atk': 90,
    'defense': 60,
    'sp_def': 75,
    'hp': 70,
    'speed': 90
  },
  'Diglett': {
    'type1': "Ground",
    'evolution_set': 21,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 26,
    'attack': 55,
    'sp_atk': 35,
    'defense': 25,
    'sp_def': 45,
    'hp': 10,
    'speed': 95
  },
  'Dugtrio': {
    'type1': "Ground",
    'evolution_set': 21,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 80,
    'sp_atk': 50,
    'defense': 50,
    'sp_def': 70,
    'hp': 35,
    'speed': 120
  },
  'Meowth': {
    'type1': "Normal",
    'evolution_set': 22,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 28,
    'attack': 45,
    'sp_atk': 40,
    'defense': 35,
    'sp_def': 40,
    'hp': 40,
    'speed': 90
  },
  'Persian': {
    'type1': "Normal",
    'evolution_set': 22,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'attack': 70,
    'sp_atk': 65,
    'defense': 60,
    'sp_def': 65,
    'hp': 65,
    'speed': 115
  },
  'Psyduck': {
    'type1': "Water",
    'evolution_set': 23,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 33,
    'attack': 52,
    'sp_atk': 65,
    'defense': 48,
    'sp_def': 50,
    'hp': 50,
    'speed': 55
  },
  'Golduck': {
    'type1': "Water",
    'evolution_set': 23,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'attack': 82,
    'sp_atk': 95,
    'defense': 78,
    'sp_def': 80,
    'hp': 80,
    'speed': 85
  },
  'Mankey': {
    'type1': "Fighting",
    'evolution_set': 24,
    'evolution_position': 1,
    'rarity': 2,
    'time': 3,
    'evolution_level': 28,
    'attack': 80,
    'sp_atk': 35,
    'defense': 35,
    'sp_def': 45,
    'hp': 40,
    'speed': 70
  },
  'Primeape': {
    'type1': "Fighting",
    'evolution_set': 24,
    'evolution_position': 2,
    'rarity': 3,
    'time': 3,
    'attack': 105,
    'sp_atk': 60,
    'defense': 60,
    'sp_def': 70,
    'hp': 65,
    'speed': 95
  },
  'Growlithe': {
    'type1': "Fire",
    'evolution_set': 25,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 30,
    'evolution_item': 'Fire Stone',
    'attack': 70,
    'sp_atk': 70,
    'defense': 45,
    'sp_def': 50,
    'hp': 55,
    'speed': 60
  },
  'Arcanine': {
    'type1': "Fire",
    'evolution_set': 25,
    'evolution_position': 2,
    'rarity': 0,
    'time': 3,
    'attack': 110,
    'sp_atk': 100,
    'defense': 80,
    'sp_def': 80,
    'hp': 90,
    'speed': 95
  },
  'Poliwag': {
    'type1': "Water",
    'evolution_set': 26,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 25,
    'attack': 50,
    'sp_atk': 40,
    'defense': 40,
    'sp_def': 40,
    'hp': 40,
    'speed': 90
  },
  'Poliwhirl': {
    'type1': "Water",
    'evolution_set': 26,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'Water Stone',
    'attack': 65,
    'sp_atk': 50,
    'defense': 65,
    'sp_def': 50,
    'hp': 65,
    'speed': 90
  },
  'Poliwrath': {
    'type1': "Water",
    'evolution_set': 26,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 95,
    'sp_atk': 70,
    'defense': 95,
    'sp_def': 90,
    'hp': 90,
    'speed': 70
  },
  'Abra': {
    'type1': "Psychic",
    'evolution_set': 27,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 16,
    'attack': 20,
    'sp_atk': 105,
    'defense': 15,
    'sp_def': 55,
    'hp': 25,
    'speed': 90
  },
  'Kadabra': {
    'type1': "Psychic",
    'evolution_set': 27,
    'evolution_position': 2,
    'rarity': 1,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'trade',
    'attack': 35,
    'sp_atk': 120,
    'defense': 30,
    'sp_def': 70,
    'hp': 40,
    'speed': 105
  },
  'Alakazam': {
    'type1': "Psychic",
    'evolution_set': 27,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 50,
    'sp_atk': 135,
    'defense': 45,
    'sp_def': 95,
    'hp': 55,
    'speed': 120
  },
  'Machop': {
    'type1': "Fighting",
    'evolution_set': 28,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 28,
    'attack': 80,
    'sp_atk': 35,
    'defense': 50,
    'sp_def': 35,
    'hp': 70,
    'speed': 35
  },
  'Machoke': {
    'type1': "Fighting",
    'evolution_set': 28,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'trade',
    'attack': 100,
    'sp_atk': 50,
    'defense': 70,
    'sp_def': 60,
    'hp': 80,
    'speed': 45
  },
  'Machamp': {
    'type1': "Fighting",
    'evolution_set': 28,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 130,
    'sp_atk': 65,
    'defense': 80,
    'sp_def': 85,
    'hp': 90,
    'speed': 55
  },
  'Bellsprout': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 29,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 21,
    'attack': 75,
    'sp_atk': 70,
    'defense': 35,
    'sp_def': 30,
    'hp': 50,
    'speed': 40
  },
  'Weepinbell': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 29,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 30,
    'evolution_item': 'Leaf Stone',
    'attack': 90,
    'sp_atk': 85,
    'defense': 50,
    'sp_def': 45,
    'hp': 65,
    'speed': 55
  },
  'Victreebel': {
    'type1': "Grass",
    'type2': "Poison",
    'evolution_set': 29,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 105,
    'sp_atk': 100,
    'defense': 65,
    'sp_def': 70,
    'hp': 80,
    'speed': 70
  },
  'Tentacool': {
    'type1': "Water",
    'type2': "Poison",
    'evolution_set': 30,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 50,
    'defense': 35,
    'sp_def': 100,
    'hp': 40,
    'speed': 70
  },
  'Tentacruel': {
    'type1': "Water",
    'type2': "Poison",
    'evolution_set': 30,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 70,
    'sp_atk': 80,
    'defense': 65,
    'sp_def': 120,
    'hp': 80,
    'speed': 100
  },
  'Geodude': {
    'type1': "Rock",
    'type2': "Ground",
    'evolution_set': 31,
    'evolution_position': 1,
    'rarity': 3,
    'time': 3,
    'evolution_level': 25,
    'attack': 80,
    'sp_atk': 30,
    'defense': 100,
    'sp_def': 30,
    'hp': 40,
    'speed': 20
  },
  'Graveler': {
    'type1': "Rock",
    'type2': "Ground",
    'evolution_set': 31,
    'evolution_position': 2,
    'rarity': 2,
    'time': 3,
    'evolution_level': 32,
    'evolution_item': 'trade',
    'attack': 95,
    'sp_atk': 45,
    'defense': 115,
    'sp_def': 45,
    'hp': 55,
    'speed': 35
  },
  'Golem': {
    'type1': "Rock",
    'type2': "Ground",
    'evolution_set': 31,
    'evolution_position': 3,
    'rarity': 0,
    'time': 3,
    'attack': 120,
    'sp_atk': 55,
    'defense': 130,
    'sp_def': 65,
    'hp': 80,
    'speed': 45
  },
  'Ponyta': {
    'type1': "Fire",
    'evolution_set': 32,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Rapidash': {
    'type1': "Fire",
    'evolution_set': 32,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Slowpoke': {
    'type1': "Water",
    'type2': "Psychic",
    'evolution_set': 33,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Slowbro': {
    'type1': "Water",
    'type2': "Psychic",
    'evolution_set': 33,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Magnemite': {
    'type1': "Electric",
    'type2': "Steel",
    'evolution_set': 34,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Magneton': {
    'type1': "Electric",
    'type2': "Steel",
    'evolution_set': 34,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  "Farfetch'd": {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 35,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Doduo': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 35,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dodrio': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 36,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Seel': {
    'type1': "Water",
    'evolution_set': 37,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dewgong': {
    'type1': "Water",
    'evolution_set': 37,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Grimer': {
    'type1': "Poison",
    'evolution_set': 38,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Muk': {
    'type1': "Poison",
    'evolution_set': 38,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Shellder': {
    'type1': "Water",
    'evolution_set': 39,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Cloyster': {
    'type1': "Water",
    'type2': "Ice",
    'evolution_set': 39,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Gastly': {
    'type1': "Ghost",
    'type2': "Poison",
    'evolution_set': 40,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Haunter': {
    'type1': "Ghost",
    'type2': "Poison",
    'evolution_set': 40,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Gengar': {
    'type1': "Ghost",
    'type2': "Poison",
    'evolution_set': 40,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Onix': {
    'type1': "Rock",
    'type2': "Ground",
    'evolution_set': 41,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Drowzee': {
    'type1': "Psychic",
    'evolution_set': 42,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Hypno': {
    'type1': "Psychic",
    'evolution_set': 42,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Krabby': {
    'type1': "Water",
    'evolution_set': 43,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Kingler': {
    'type1': "Water",
    'evolution_set': 43,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Voltorb': {
    'type1': "Electric",
    'evolution_set': 44,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Electrode': {
    'type1': "Electric",
    'evolution_set': 44,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Exeggcute': {
    'type1': "Grass",
    'type2': "Psychic",
    'evolution_set': 45,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Exeggcuter': {
    'type1': "Grass",
    'type2': "Psychic",
    'evolution_set': 45,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Cubone': {
    'type1': "Ground",
    'evolution_set': 46,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Marowak': {
    'type1': "Ground",
    'evolution_set': 46,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Doduo': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 47,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dodrio': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 47,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Hitmonlee': {
    'type1': "Fighting",
    'evolution_set': 48,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Hitmonchan': {
    'type1': "Fighting",
    'evolution_set': 49,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Lickitung': {
    'type1': "Normal",
    'evolution_set': 50,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Koffing': {
    'type1': "Poison",
    'evolution_set': 51,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Weezing': {
    'type1': "Poison",
    'evolution_set': 51,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Rhyhorn': {
    'type1': "Ground",
    'evolution_set': 52,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Rhydon': {
    'type1': "Ground",
    'type2': "Rock",
    'evolution_set': 52,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Chansey': {
    'type1': "Normal",
    'evolution_set': 53,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Tangela': {
    'type1': "Grass",
    'evolution_set': 54,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Kangaskhan': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 55,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Horsea': {
    'type1': "Water",
    'evolution_set': 56,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Seadra': {
    'type1': "Water",
    'evolution_set': 56,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Goldeen': {
    'type1': "Water",
    'evolution_set': 57,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Seaking': {
    'type1': "Water",
    'evolution_set': 57,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Staryu': {
    'type1': "Water",
    'evolution_set': 58,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Starmie': {
    'type1': "Water",
    'evolution_set': 58,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Mr. Mime': {
    'type1': "Psychic",
    'type2': "Flying",
    'evolution_set': 59,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Scyther': {
    'type1': "Bug",
    'type2': "Flying",
    'evolution_set': 60,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Jynx': {
    'type1': "Ice",
    'type2': "Psychic",
    'evolution_set': 61,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Electabuzz': {
    'type1': "Electric",
    'evolution_set': 62,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Magmar': {
    'type1': "Fire",
    'evolution_set': 63,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Pinsir': {
    'type1': "Bug",
    'type2': "Flying",
    'evolution_set': 64,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Tauros': {
    'type1': "Normal",
    'evolution_set': 65,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Magikarp': {
    'type1': "Water",
    'evolution_set': 66,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Gyrados': {
    'type1': "Water",
    'type2': "Flying",
    'evolution_set': 66,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Lapras': {
    'type1': "Water",
    'type2': "Ice",
    'evolution_set': 67,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Ditto': {
    'type1': "Normal",
    'evolution_set': 68,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Eevee': {
    'type1': "Normal",
    'evolution_set': 69,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Vaporeon': {
    'type1': "Water",
    'evolution_set': 69,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Jolteon': {
    'type1': "Electric",
    'evolution_set': 69,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Flareon': {
    'type1': "Fire",
    'evolution_set': 69,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Porygon': {
    'type1': "Normal",
    'evolution_set': 70,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Omanyte': {
    'type1': "Rock",
    'type2': "Water",
    'evolution_set': 71,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Omastar': {
    'type1': "Rock",
    'type2': "Water",
    'evolution_set': 71,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Kabuto': {
    'type1': "Rock",
    'type2': "Water",
    'evolution_set': 72,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Kabutops': {
    'type1': "Rock",
    'type2': "Water",
    'evolution_set': 72,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Aerodactyl': {
    'type1': "Rock",
    'type2': "Flying",
    'evolution_set': 73,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Snorlax': {
    'type1': "Normal",
    'evolution_set': 74,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Articuno': {
    'type1': "Rock",
    'type2': "Flying",
    'evolution_set': 75,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Zapdos': {
    'type1': "Zapdos",
    'type2': "Flying",
    'evolution_set': 76,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Moltres': {
    'type1': "Water",
    'type2': "Flying",
    'evolution_set': 77,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dratini': {
    'type1': "Dragon",
    'evolution_set': 78,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dragonair': {
    'type1': "Dragon",
    'evolution_set': 78,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Dragonite': {
    'type1': "Dragon",
    'type2': "Flying",
    'evolution_set': 78,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Mewtwo': {
    'type1': "Psychic",
    'evolution_set': 79,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Mew': {
    'type1': "Psychic",
    'evolution_set': 80,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  'Missingno': {
    'type1': "Normal",
    'type2': "Flying",
    'evolution_set': 0,
    'evolution_position': 0,
    'rarity': 3,
    'time': 3,
    'evolution_level': 'trade',
    'attack': 40,
    'sp_atk': 20,
    'defense': 10,
    'sp_def': 5,
    'hp': 30,
    'speed': 15
  },
  
}

print_dict = {}
    
evolution_index = []

pokemon_1_cat = []
pokemon_2_cat = []

pokemon_1_mod = []
pokemon_2_mod = []

evolution_cat = []

multipliers = {
    'Normal': {
            'Fighting': 2.0,
            'Ghost': 0.0,
            },
    'Fighting': {
             'Flying': 2.0,
             'Rock': 0.5,
             'Bug': 0.5,
             'Psychic': 2.0,
             'Dark': 0.5,
             'Fairy': 2.0
             },
    'Flying': {
             'Fighting': 0.5,
             'Ground': 0.0,
             'Rock': 2.0,
             'Bug': 0.5,
             'Grass': 0.5,
             'Electric': 2.0,
             'Ice': 2.0 
             },
    'Poison': {
             'Fighting': 0.5,
             'Poison': 0.5,
             'Ground': 2.0,
             'Bug': 0.5,
             'Grass': 0.5,
             'Psychic': 2.0,
             'Fairy': 0.5
             },
    'Ground': {
             'Poison': 0.5,
             'Rock': 0.5,
             'Water': 2.0,
             'Grass': 2.0,
             'Electric': 0.0,
             'Ice': 2.0  
             },
    'Rock': {
             'Normal': 0.5,
             'Fighting': 2.0,
             'Flying': 0.5,
             'Poison': 0.5,
             'Ground': 2.0,
             'Steel': 2.0,
             'Fire': 0.5,
             'Water': 2.0,
             'Grass': 2.0
             },
    'Bug': {
            'Fighting': 0.5,
            'Flying': 2.0,
            'Ground': 0.5,
            'Rock': 2.0,
            'Fire': 2.0,
            'Grass': 2.0
            },
    'Ghost': {
              'Normal': 0.0,
              'Fighting': 0.0,
              'Poison': 0.5,
              'Bug': 0.5,
              'Ghost': 2.0,
              'Dark': 2.0
              },
    'Steel': {
              'Normal': 0.5,
              'Fighting': 2.0,
              'Flying': 0.5,
              'Poison': 0.0,
              'Ground': 2.0,
              'Rock': 0.5,
              'Bug': 0.5,
              'Steel': 0.5,
              'Fire': 2.0,
              'Grass': 0.5,
              'Psychic': 0.5,
              'Ice': 0.5,
              'Dragon': 0.5,
              'Fairy': 0.5
              },
    'Fire': {
             'Ground': 2.0,
             'Rock': 2.0,
             'Bug': 0.5,
             'Steel': 0.5,
             'Fire': 0.5,
             'Water': 2.0,
             'Grass': 0.5,
             'Ice': 0.5,
             'Fairy': 0.5
             },
    'Water': {
              'Steel': 0.5,
              'Fire': 0.5,
              'Water': 0.5,
              'Grass': 2.0,
              'Electric': 2.0,
              'Ice': 0.5
              },
    'Grass': {
              'Flying': 2.0,
              'Poison': 2.0,
              'Ground': 0.5,
              'Bug': 2.0,
              'Fire': 2.0,
              'Water': 0.5,
              'Grass': 0.5,
              'Electric': 0.5,
              'Ice': 2.0
              },
    'Electric': {
                 'Flying': 0.5,
                 'Ground': 2.0,
                 'Steel': 0.5,
                 'Electric': 0.5
                 },
    'Psychic': {
                'Fighting': 0.5,
                'Bug': 2.0,
                'Ghost': 2.0,
                'Psychic': 0.5,
                'Dark': 2.0
                },
    'Ice': {
            'Fighting': 2.0,
            'Rock': 2.0,
            'Steel': 2.0,
            'Fire': 2.0,
            'Ice': 0.5
            },
    'Dragon': {
               'Fire': 0.5,
               'Water': 0.5,
               'Grass': 0.5,
               'Electric': 0.5,
               'Ice': 2.0,
               'Dragon': 2.0,
               'Fairy': 2.0
               },
    'Dark': {
             'Fighting': 2.0,
             'Bug': 2.0,
             'Ghost': 0.5,
             'Psychic': 0.0,
             'Dark': 0.5,
             'Fairy': 2.0
             },
    'Fairy': {
              'Fighting': 0.5,
              'Poison': 2.0,
              'Bug': 0.5,
              'Steel': 2.0,
              'Dragon': 0.0,
              'Dark': 0.5
              }   
}

def pokemon_calculate():
    rarity_list = []
    
    for poke in master_pokemon_dict:
        for number in range(master_pokemon_dict[poke]['rarity']):
            rarity_list.append(poke)
    
    pokemon_choice = random.choice (rarity_list)
    print "pokemon choice: ", pokemon_choice
    print "rarity list: ", rarity_list

def pokemon(args):
    
    usage = '!pokemon <action (battle/print/evolution)> <name ([if battle - now]/pokemon name)>'
    
    action = args[0]
    #name = args[1]
    
    
    poke_master = globals.CURRENT_USER
    

    def get_fighting_index():
        
        #pokemon 1 is electric(mod) and psychic(mod). weak against ground(opp) and bug(opp)/ghost(opp)
        #pokemon 2 is ghost(mod) and dark(mod). weak against dark(opp) and fighting(opp)/bug(opp)/fairy(opp)
        
        #pokemon 1 will be affected by pokemon 2 x2, resulting in a max index of 2
        #pokemon 2 will be affected by pokemon 1 x1, resulting in a max index of 1
        
        #pokemon2 will be victorious due to its lower damage index
        
        pokemon_1_opp = []
        pokemon_2_opp = []
        
        pokemon_1_index = []
        pokemon_2_index = []

        if len(pokemon_1_mod) == 1:
            pokemon_1_opp.append(multipliers[pokemon_1_mod[0]])
        else:
            pokemon_1_opp.append(multipliers[pokemon_1_mod[0]], multipliers[pokemon_1_mod[1]])
        if len(pokemon_1_mod) == 1:
            pokemon_2_opp.append(multipliers[pokemon_2_mod[0]])
        else:
            pokemon_2_opp.append(multipliers[pokemon_2_mod[0]], multipliers[pokemon_2_mod[1]])
                
        if pokemon_1_mod in pokemon_2_opp:
            for type, index in pokemon_2_opp.iteritems():
                pokemon_2_index.append(type, index)
        if pokemon_2_mod in pokemon_1_opp:
            for type, index in pokemon_1_opp.iteritems():
                pokemon_1_index.append(type, index)
                
        if pokemon_1_index > pokemon_2_index:
            return "pokemon 2 wins"
        elif pokemon_2_index > pokemon_1_index:
            return "pokemon 1 wins"
        else:
            return "nothing happened"
                
    
     
    # Script that handles battle    
    def battle():
        # Establishes two randomly selected pokemon as independent variables
        #print "master_pokemon_dict: ", master_pokemon_dict
        
        pokemon_1 = random.choice (master_pokemon_dict.keys())
        print "pokemon_1: " + pokemon_1
        pokemon_2 = random.choice (master_pokemon_dict.keys())
        print "pokemon_2: " + pokemon_2
        
        if "type2" in master_pokemon_dict[pokemon_1]:
            pokemon_1_type = master_pokemon_dict[pokemon_1]["type1"], master_pokemon_dict[pokemon_1]["type2"]
            print "pokemon_1_types: ", pokemon_1_type
        else:
            pokemon_1_type = master_pokemon_dict[pokemon_1]["type1"]
            print "pokemon_1_type: " + pokemon_1_type
        
        if "type2" in master_pokemon_dict[pokemon_2]:
            pokemon_2_type = master_pokemon_dict[pokemon_2]["type1"], master_pokemon_dict[pokemon_2]["type2"]
            print "pokemon_2_types: ", pokemon_2_type
        else:
            pokemon_2_type = master_pokemon_dict[pokemon_1]["type1"]
            print "pokemon_2_type: " + pokemon_2_type       
        
        versus_list = [pokemon_1, pokemon_2]
        
        winner = random.choice (versus_list)
        
        return "It's " + pokemon_1 +" versus " + pokemon_2 + "! " + winner + " wins!"
        
    #Return corresponding evolutionary set
    def evolution():
        #Iterate through nested list, returning Pokemon name, type, and set
        #and adding it to empty evolution_set
        for poke,__,set in master_pokemon:
            
            if args[1] == poke.lower():
                evolution_index.append(set)

                for index in evolution_index:
                    pass
                
                    if set == index:
                        evolution_cat.append(" ".join([poke,set]))
                        
                
        #evolved_pokemon = random.choice (evolution_set)
                if set == evolution_index[0]:
                    print "MATCH FOR INDEX " + str(evolution_index[0])
                    print evolution_cat[0]
        #random.shuffle(master_pokemon)
                return str(evolution_index[0])
    
    def print_pokemon():
        
        print_dict[0] = args[1]

        #for item in master_pokemon:
        #    pass
        
        for name, type, group in master_pokemon:
            
            if group == "3":
                print str(name)
            
            if args[1].lower() in name.lower():
                
                evolution_index.append(group)
                for index in evolution_index:
                    pass
                    print str(index)
                
                    if group == index:
                        print name + " Checking for working status"
                print "Match: " + str(name) + " is a " + str(type) + str(group)
                return " ".join([str(name) + " is type: ",str(type).replace("(", "").replace(")","").replace(",", " ")])
      
    #print ("Name List: " + str(name_list))
    #print ("Evolution Set: " + str(evolution_set))
    #print ("Pocket Monster " + str(pocket_monster))
        
    #return getmultiplier()
    if action == "battle":# and name.lower() == "now":
        return battle()
    elif action == "me":
        if capture_import.pokemon_query(poke_master) is not "":
            return capture_import.pokemon_query(poke_master)
        else:
            return "You gotta catch something first, ya dope"
    elif action == "evolution":
        return evolution()
    elif action == "print":
        return print_pokemon()
    else:
        return "Usage: " + usage.replace('<','').replace('>','')
    print "At least this works"
    #else:
        # return a thing