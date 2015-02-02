import sqlite3
import sys
import re
import socket

import src.lib.user_data as user_data

def llama():
    #allocate memory for operations
    db = sqlite3.connect(':memory:')
    #create/connect to user database
    db = sqlite3.connect('/home/shane/git/lorenzotherobot/src/lib/userdata.db')

    # Get a cursor object
    cursor = db.cursor()
    
#####Delete the below lines if first time running
 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(name TEXT PRIMARY KEY,
                       pokemon TEXT, treats TEXT, ul TEXT)
    ''')
    
    for p in user_data.user_data_points:
        format_str = """INSERT INTO users (name, pokemon, treats, ul)
        VALUES ("{name}", "{pokemon}", "{treats}", "{ul}" );"""
    
        sql_command = format_str.format(name=p[0], pokemon=p[1], treats = p[2], ul = p[3])
        cursor.execute(sql_command)
   
    cursor.execute("SELECT * FROM users")
    
    #prints all entries 
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    cursor.execute("SELECT * FROM users") 
    #prints one entry
    print("\nfetch one:")
    res = cursor.fetchone()
     
    print(res)
    db.close()