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