#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import globals
login = globals.mysql_credentials
con = mdb.connect(login[0], login[1], login[2], login[3])
from src.lib.queries.points_queries import *


###TODO: with con.cursor() as cur: 

def get_pokemon_id_from_name(pokemon_name):
    
    with con:
        cur = con.cursor()
        cur.execute("""SELECT pokemon.id FROM pokemon WHERE pokemon.name = %s""", [pokemon_name])
        
        pokemon_id = cur.fetchone()
        
        if pokemon_id is not None:
            return pokemon_id[0]
        else:
            return "Error"
            
def find_open_party_positions(username):    
    with con: 

        cur = con.cursor()
        cur.execute("SELECT position from userpokemon where username = %s order by position", [username])
        
        occupied_positions = cur.fetchall()
        simple_list = [x[0] for x in occupied_positions]
        possible_positions = [1,2,3,4,5,6]
        available_positions = list(set(possible_positions) - set(simple_list))
        
        return available_positions, occupied_positions

def insert_user_pokemon(username, caught_by, position, id, level, nickname, for_trade, for_sale):
    try:
        with con: 
    
            cur = con.cursor()
            cur.execute("""INSERT INTO userpokemon (username, caught_by, position, pokemon_id, level, nickname, for_trade, for_sale) VALUES (%s, %s, %s, %s, %s, (SELECT name FROM pokemon WHERE id = %s), 0, 0)""", [username, caught_by, position, id, level, id])
            cur.execute("""SELECT nickname FROM userpokemon WHERE username = %s AND position = %s""", [username, position])
            pokemon_caught = cur.fetchone()
        
            return str(pokemon_caught[0]) + ' was caught!'
    except:
        return "Party full. One empty slot in party needed."
    
def remove_user_pokemon(username,position):
    
    with con:
        cur = con.cursor()
        success = cur.execute("""DELETE FROM userpokemon WHERE username = %s AND position = %s""", [username, position])
        if (success):
            return "Released party member #" + str(position)
        else:
            return "Nothing to release!"
    

def get_user_party_info(username):
    #broken
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT userpokemon.position, userpokemon.level, userpokemon.nickname
        FROM userpokemon WHERE username = %s ORDER BY userpokemon.position;""", [username])
        
        
        party_members = cur.fetchall()
        
        if party_members != None:
            return party_members
        else:
            return "No Pokemon found. Tell them to use !catch"

def user_pokemon_types_summary(username, position):
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT userpokemon.nickname as 'Nickname',
        type_primary.id as 'ID 1', type_secondary.id as 'ID 2',
        pokemon.name as 'Name', type_primary.identifier as 'Type 1',
        type_secondary.identifier as 'Type 2'
        from userpokemon inner join pokemon on pokemon.id = userpokemon.pokemon_id inner
        join types as type_primary on ( type_primary.id = pokemon.type_primary )
        left outer join types as type_secondary on ( type_secondary.id = pokemon.type_secondary )
        where username = %s and userpokemon.position = %s""", [username,position])
    
        types_summary = cur.fetchone()
        print types_summary
        nickname = types_summary[0]
        pokemon_type1_id = types_summary[1]
        pokemon_type2_id = types_summary[2]
        pokemon_name = types_summary[3]
        pokemon_type1 = types_summary[4]
        if types_summary[2] and types_summary[5] is not None:
            pokemon_type2 = types_summary[5]
            return nickname, pokemon_type1_id, pokemon_type2_id, pokemon_name, pokemon_type1, pokemon_type2
        else:
            pokemon_type2 = "No secondary type."
            return nickname, pokemon_type1_id, 'none', pokemon_name, pokemon_type1, 'none'

def level_up_user_pokemon(username, position):
    with con: 

        cur = con.cursor()
        cur.execute("""update userpokemon set level = level + 1
        where username = %s and position = %s
        """, [username, position])
        
