#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import globals
from src.lib.twitch import *
login = globals.mysql_credentials
con = mdb.connect(login[0], login[1], login[2], login[3])

user_dict, all_users = get_dict_for_users()

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
        try:
            points = cur.fetchone()
            if points[0] > 0:
                return points[0]
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except:
            return "User not found. Check your spelling."

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
    print all_users
    user_list_for_query = [(x,points_to_increment) for x in all_users]
    print user_list_for_query
    length = len(user_list_for_query) - 1
    
    try:
        with con:
            cur = con.cursor()
            
            dData = user_list_for_query  # exact input you gave

            sql = """
            INSERT INTO users
              (username, points)
            VALUES
              (%s, %s)
            ON DUPLICATE KEY UPDATE
              points = points + """ + str(points_to_increment)
            # keep parameters in one part of the statement
            
            # generator expression takes care of the repeated values
            cur.executemany(sql, ((user, points) for user, points in dData) )
            
            #cur.executemany("INSERT INTO users (username, points) VALUES (%s, 1) ON DUPLICATE KEY UPDATE points = points + 1", (user_list_for_query) )
                
            #con.commit()
            #print "DEBUG (last executed): " + cur._last_executed
            return "success"

    except Exception, error:
        print "ERROR", error
        return "Error incrementing points:" + str(error)
    
def modify_points_all_users_hack(points_to_increment = 1):
    with con:
        print unicode(all_users)
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE points = points + " + str(points_to_increment), user)
        
        #print "DEBUG (last executed): " + cur._last_executed
        return "success"
