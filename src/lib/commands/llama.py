import sqlite3
import sys
import re
import socket
import pexpect
import time
import os
import src.lib.user_data as user_data
import os
import urllib2
import ast

"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""
def database_entry():
    #create/connect to user database
    db = sqlite3.connect('/home/shane/git/lorenzotherobot/src/lib/userdata.db')
    
    #get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(name TEXT PRIMARY KEY,
                        pokemon TEXT, treats TEXT, ul TEXT)
     ''')
    for p in user_data.user_data_points:
        format_str = """INSERT INTO users (name, pokemon, treats, ul)
        VALUES ("{name}", "{pokemon}", "{treats}", "{ul}" );"""
        sql_command = format_str.format(name=p[0], pokemon=p[1], treats=p[2], ul=p[3])
        cursor.execute(sql_command)
    cursor.execute("SELECT * FROM users")
    #prints all entires
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

"""Gets list of users and returns them to the chat"""

def llama():
    response = urllib2.urlopen('https://tmi.twitch.tv/group/user/lorenzotherobot/chatters')#change username to your channel
    user_dict = ast.literal_eval(response.read())
    return str("Viewers: " + ", ".join(user_dict["chatters"]["moderators"]) + ", " + ", ".join(user_dict["chatters"]["viewers"]))