def get_last_battle(username):
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT lastbattle from users WHERE username = %s""", [username])
        last_battle = cur.fetchone()
        
        return last_battle[0]
    
def set_battle_timestamp(username, datetime):
    with con: 

        cur = con.cursor()
        cur.execute("""UPDATE users SET lastbattle = %s WHERE username = %s""", [datetime, username])
        last_battle = cur.fetchone()
                
def get_battle_stats(username, position):
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT username,
        userpokemon.nickname as 'Nickname',
        userpokemon.level as 'Level',
        pokemon.name as 'Name',
        type_primary as 'Type 1',
        type_secondary as 'Type 2',
        ((2*pokemon.hp_base)/100*userpokemon.level)+110 as 'Health Points',
        ((2*pokemon.speed_base)/100*userpokemon.level)+5 as 'Speed',
        ((2*pokemon.attack_base)/100*userpokemon.level)+5 as 'Attack',
        ((2*pokemon.defense_base)/100*userpokemon.level)+5 as 'Defense',
        ((2*pokemon.special_attack_base)/100*userpokemon.level)+5 as 'Special',
        ((2*pokemon.special_defense_base)/100*userpokemon.level)+5 as 'Special Defense'
        from userpokemon
        inner join pokemon on pokemon.id = userpokemon.pokemon_id
        where username = %s and userpokemon.position = %s""", [username, position])
        
        battle_stats = cur.fetchone()
        print battle_stats
        
        nickname = battle_stats[1]
        level = battle_stats[2]
        hp = int(round(battle_stats[6]))
        speed = int(round(battle_stats[7]))
        attack = int(round(battle_stats[8]))
        defense = int(round(battle_stats[9]))
        special_attack = int(round(battle_stats[10]))
        special_defense = int(round(battle_stats[11]))
        
        return level, nickname, hp, speed, attack, defense, special_attack, special_defense

def broken_get_damage_multiplier(attacking_type, defending_type):
    with con: 

        cur = con.cursor()
        cur.execute("SET @attacking_type = %s", [attacking_type])
        cur.execute("SET @defending_type = %s", [defending_type])
        cur.execute("""SET @query = CONCAT('SELECT ',@table,'.',@defending_type,'
        as "Damage Multiplier" FROM types WHERE id = ', @attacking_type)""")
        cur.execute("PREPARE stmt FROM @query")
        cur.execute("EXECUTE stmt")
        
        damage_multiplier = cur.fetchone()
        
        return damage_multiplier
    
def get_attacker_multiplier(attacker_type, defender_type):
    with con: 
        cur = con.cursor()
        cur.execute("""SELECT * from types WHERE id = %s""", [attacker_type])
        attacker_multipliers = cur.fetchone()
        row_correction = defender_type + 1
    
        attacker_effect = attacker_multipliers[row_correction]
        return attacker_effect
    
def get_defender_multiplier(attacker_type, defender_type):
    with con: 
        cur = con.cursor()
        cur.execute("""SELECT * from types WHERE id = %s""", [defender_type])
        defender_multipliers = cur.fetchone()
        row_correction = attacker_type + 1
        
        defender_effect = defender_multipliers[row_correction]
        return defender_effect
    
is_tradeable = 1
asking_pokemon_id = 150
minimum_level = 10
party_position = 1

def get_pokemon_id(username, position):
    with con: 
    
        cur = con.cursor()
        cur.execute("""SELECT userpokemon.pokemon_id WHERE username = %s and position = %s
        """, [username, position])
        
        pokemon_id = cur.fetchone()
        return pokemon_id

def reset_trade_timestamp(time):
        with con: 

            cur = con.cursor()
            cur.execute("""UPDATE userpokemon SET for_trade = 0, time_trade_set = NULL WHERE time_trade_set < %s
            """, [time])
        
def set_pokemon_trade_status(time, asking_pokemon_id, minimum_level, username, party_position):
    with con: 

        cur = con.cursor()
        cur.execute("""UPDATE userpokemon SET time_trade_set = %s, for_trade = 1, asking_trade = %s, asking_level = %s
        WHERE username = %s AND position = %s
        """, [time, asking_pokemon_id, minimum_level, username, party_position])

