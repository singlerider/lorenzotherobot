#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import globals
login = globals.mysql_credentials
con = mdb.connect(login[0], login[1], login[2], login[3])

def get_pokemon_id_from_name(pokemon_name):
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT pokemon.id FROM pokemon WHERE pokemon.name = %s""", [pokemon_name])
        
        pokemon_id = cur.fetchone()
        
        return pokemon_id[0]
            
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
        
            return str(pokemon_caught[0]) + ' successfuly added!'
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
        cur.execute("""select userpokemon.position, userpokemon.nickname from userpokemon
        where username = %s
        order by userpokemon.position""", [username])
        
        simplified_party_members = []
        
        party_members = cur.fetchall()
        for item in party_members:
            for member in item:
                simplified_party_members.append(member)
        
        return simplified_party_members

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
        
def set_pokemon_trade_status():
    with con: 

        cur = con.cursor()
        cur.execute("""update userpokemon
        set for_trade = %s,
        asking_trade = %s,
        asking_level = %s
        where username = %s and position = %s
        """, [is_tradeable, asking_pokemon_id, minimum_level, globals.CURRENT_USER, party_position])

def mark_pokemon_trade_status():
    with con: 

        cur = con.cursor()
        cur.execute("""update userpokemon
        set for_trade = %s,
        asking_trade = (select id from pokemon where name = 'Charmander'),
        asking_level = %s
        where username = %s and position = %s
        """, [is_tradeable, minimum_level, globals.CURRENT_USER, party_position])
        
def show_all_tradeable_pokemon():
    with con: 

        cur = con.cursor()
        cur.execute("""select
        userpokemon.username as 'Owner',
        owner_pokemon.name as 'Pokemon',
        userpokemon.position as 'Position',
        asking_for.name as 'Trading for',
        asking_level as 'Minimum level'
        from userpokemon
        inner join pokemon as owner_pokemon on owner_pokemon.id = userpokemon.pokemon_id
        left outer join pokemon as asking_for on asking_for.id = userpokemon.asking_trade
        where for_trade = 1
        """)
        
        trades = cur.fetchall()
        for trade in trades:
            print trade
            
def show_user_tradeable_pokemon():
    with con: 

        cur = con.cursor()
        cur.execute("""select
        userpokemon.username as 'Owner',
        owner_pokemon.name as 'Pokemon',
        userpokemon.position as 'Position',
        asking_for.name as 'Trading for',
        asking_level as 'Minimum level'
        from userpokemon
        inner join pokemon as owner_pokemon on owner_pokemon.id = userpokemon.pokemon_id
        left outer join pokemon as asking_for on asking_for.id = userpokemon.asking_trade
        where for_trade = 1 and username = %s
        """, [globals.CURRENT_USER])
        
        trades = cur.fetchall()
        for trade in trades:
            print trade

def trade_transaction():
#will test this under supervision
    with con: 

        cur = con.cursor()
        cur.execute("""START transaction""")
        cur.execute("""SET @player_1 = 'singlerider'""")
        cur.execute("""SET @position_1 = 3""")
        cur.execute("""SET @player_2 = 'lorenzotherobot'""")
        cur.execute("""SET @position_2 = 1""")
        cur.execute("""UPDATE userpokemon SET username = @player_1, for_trade = 0, position = 0
        WHERE username = @player_2 AND position = @position_2""")
        cur.execute("""UPDATE userpokemon SET username = @player_2, for_trade = 0, position = @position_2
        WHERE username = @player_1 AND position = @position_1""")
        cur.execute("""UPDATE userpokemon SET position = @position_1
        WHERE position = 0""")
        cur.execute("""COMMIT""")

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
