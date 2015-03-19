'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import random
import time
import re
import src.lib.commands.capture as capture_import
import globals

# Pokemon name,their type(s), and a grouping for their evolution order, in the form of a list
master_pokemon = [
        [ 'Bulbasaur', ('Grass' , 'Poison') , '0' ],
        [ 'Ivysaur', ('Grass' , 'Poison') , '0' ],
        [ 'Venusaur', ('Grass' , 'Poison') , '0' ],
        [ 'Charmander', ('Fire',) , '1' ],
        [ 'Charmeleon', ('Fire',) , '1' ],
        [ 'Charizard', ('Fire' , 'Flying') , '1' ],
        [ 'Squirtle', ('Water',) , '2' ],
        [ 'Wartortle', ('Water',) , '2' ],
        [ 'Blastoise', ('Water',) , '2' ],
        [ 'Caterpie', ('Bug',) , '3' ],
        [ 'Metapod', ('Bug',) , '3' ],
        [ 'Butterfree', ('Bug' , 'Flying') , '3' ],
        [ 'Weedle', ('Bug' , 'Poison') , '4' ],
        [ 'Kakuna', ('Bug' , 'Poison') , '4' ],
        [ 'Beedrill', ('Bug' , 'Poison') , '4' ],
        [ 'Pidgey', ('Normal' , 'Flying') , '5' ],
        [ 'Pidgeotto', ('Normal' , 'Flying') , '5' ],
        [ 'Pidgeot', ('Normal' , 'Flying') , '5' ],
        [ 'Rattata', ('Normal',) , '6' ],
        [ 'Raticate', ('Normal',) , '6' ],
        [ 'Spearow', ('Normal' , 'Flying') , '7' ],
        [ 'Fearow', ('Normal' , 'Flying') , '7' ],
        [ 'Ekans', ('Poison',) , '8' ],
        [ 'Arbok', ('Poison',) , '8' ],
        [ 'Pikachu', ('Electric',) , '9' ],
        [ 'Raichu', ('Electric',) , '9' ],
        [ 'Sandshrew', ('Ground',) , '10' ],
        [ 'Sandslash', ('Ground',) , '10' ],
        [ 'Nidoran Female', ('Poison',) , '11' ],
        [ 'Nidorina', ('Poison',) , '11' ],
        [ 'Nidoqueen', ('Poison' , 'Ground') , '11' ],
        [ 'Nidoran Male', ('Poison',) , '12' ],
        [ 'Nidorino', ('Poison',) , '12' ],
        [ 'Nidoking', ('Poison' , 'Ground') , '12' ],
        [ 'Clefairy', ('Fairy',) , '13' ],
        [ 'Clefable', ('Fairy',) , '13' ],
        [ 'Vulpix', ('Fire',) , '14' ],
        [ 'Ninetales', ('Fire',) , '14' ],
        [ 'Jigglypuff', ('Normal' , 'Fairy') , '15' ],
        [ 'Wigglytuff', ('Normal' , 'Fairy') , '15' ],
        [ 'Zubat', ('Poison' , 'Flying') , '16' ],
        [ 'Golbat', ('Poison' , 'Flying') , '16' ],
        [ 'Oddish', ('Grass' , 'Poison') , '17' ],
        [ 'Gloom', ('Grass' , 'Poison') , '17' ],
        [ 'Vileplume', ('Grass' , 'Poison') , '17' ],
        [ 'Paras', ('Bug' , 'Grass') , '18' ],
        [ 'Parasect', ('Bug' , 'Grass') , '18' ],
        [ 'Venonat', ('Bug' , 'Poison') , '19' ],
        [ 'Venomoth', ('Bug' , 'Poison') , '19' ],
        [ 'Diglett', ('Ground',) , '20' ],
        [ 'Dugtrio', ('Ground',) , '20' ],
        [ 'Meowth', ('Normal',) , '21' ],
        [ 'Persian', ('Normal',) , '21' ],
        [ 'Psyduck', ('Water',) , '22' ],
        [ 'Golduck', ('Water',) , '22' ],
        [ 'Mankey', ('Fighting',) , '23' ],
        [ 'Primeape', ('Fighting',) , '23' ],
        [ 'Growlithe', ('Fire',) , '24' ],
        [ 'Arcanine', ('Fire',) , '24' ],
        [ 'Poliwag', ('Water',) , '25' ],
        [ 'Poliwhirl', ('Water',) , '25' ],
        [ 'Poliwrath', ('Water' , 'Fighting') , '25' ],
        [ 'Abra', ('Psychic',) , '26' ],
        [ 'Kadabra', ('Psychic',) , '26' ],
        [ 'Alakazam', ('Psychic',) , '26' ],
        [ 'Machop', ('Fighting',) , '27' ],
        [ 'Machoke', ('Fighting',) , '27' ],
        [ 'Machamp', ('Fighting',) , '27' ],
        [ 'Bellsprout', ('Grass' , 'Poison') , '28' ],
        [ 'Weepinbell', ('Grass' , 'Poison') , '28' ],
        [ 'Victreebel', ('Grass' , 'Poison') , '28' ],
        [ 'Tentacool', ('Water' , 'Poison') , '29' ],
        [ 'Tentacruel', ('Water' , 'Poison') , '29' ],
        [ 'Geodude', ('Rock' , 'Ground') , '30' ],
        [ 'Graveler', ('Rock' , 'Ground') , '30' ],
        [ 'Golem', ('Rock' , 'Ground') , '30' ],
        [ 'Ponyta', ('Fire',) , '31' ],
        [ 'Rapidash', ('Fire',) , '31' ],
        [ 'Slowpoke', ('Water' , 'Psychic') , '32' ],
        [ 'Slowbro', ('Water' , 'Psychic') , '32' ],
        [ 'Magnemite', ('Electric' , 'Steel') , '33' ],
        [ 'Magneton', ('Electric' , 'Steel') , '33' ],
        [ "Farfetch'd ", ('Normal' , 'Flying') , '34' ],
        [ 'Doduo', ('Normal' , 'Flying') , '35' ],
        [ 'Dodrio', ('Normal' , 'Flying') , '35' ],
        [ 'Seel', ('Water',) , '36' ],
        [ 'Dewgong', ('Water' , 'Ice') , '36' ],
        [ 'Grimer', ('Poison',) , '37' ],
        [ 'Muk', ('Poison',) , '37' ],
        [ 'Shellder', ('Water',) , '38' ],
        [ 'Cloyster', ('Water' , 'Ice') , '38' ],
        [ 'Gastly', ('Ghost' , 'Poison') , '39' ],
        [ 'Haunter', ('Ghost' , 'Poison') , '39' ],
        [ 'Gengar', ('Ghost' , 'Poison') , '39' ],
        [ 'Onix', ('Rock' , 'Ground') , '40' ],
        [ 'Drowzee', ('Psychic',) , '41' ],
        [ 'Hypno', ('Psychic',) , '41' ],
        [ 'Krabby', ('Water',) , '42' ],
        [ 'Kingler', ('Water',) , '42' ],
        [ 'Voltorb', ('Electric',) , '43' ],
        [ 'Electrode', ('Electric',) , '43' ],
        [ 'Exeggcute', ('Grass' , 'Psychic') , '44' ],
        [ 'Exeggutor', ('Grass' , 'Psychic') , '44' ],
        [ 'Cubone', ('Ground',) , '45' ],
        [ 'Marowak', ('Ground',) , '45' ],
        [ 'Hitmonlee', ('Fighting',) , '46' ],
        [ 'Hitmonchan', ('Fighting',) , '47' ],
        [ 'Lickitung', ('Normal',) , '48' ],
        [ 'Koffing', ('Poison',) , '49' ],
        [ 'Weezing', ('Poison',) , '50' ],
        [ 'Rhyhorn', ('Ground' , 'Rock') , '51' ],
        [ 'Rhydon', ('Ground' , 'Rock') , '51' ],
        [ 'Chansey', ('Normal',) , '52' ],
        [ 'Tangela', ('Grass',) , '53' ],
        [ 'Kangaskhan', ('Normal',) , '54' ],
        [ 'Horsea', ('Water',) , '55' ],
        [ 'Seadra', ('Water',) , '55' ],
        [ 'Goldeen', ('Water',) , '56' ],
        [ 'Seaking', ('Water',) , '56' ],
        [ 'Staryu', ('Water',) , '57' ],
        [ 'Starmie', ('Water' , 'Psychic') , '57' ],
        [ 'Mr. Mime', ('Psychic', ) , '58' ],
        [ 'Scyther', ('Bug' , 'Flying') , '59' ],
        [ 'Jynx', ('Ice' , 'Psychic') , '60' ],
        [ 'Electabuzz', ('Electric',) , '61' ],
        [ 'Magmar', ('Fire',) , '62' ],
        [ 'Pinsir', ('Bug',) , '63' ],
        [ 'Tauros', ('Normal',) , '64' ],
        [ 'Magikarp', ('Water',) , '65' ],
        [ 'Gyarados', ('Water' , 'Flying') , '65' ],
        [ 'Lapras', ('Water' , 'Ice') , '66' ],
        [ 'Ditto', ('Normal',) , '67' ],
        [ 'Eevee', ('Normal',) , ('68',) ],
        [ 'Vaporeon', ('Water',) , ('68','0') ],
        [ 'Jolteon', ('Electric',) , ('68','1') ],
        [ 'Flareon', ('Fire',) , ('68','2') ],
        [ 'Porygon', ('Normal',) , '69' ],
        [ 'Omanyte', ('Rock' , 'Water') , '70' ],
        [ 'Omastar', ('Rock' , 'Water') , '70' ],
        [ 'Kabuto', ('Rock' , 'Water') , '71' ],
        [ 'Kabutops', ('Rock' , 'Water') , '71' ],
        [ 'Aerodactyl', ('Rock' , 'Flying') , '72' ],
        [ 'Snorlax', ('Normal',) , '73' ],
        [ 'Articuno', ('Ice' , 'Flying') , '74' ],
        [ 'Zapdos', ('Electric' , 'Flying') , '75' ],
        [ 'Moltres', ('Fire' , 'Flying') , '76' ],
        [ 'Dratini', ('Dragon',) , '77' ],
        [ 'Dragonair', ('Dragon',) , '77' ],
        [ 'Dragonite', ('Dragon' , 'Flying') , '77' ],
        [ 'Mewtwo', ('Psychic',) , '78' ],
        [ 'Mew', ('Psychic',) , '79' ],
        [ 'Missingno', ('Normal', 'Flying') , '80' ]
        ]