def get_receiver_trade_status(position, receiver):
    with con: 

        cur = con.cursor()
        cur.execute("""
        SELECT pokemon_id, level FROM userpokemon WHERE username = %s AND position = %s
        """, [receiver, position])
        
        trader_party = cur.fetchall()
        return trader_party

def get_giver_trade_status(position, giver):
    with con: 

        cur = con.cursor()
        cur.execute("""
        SELECT asking_trade, asking_level FROM userpokemon WHERE username = %s AND position = %s
        """, [giver, position])
        
        trader_party = cur.fetchall()
        return trader_party
        
def show_all_tradable_pokemon():
    with con: 

        cur = con.cursor()
        cur.execute("""select
        userpokemon.username,
        owner_pokemon.name,
        userpokemon.position,
        asking_for.name,
        asking_level
        from userpokemon
        inner join pokemon as owner_pokemon on owner_pokemon.id = userpokemon.pokemon_id
        left outer join pokemon as asking_for on asking_for.id = userpokemon.asking_trade
        where for_trade = 1
        """)
        
        trades = cur.fetchall()
        for trade in trades:
            print trade
            
        return trades
            
def show_user_tradable_pokemon(username):
    with con: 

        cur = con.cursor()
        cur.execute("""select
        userpokemon.username,
        owner_pokemon.name,
        userpokemon.position,
        asking_for.name,
        asking_level
        from userpokemon
        inner join pokemon as owner_pokemon on owner_pokemon.id = userpokemon.pokemon_id
        left outer join pokemon as asking_for on asking_for.id = userpokemon.asking_trade
        where for_trade = 1 and username = %s
        """, [username])
        
        trades = cur.fetchall()
        print trades
        return trades

def add_win(username):
    with con:
        
        cur = con.cursor()
        cur.execute("""UPDATE users SET wins = wins + 1 WHERE username = %s
        """, [username])
        
def add_loss(username):
    with con:
        
        cur = con.cursor()
        cur.execute("""UPDATE users SET losses = losses + 1 WHERE username = %s
        """, [username])

def trade_transaction(giver, giver_position, receiver, receiver_position):
#will test this under supervision
    with con: 

        cur = con.cursor()
        cur.execute("""UPDATE userpokemon SET username = %s, for_trade = 2, position = 0
        WHERE username = %s AND position = %s""", [receiver, giver, giver_position])
        cur.execute("""UPDATE userpokemon SET username = %s, for_trade = 2, position = %s
        WHERE username = %s AND position = %s""", [giver, giver_position, receiver, receiver_position])
        cur.execute("""UPDATE userpokemon SET position = %s, for_trade = 2
        WHERE position = 0""", [receiver_position])
        cur.execute("""UPDATE userpokemon SET time_trade_set = NULL WHERE username = %s AND position = %s
        """, [receiver, receiver_position])
        #cur.execute("""UPDATE userpokemon SET time_trade_set = NULL WHERE username = %s AND position = %s
        #""", [giver, giver_position])

