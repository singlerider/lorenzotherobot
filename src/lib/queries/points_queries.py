#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import globals
from src.lib.twitch import *
login = globals.mysql_credentials
con = mdb.connect(login[0], login[1], login[2], login[3])

user_dict, user_list = get_dict_for_users()

def mysql_version():
    #When this was run, it prevented other things from working.
    #It worked on its own, though. I removed the code stuffs from it.
    pass

def mysql_ping():
    with con:
        
        con.ping()
        print "pinging database"

def get_points_list():
    with con: 

        cur = con.cursor()
        cur.execute("""SELECT username, points FROM users ORDER BY points * 1 DESC""")
        user_data = cur.fetchall()
        return str(user_data[0:9])
            
def get_user_points(username):
    with con: 

        cur = con.cursor()
        cur.execute("select points from users where username = %s", [username])
    
        points = cur.fetchone()
        return points[0]

def set_user_points(delta_user, delta):
    with con: 

        cur = con.cursor()
        cur.execute("update users set points = %s where username = %s", [delta, delta_user])
        
def modify_user_points(delta_user, delta):
# update integer variable path to interact with delta_treats(400)
    with con: 

        cur = con.cursor()
        cur.execute("""INSERT INTO users (username, points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE points = points + %s""", [delta_user,delta,delta])
    
def modify_points_all_users(points_to_increment = 1):
    user_list_for_query = [(x,points_to_increment) for x in user_list]
    try:
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO users (username, points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE points = points + " + str(points_to_increment), user_list_for_query)
            
            con.commit()
            #print "DEBUG (last executed): " + cur._last_executed
            return "success"

    except Exception, error:
        print "ERROR", error
        return "Error incrementing points:" + str(error)