#evolution_set = 0: , evolution_position = 0:2, rarity = 0:3 (0:2 - lower number, more common; 3 - does not spawn)
#time = 0:3 (time quadrants in 6-hour blocks for spawning), evolution_caveat = some_requirement_for_evolution (moon_stone, int(level number), etc)
#attack = int(number), special_attack = int(number), defense = int(number), special_defense = int(number), health = int(number), speed = int(number)
#above ints will act as preliminary modifiers for power - current_level will be assigned in database

master_pokemon_dict = {
  'Bulbasaur': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 1, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Ivysaur': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 1, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Venusaur': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 1, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Charmander': {     'type1': "Fire", 'evolution_set': 2, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Charmeleon': {     'type1': "Fire", 'evolution_set': 2, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Charizard': {     'type1': "Fire", 'type2': "Flying", 'evolution_set': 2, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Squirtle': {     'type1': "Water", 'evolution_set': 3, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Wartortle': {     'type1': "Water", 'evolution_set': 3, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Blastoise': {     'type1': "Water", 'evolution_set': 3, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Caterpie': {     'type1': "Bug",  'evolution_set': 4, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Metapod': {     'type1': "Bug",  'evolution_set': 4, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Butterfree': {     'type1': "Bug", 'type2': "Flying", 'evolution_set': 4, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Weedle': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 5, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kakuna': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 5, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Beedrill': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 5, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Pidgey': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 6, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Pidgeotto': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 6, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Pidgeot': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 6, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Rattata': {     'type1': "Normal", 'evolution_set': 7, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Raticate': {     'type1': "Normal", 'evolution_set': 7, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Spearow': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 8, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Fearow': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 8, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Ekans': {     'type1': "Poison", 'evolution_set': 9, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Arbok': {     'type1': "Poison", 'evolution_set': 9, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Pikachu': {     'type1': "Electric", 'evolution_set': 10, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Raichu': {     'type1': "Electric", 'evolution_set': 10, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Sandshrew': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 11, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Sandslash': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 11, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidoran Female': {     'type1': "Poison", 'evolution_set': 12, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidorina': {     'type1': "Poison", 'evolution_set': 12, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidoqueen': {     'type1': "Poison", 'type2': "Ground", 'evolution_set': 12, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidoran Male': {     'type1': "Poison", 'evolution_set': 13, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidorino': {     'type1': "Poison", 'evolution_set': 13, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Nidoking': {     'type1': "Poison", 'type2': "Ground", 'evolution_set': 13, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Clefairy': {     'type1': "Fairy", 'evolution_set': 14, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Clefable': {     'type1': "Fairy", 'evolution_set': 14, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Vulpix': {     'type1': "Fire", 'evolution_set': 15, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Ninetales': {     'type1': "Fire", 'evolution_set': 15, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Jigglypuff': {     'type1': "Normal", 'type2': "Fairy", 'evolution_set': 16, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Wigglytuff': {     'type1': "Normal", 'type2': "Fairy", 'evolution_set': 16, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Zubat': {     'type1': "Poison", 'type2': "Flying", 'evolution_set': 17, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Golbat': {     'type1': "Poison", 'type2': "Flying", 'evolution_set': 17, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Oddish': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 18, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Gloom': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 18, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Vileplume': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 18, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Paras': {     'type1': "Bug", 'type2': "Grass", 'evolution_set': 19, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Parasect': {     'type1': "Bug", 'type2': "Grass", 'evolution_set': 19, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Venonat': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 20, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Venomoth': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 20, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Diglett': {     'type1': "Ground",'evolution_set': 21, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dugtrio': {     'type1': "Ground", 'evolution_set': 21, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Meowth': {     'type1': "Normal", 'evolution_set': 22, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Persian': {     'type1': "Normal", 'evolution_set': 22, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Psyduck': {     'type1': "Water", 'evolution_set': 23, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Golduck': {     'type1': "Water", 'evolution_set': 23, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Mankey': {     'type1': "Fighting", 'evolution_set': 24, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Primeape': {     'type1': "Fighting", 'evolution_set': 24, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Growlithe': {     'type1': "Fire", 'evolution_set': 25, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Arcanine': {     'type1': "Fire", 'evolution_set': 25, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Poliwag': {     'type1': "Water", 'evolution_set': 26, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Poliwhirl': {     'type1': "Water", 'evolution_set': 26, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Poliwrath': {     'type1': "Water", 'evolution_set': 26, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Abra': {     'type1': "Psychic", 'evolution_set': 27, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kadabra': {     'type1': "Psychic", 'evolution_set': 27, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Machop': {     'type1': "Fighting", 'evolution_set': 28, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Machoke': {     'type1': "Fighting", 'evolution_set': 28, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Machamp': {     'type1': "Fighting", 'evolution_set': 28, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Bellsprout': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 29, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Weepinbell': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 29, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Victreebel': {     'type1': "Grass", 'type2': "Poison", 'evolution_set': 29, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Tentacool': {     'type1': "Water", 'type2': "Poison", 'evolution_set': 30, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Tentacruel': {     'type1': "Water", 'type2': "Poison", 'evolution_set': 30, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Geodude': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 31, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Graveler': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 31, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Golem': {     'type1': "Bug", 'type2': "Poison", 'evolution_set': 31, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Ponyta': {     'type1': "Fire", 'evolution_set': 32, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Rapidash': {     'type1': "Fire", 'evolution_set': 32, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Slowpoke': {     'type1': "Water", 'type2': "Psychic", 'evolution_set': 33, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Slowbro': {     'type1': "Water", 'type2': "Psychic", 'evolution_set': 33, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Magnemite': {     'type1': "Electric", 'type2': "Steel", 'evolution_set': 34, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Magneton': {     'type1': "Electric", 'type2': "Steel", 'evolution_set': 34, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  "Farfetch'd": {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 35, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Doduo': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 35, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dodrio': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 36, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Seel': {     'type1': "Water", 'evolution_set': 37, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dewgong': {     'type1': "Water", 'evolution_set': 37, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Grimer': {     'type1': "Poison", 'evolution_set': 38, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Muk': {     'type1': "Poison", 'evolution_set': 38, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Shellder': {     'type1': "Water", 'evolution_set': 39, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Cloyster': {     'type1': "Water", 'type2': "Ice", 'evolution_set': 39, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Gastly': {     'type1': "Ghost", 'type2': "Poison", 'evolution_set': 40, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Haunter': {     'type1': "Ghost", 'type2': "Poison", 'evolution_set': 40, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Gengar': {     'type1': "Ghost", 'type2': "Poison", 'evolution_set': 40, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Onix': {     'type1': "Rock", 'type2': "Ground", 'evolution_set': 41, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Drowzee': {     'type1': "Psychic", 'evolution_set': 42, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Hypno': {     'type1': "Psychic", 'evolution_set': 42, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Krabby': {     'type1': "Water", 'evolution_set': 43, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kingler': {     'type1': "Water", 'evolution_set': 43, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Voltorb': {     'type1': "Electric", 'evolution_set': 44, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Electrode': {     'type1': "Electric", 'evolution_set': 44, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Exeggcute': {     'type1': "Grass", 'type2': "Psychic", 'evolution_set': 45, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Exeggcuter': {     'type1': "Grass", 'type2': "Psychic", 'evolution_set': 45, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Cubone': {     'type1': "Ground", 'evolution_set': 46, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Marowak': {     'type1': "Ground", 'evolution_set': 46, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Doduo': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 47, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dodrio': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 47, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Hitmonlee': {     'type1': "Fighting", 'evolution_set': 48, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Hitmonchan': {     'type1': "Fighting", 'evolution_set': 49, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Lickitung': {     'type1': "Normal", 'evolution_set': 50, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Koffing': {     'type1': "Poison", 'evolution_set': 51, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Weezing': {     'type1': "Poison", 'evolution_set': 51, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Rhyhorn': {     'type1': "Ground", 'evolution_set': 52, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Rhydon': {     'type1': "Ground", 'type2': "Rock", 'evolution_set': 52, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Chansey': {     'type1': "Normal", 'evolution_set': 53, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Tangela': {     'type1': "Grass", 'evolution_set': 54, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kangaskhan': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 55, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Horsea': {     'type1': "Water", 'evolution_set': 56, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Seadra': {     'type1': "Water", 'evolution_set': 56, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Goldeen': {     'type1': "Water", 'evolution_set': 57, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Seaking': {     'type1': "Water", 'evolution_set': 57, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Staryu': {     'type1': "Water", 'evolution_set': 58, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Starmie': {     'type1': "Water", 'evolution_set': 58, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Mr. Mime': {     'type1': "Psychic", 'type2': "Flying", 'evolution_set': 59, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Scyther': {     'type1': "Bug", 'type2': "Flying", 'evolution_set': 60, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Jynx': {     'type1': "Ice", 'type2': "Psychic", 'evolution_set': 61, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Electabuzz': {     'type1': "Electric", 'evolution_set': 62, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Magmar': {     'type1': "Fire", 'evolution_set': 63, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Pinsir': {     'type1': "Bug", 'type2': "Flying", 'evolution_set': 64, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Tauros': {     'type1': "Normal", 'evolution_set': 65, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Magikarp': {     'type1': "Water", 'evolution_set': 66, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Gyrados': {     'type1': "Water", 'type2': "Flying", 'evolution_set': 66, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Lapras': {     'type1': "Water", 'type2': "Ice", 'evolution_set': 67, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Ditto': {     'type1': "Normal", 'evolution_set': 68, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Eevee': {     'type1': "Normal", 'evolution_set': 69, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Vaporeon': {     'type1': "Water", 'evolution_set': 69, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Jolteon': {     'type1': "Electric", 'evolution_set': 69, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Flareon': {     'type1': "Fire", 'evolution_set': 69, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Porygon': {     'type1': "Normal", 'evolution_set': 70, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Omanyte': {     'type1': "Rock", 'type2': "Water", 'evolution_set': 71, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Omastar': {     'type1': "Rock", 'type2': "Water", 'evolution_set': 71, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kabuto': {     'type1': "Rock", 'type2': "Water", 'evolution_set': 72, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Kabutops': {     'type1': "Rock", 'type2': "Water", 'evolution_set': 72, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Aerodactyl': {     'type1': "Rock", 'type2': "Flying", 'evolution_set': 73, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Snorlax': {     'type1': "Normal", 'evolution_set': 74, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Articuno': {     'type1': "Rock", 'type2': "Flying", 'evolution_set': 75, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Zapdos': {     'type1': "Zapdos", 'type2': "Flying", 'evolution_set': 76, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Moltres': {     'type1': "Water", 'type2': "Flying", 'evolution_set': 77, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dratini': {     'type1': "Dragon", 'evolution_set': 78, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dragonair': {     'type1': "Dragon", 'evolution_set': 78, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Dragonite': {     'type1': "Dragon", 'type2': "Flying", 'evolution_set': 78, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Mewtwo': {     'type1': "Psychic", 'evolution_set': 79, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Mew': {     'type1': "Psychic", 'evolution_set': 80, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
  'Missingno': {     'type1': "Normal", 'type2': "Flying", 'evolution_set': 0, 'evolution_position': 0 , 'rarity': 3, 'time': 3, 'evolution_caveat': 'trade', 'attack': 40, 'special_attack': 20, 'defense': 10, 'special_defense': 5, 'health': 30, 'speed': 15},
                      }

def pokemon(args):
    
    usage = '!pokemon <action (battle/print/evolution)> <name ([if battle - now]/pokemon name)>'
    
    action = args[0]
    #name = args[1]
    
    print_dict = {}
    
    evolution_index = []
    
    pokemon_1_cat = []
    pokemon_2_cat = []
    
    pokemon_1_mod = []
    pokemon_2_mod = []

    evolution_cat = []
    
    multipliers = {'Normal': {
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


    # One-line for loop that runs through master_pokemon, searching only the first column    
    pocket_monster = [x[0] for x in master_pokemon]
    #One-line for loop that runs through master_pokemon, searching only the third column
    evolution_set = [k[2] for k in master_pokemon]
    
    # Grabs multiplier of pokemon based on name[type]

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

        pokemon_1 = random.choice (pocket_monster)
        pokemon_2 = random.choice (pocket_monster)
        
        # Establishes the two selected pokemon as a concatenation 
        versus = "It's " + pokemon_1 + " versus " + pokemon_2 + ", dude!"
        
        # Establishes the two selected pokemon to battle
        versus_list = [pokemon_1, pokemon_2]
        
        # Sets variable for winner between pokemon1 and pokemon2
        winner = random.choice(versus_list) + " Wins!"
        
        # Allows for random selection from each list
        random.shuffle(master_pokemon)
        random.shuffle(versus_list)

        for poke, mod, __ in master_pokemon:
            
            type_index = []
            
            if pokemon_1.lower() in poke.lower():
                type_index.append(mod)
                
                for index in type_index:
                    pass
                    #print "Type for 1 " + str(index)
                
                    if mod == index:
                        pokemon_1_cat.append(" ".join([poke, "is Pokemon 1" , "with type(s)" , str(mod).replace('(','').replace(')','').replace("'",'').replace(',','')]))
                        #print pokemon_1_cat[0]
                        #print pocket_monster
                        #print evolution_set
                        
#        for poke, mod, group in master_pokemon:
            
            if pokemon_2.lower() == poke.lower():
                
################I think this is the key to point to the dictionary
                type_index.append(mod)
                print type_index
                
                for index in type_index:
                    pass
                    #print "Type for 2 " + str(index)
                
                    if mod == index:
                        pokemon_2_cat.append(" ".join([poke, "is Pokemon 2" , "with type(s)" , str(mod).replace('(','').replace(')','').replace("'",'').replace(',','')]))                       
                        #print pokemon_2_cat[0]
        
        # Concatenates results of versus and winner, separated by a space
        return pokemon_1_cat[0] + ". " + pokemon_2_cat[0] + ". " + " ".join([versus, winner]) + " " + get_fighting_index()

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
        poke_master = globals.CURRENT_USER
        print poke_master
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