def show_all_pokemon_for_sale():
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT userpokemon.username AS 'Owner', pokemon.name, userpokemon.asking_price
        FROM userpokemon
        INNER JOIN pokemon ON pokemon.id = userpokemon.pokemon_id
        WHERE for_sale = 1;""")

def show_user_pokemon_for_sale():
    with con:
        
        cur = con.cursor()
        cur.execute("""SELECT userpokemon.username, pokemon.name, userpokemon.position
        FROM userpokemon
        INNER JOIN pokemon ON pokemon.id = userpokemon.pokemon_id
        WHERE for_sale = 1 AND username = %s""", [globals.CURRENT_USER])
        
def check_for_pokemon_for_sale():
    pokemon_query = "Mewtwo"
    with con:
        
        cur = con.cursor()
        cur.execute("""SELECT userpokemon.username, pokemon.name, userpokemon.asking_price
        FROM pokemon
        LEFT JOIN userpokemon on userpokemon.pokemon_id = pokemon.id
        WHERE for_sale = 1 and pokemon.name = %s""", [pokemon_query])
        
def set_pokemon_as_for_sale():
    for_sale = 1
    asking_price = 5000
    with con:
        
        cur = con.cursor()
        cur.execute("""update userpokemon
        set for_sale = %s, asking_price = %s
        where username = %s and position = %s""", [for_sale, asking_price, globals.CURRENT_USER, party_position])
        
def update_asking_price():
    asking_price = 4000
    with con:
        
        cur = con.cursor()
        cur.execute("""update userpokemon
        set asking_price = %s
        where username = %s and position = %s""", [asking_price, globals.CURRENT_USER, party_position])
        
def sell_transaction():
    seller = 'lorenzotherobot'
    buyer = globals.CURRENT_USER
    open_position = 5
    with con:
        
        cur = con.cursor()
        cur.execute("""set @seller = %s""", [seller])
        cur.execute("""@position = %s""", [party_position])
        cur.execute("""set @buyer = %s""", [buyer])
        cur.execute("""set @position_free = %s""", [open_position])
        cur.execute("""set @price = (select asking_price from userpokemon where username = @owner and position = @position)""")
        cur.execute("""update userpokemon set username = @buyer, for_sale = 0, position = @position_free
        where username = @seller and position = @position""")
        cur.execute("""update users set points = points + @price
        where username = @seller""")
        cur.execute("""update users set points = points - @price
        where username = @buyer""")
        cur.execute("""COMMIT""")
        
def spawn_tallgrass(rarity_index):
    with con:
        
        cur = con.cursor()
        cur.execute("""SELECT name FROM pokemon WHERE rarity = %s AND evolution_trigger = 0 AND id != 244 ORDER BY rand() limit 1""", [rarity_index]) #Intentionally excludes Entei
        rare_pokemon = cur.fetchone()
        
        return rare_pokemon[0]
    
def check_evolution_eligibility(username, position):
    with con:
        
        cur = con.cursor()
        cur.execute("""SELECT userpokemon.nickname, pokemon.name, pokeset.name, pokeset.id FROM userpokemon
        JOIN pokemon on userpokemon.pokemon_id = pokemon.id
        JOIN pokemon as pokeset on pokemon.evolution_set = pokeset.evolution_set
        WHERE userpokemon.level >= pokemon.evolution_level AND pokeset.id > userpokemon.pokemon_id
        AND userpokemon.username = %s AND userpokemon.position = %s LIMIT 1
        """, [username, position])
        
        eligible_evolution = cur.fetchone()
        return eligible_evolution
    
        #| nickname  | name      | name    | id |
        #| Bulbasaur | Bulbasaur | Ivysaur |  2 |

def apply_evolution(username, position):
    evolution_result = check_evolution_eligibility(username, position)
    nickname = evolution_result[0]
    id = evolution_result[3]
    
    if evolution_result is not None:
    
        if nickname == evolution_result[1]:
            nickname = evolution_result[2]
        
        with con:
            
            cur = con.cursor()
            cur.execute("""UPDATE userpokemon SET pokemon_id = %s, nickname = %s WHERE username = %s AND position = %s
            """, [id, nickname, username, position])
            
            return nickname + " has evolved! Raise your Kappa s!!!" 
    else:
        return "No Pokemon eligible for evolution."

def update_nickname(nickname, username, position):
    
    # todo - error message on no entry
    with con:
        
        cur = con.cursor()
        cur.execute("""UPDATE userpokemon SET nickname = %s WHERE username = %s
        AND position = %s""", [nickname, username, position])

def check_items():
    
    with con:
        cur = con.cursor()
        cur.execute("""SELECT id, name, value FROM items WHERE id IN (1,2,3,4,5,11,12,13,14)""")
        for_sale = cur.fetchall()
        
        return for_sale

def get_item_value(id):
    
    with con:
        cur = con.cursor()
        cur.execute("""SELECT value FROM items WHERE id = %s""", [id])
        value = cur.fetchone()
        
        return value[0]

def check_inventory(username):
    
    with con:
        cur = con.cursor()
        cur.execute("""SELECT items.id, items.name, useritems.quantity
        FROM useritems
        INNER JOIN items ON items.id = useritems.item_id
        WHERE username = %s""", [username])
        inventory = cur.fetchall()
        
        return inventory

def buy_items(id, username):
    try:
        if int(id) in (1,2,3,4,5,11,12,13,14):
            print "ID FOUND TO MATCH ITEMS AVAILABLE"
            points = int(get_user_points(username))
            value = int(get_item_value(id))
            print value
            print type(value)
            if points >= value:
                print "POINTS ARE HIGHER THAN ITEM VALUE"
                with con:
                    cur = con.cursor()
                    cur.execute("""INSERT INTO useritems (username, item_id, quantity) VALUES (%s, %s, 1) ON
                    DUPLICATE KEY UPDATE quantity = quantity + 1""", [username, id])
                    cur.execute("""UPDATE users SET points = points - %s WHERE username = %s""", [value,username])
                    
                    return "Transaction successful."
            else:
                return "You need more points for that!"
        else:
            return "That is not a valid item position."
    except:
        return "Item ID must be a number"



def use_item(username, item, position):
    try:
        if int(item) == 11:
            item_in_stock = False
            inventory = check_inventory(username)
            for id, __, __ in inventory:
                if int(id) == int(item):
                    item_in_stock = True
            if item_in_stock == True: 
                cur = con.cursor()
                cur.execute("""UPDATE userpokemon SET level = level + 10
                WHERE username = %s AND position = %s
                """, [username, position])
                cur = con.cursor()
                cur.execute("""UPDATE userpokemon SET level = 100
                WHERE username = %s AND position = %s AND level > 100
                """, [username, position])
                cur.execute("""UPDATE useritems SET quantity = quantity - 1 WHERE username = %s AND item_id = %s
                        """, [username, item])
                cur.execute("""DELETE FROM useritems WHERE username = %s AND quantity <= 0""", [username])
                return "Level up!!!"
            else:
                return "You don't have any more!"
            
        else:
            
            def check_special_evolution_eligibility(username, position, item):
    
                with con:
                    
                    cur = con.cursor()
                    cur.execute("""SELECT userpokemon.nickname, pokemon.name, pokeset.name, pokeset.id, pokeset.evolution_set, pokeset.evolution_index, pokeset.evolution_trigger
                    FROM userpokemon
                    JOIN pokemon on userpokemon.pokemon_id = pokemon.id
                    JOIN pokemon as pokeset on pokemon.evolution_set = pokeset.evolution_set
                    WHERE userpokemon.username = %s AND userpokemon.position = %s AND pokeset.evolution_index = pokemon.evolution_index + 1
                    AND pokeset.evolution_trigger = %s
                    """, [username, position, item])
                    
                    #+----------+-------+----------+-----+---------------+-----------------+-------------------+
                    #| nickname | name  | name     | id  | evolution_set | evolution_index | evolution_trigger |
                    #+----------+-------+----------+-----+---------------+-----------------+-------------------+
                    #| Eevee    | Eevee | Vaporeon | 134 |            51 |               2 |                 2 |
                    #+----------+-------+----------+-----+---------------+-----------------+-------------------+
                                                
                    eligible_evolution = cur.fetchone()
                    return eligible_evolution
            
            evolution_result = check_special_evolution_eligibility(username, position, item)
            nickname = evolution_result[0]
            id = evolution_result[3]
            evolution_set = evolution_result[4]
            evolution_index = evolution_result[5]
            evolution_trigger = evolution_result[6]
            
            if evolution_result is not None:
            
                if nickname == evolution_result[1]:
                    nickname = evolution_result[2]
                
                with con:
                    
                    cur = con.cursor()
                    cur.execute("""UPDATE useritems SET quantity = quantity - 1 WHERE username = %s AND item_id = %s
                    """, [username, item])
                    cur.execute("""UPDATE userpokemon SET pokemon_id = %s, nickname = %s WHERE username = %s AND position = %s
                    """, [id, nickname, username, position])
                    cur.execute("""DELETE FROM useritems WHERE username = %s AND quantity <= 0""", [username])
                    
                    return nickname + " has evolved! Raise your Kappa s!!!" 
            else:
                return "No Pokemon eligible for evolution."
    
    except:
        return "Item being selected must be a number"
    
    
