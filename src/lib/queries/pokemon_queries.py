#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import globals
login = globals.mysql_credentials
con = mdb.connect(login[0], login[1], login[2], login[3])

def mysql_version():
    #When this was run, it prevented other things from working.
    #It worked on its own, though. I removed the code stuffs from it.
    pass
            
def get_user_points():
    with con: 

        cur = con.cursor()
        cur.execute("select points from users where username = %s", [globals.CURRENT_USER])
    
        points = cur.fetchone()
        return points[0]

def set_user_points():
# update integer variable path to interact with delta_treats(400)
    with con: 

        cur = con.cursor()
        cur.execute("update users set points = %s where username = %s", [400, globals.CURRENT_USER])

def increment_user_points():
# update integer variable path to interact with delta_treats(400)
    with con: 

        cur = con.cursor()
        cur.execute("update users set points = points + %s where username = %s", [-3, globals.CURRENT_USER])
        
def add_points_all_users():
    username_list = ['curvyllama', 'singlerider']
    for user in username_list:
        
        with con: 
    
            cur = con.cursor()
            cur.execute("update users set points = points + %s where username = %s", [1, user])
            
def find_open_party_positions():    
    with con: 

        cur = con.cursor()
        cur.execute("SELECT position from userpokemon where username = %s order by position", [globals.CURRENT_USER])
        
        occupied_positions = cur.fetchone()
        possible_positions = [1,2,3,4,5,6]
        available_positions = list(set(possible_positions) - set(occupied_positions))
        
        return available_positions

def insert_user_pokemon():
    pokemon_id = 25
    pokemon_level = 1
    open_position = 6
    try:
        with con: 
    
            cur = con.cursor()
            cur.execute("""insert into userpokemon (username, caught_by, position, pokemon_id, level, nickname, for_trade, for_sale) values (%s, %s, %s, %s, %s, (SELECT name from pokemon where id = %s), 0, 0)""", [globals.CURRENT_USER,globals.CURRENT_USER,open_position,pokemon_id,pokemon_level,pokemon_id])
            cur.execute("""select nickname from userpokemon where username = %s and position = %s""", [globals.CURRENT_USER, open_position])
            pokemon_caught = cur.fetchone()
        
            return str(pokemon_caught[0]) + ' successfuly added!'
    except:
        return "Party full. One empty slot in party needed."
    
def remove_user_pokemon():
    position = 6
    
    with con:
        cur = con.cursor()
        success = cur.execute("""delete from userpokemon where username = 'singlerider' and position = 6""")
        if (success):
            return "Released party member #" + str(position)
        else:
            return "Nothing to release!"
    

def get_user_party_info():
    with con: 

        cur = con.cursor()
        cur.execute("""select userpokemon.position, userpokemon.nickname from userpokemon
        where username = 'singlerider'
        order by userpokemon.position""")
        
        party_members = cur.fetchall()
        return party_members

def user_pokemon_types_summary():
    with con: 

        cur = con.cursor()
        cur.execute("SELECT userpokemon.nickname as 'Nickname', pokemon.name as 'Name', type_primary.identifier as 'Type 1', type_secondary.identifier as 'Type 2' from userpokemon inner join pokemon on pokemon.id = userpokemon.pokemon_id inner join types as type_primary on ( type_primary.id = pokemon.type_primary ) left outer join types as type_secondary on ( type_secondary.id = pokemon.type_secondary ) where username = %s and userpokemon.position = 1;", [globals.CURRENT_USER])
    
        types_summary = cur.fetchone()
        user_pokemon_nickname = types_summary[0]
        pokemon_name = types_summary[1]
        pokemon_type1 = types_summary[2]
        if types_summary[3] is not None:
            pokemon_type2 = types_summary[3]
        else:
            pokemon_type2 = "No secondary type."
        
        return 'Nickname: ' + user_pokemon_nickname + ', Pokemon: ' + pokemon_name + ', Types: ' + pokemon_type1 + ', ' + pokemon_type2

def level_up_user_pokemon():
    pokemon_position = 1
    with con: 

        cur = con.cursor()
        cur.execute("""update userpokemon set level = level + 1
        where username = %s and position = %s
        """, [globals.CURRENT_USER, pokemon_position])
        
def get_battle_stats():
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
    where username = %s and userpokemon.position = 1""", [globals.CURRENT_USER])
        
        battle_stats = cur.fetchone()
        
        nickname = battle_stats[1]
        hp = battle_stats[6]
        speed = battle_stats[7]
        attack = battle_stats[8]
        defense = battle_stats[9]
        special_attack = battle_stats[10]
        special_defense = battle_stats[11]
        
        return nickname + "'s battle stats - HP: " + str(hp) + ", Speed: " + str(speed) + ", Attack: " + str(attack) + ", Defense: " + str(defense) + ", Special Atack: " + str(special_attack) + ", Special Defense: " + str(special_defense)

def get_damage_multiplier():
#I'm afraid to even touch this one
    with con: 

        cur = con.cursor()
        cur.execute("SET @attacking_type = 15")
        cur.execute("SET @defending_type = 12")
        cur.execute("""SET @query = CONCAT('SELECT ',@table,'.',@defending_type,' as "Damage Multiplier" FROM types WHERE id = ', @attacking_type)""")
        cur.execute("PREPARE stmt FROM @query")
        cur.execute("EXECUTE stmt")

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
        cur.execute("""start transaction""")
        cur.execute("""set @player_1 = 'singlerider'""")
        cur.execute("""set @position_1 = 3""")
        cur.execute("""set @player_2 = 'lorenzotherobot'""")
        cur.execute("""set @position_2 = 1""")
        cur.execute("""update userpokemon set username = @player_1, for_trade = 0, position = 0
        where username = @player_2 and position = @position_2""")
        cur.execute("""update userpokemon set username = @player_2, for_trade = 0, position = @position_2
        where username = @player_1 and position = @position_1""")
        cur.execute("""update userpokemon set position = @position_1
        where position = 0""")
        cur.execute("""COMMIT""")

def show_all_pokemon_for_sale():
    with con: 

        cur = con.cursor()
        cur.execute("""select userpokemon.username as 'Owner', pokemon.name, userpokemon.asking_price
        from userpokemon
        inner join pokemon on pokemon.id = userpokemon.pokemon_id
        where for_sale = 1;""")

def show_user_pokemon_for_sale():
    with con:
        
        cur = con.cursor()
        cur.execute("""select userpokemon.username, pokemon.name, userpokemon.position
        from userpokemon
        inner join pokemon on pokemon.id = userpokemon.pokemon_id
        where for_sale = 1 and username = %s""", [globals.CURRENT_USER])
        
def check_for_pokemon_for_sale():
    pokemon_query = "Mewtwo"
    with con:
        
        cur = con.cursor()
        cur.execute("""select userpokemon.username, pokemon.name, userpokemon.asking_price
        from pokemon
        left join userpokemon on userpokemon.pokemon_id = pokemon.id
        where for_sale = 1 and pokemon.name = %s""", [pokemon_query])
        
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