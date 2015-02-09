"""
Developed by dustinbcox

Adjustments by Shane Engelman <me@5h4n3.com>
"""

import sqlite3
import sys
import re
import socket
import pexpect
import time
import os
import src.lib.user_data as user_data
import urllib2
import ast

response = urllib2.urlopen('https://tmi.twitch.tv/group/user/curvyllama/chatters')#change username to your channel
user_dict = ast.literal_eval(response.read())

user_list = ast.literal_eval("['" + str("', '".join(user_dict["chatters"]["moderators"])) + "', '" + str("', '".join(user_dict["chatters"]["viewers"])) + "']")

"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""

 
class UserData (object):
    """ Save the points to a database """
 
    # Start off with 5 points, add incrementally this value each time ran
    INITIAL_VALUE = 5
 
    def __init__(self, filepath):
        """ Initialize the database as needed """
        self.filepath = filepath
        conn = sqlite3.connect(self.filepath)
        conn.execute("""CREATE TABLE IF NOT EXISTS users
                    (username VARCHAR(50) PRIMARY KEY,
                    points INTEGER);""")
        conn.commit()
        conn.close()
    # Saves user and points to database 
    def save(self, users):
        for user in users:
            while user is not '':#added as test
                if self.get_user(user) is None:
                    conn = sqlite3.connect(self.filepath)
                    # Let's add the user then
                    conn.execute("INSERT INTO users VALUES(?,?)", (user,
                                 self.INITIAL_VALUE))
                    conn.commit()
                    conn.close()
                else:
                    conn = sqlite3.connect(self.filepath)
                    # Let's update the existing user
                    conn.execute("UPDATE users SET points = points + ?" +
                                 " WHERE username = ?", (self.INITIAL_VALUE, user))
                    conn.commit()
                    conn.close()
 
    def get_user(self, username):
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT points FROM users WHERE username = ?",
                              (username,))
        points = cursor.fetchone()
        if points is not None:
            points = points[0] # get only the points from the tuple
        conn.close()
        return points

# If run interactively as llama.py
if __name__ == "__main__":
    llamas = UserData("sample_sqlite_database.db")
 
    #user_list = ['greg', 'jerry', 'larry', 'sam', 'jenny', 'moe', 'cindy',
    #            'shane']
    
    llamas.save(user_list)
    print "Users:"
    for user in user_list:
        while user is not '':#added as test
            print "User:", user, " ",
            print llamas.get_user(user)
    
"""Gets list of users and returns them to the chat"""
def llama():
    
    # Path is relative - for Unix
    llama_object = UserData("llama.db")
    
    if "curvyllama" in user_dict["chatters"]["moderators"]:
        print "Match for user_list: ", user_list
        llama_object.save(user_list)
        #print "Type: ", type(user_list)# Should say 'list'
    else:
        print "No match for user_list: ", user_list 
    return str(", ".join(user_dict["chatters"]["moderators"]) + ", " + ", ".join(user_dict["chatters"]["viewers"]))