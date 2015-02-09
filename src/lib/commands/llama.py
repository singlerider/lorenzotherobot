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
#import src.lib.user_data as user_data
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
        try:
            for user in users:
                if user is not '':#added as test
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
        except:
            pass
 
    def get_user(self, username):
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT points FROM users WHERE username = ?",
                              (username,))
        points = cursor.fetchone()
        if points is not None:
            points = points[0] # get only the points from the tuple
        conn.close()
        return points
    def get_users(self):
        """ Get all of the users point data ordered by point value"""
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT username,points FROM users ORDER BY points * 1 DESC")
        user_data = cursor.fetchall()
        conn.close()
        return user_data

# If run interactively as llama.py
if __name__ == "__main__":
    llama_object = UserData("llama.db")
    print llama_object.get_users()
 
    #user_list = ['greg', 'jerry', 'larry', 'sam', 'jenny', 'moe', 'cindy',
    #            'shane']
    
    llama_object.save(user_list)
    print "Users:"
    for user in user_list:
        if user is not '':#added as test
            print "User:", user, " ",
            print llama_object.get_user(user)
    
"""Gets list of users and returns them to the chat"""
def enter_into_database():
    
    # Path is relative - for Unix
    llama_object = UserData("llama.db")
    try:
        if "curvyllama" in user_dict["chatters"]["moderators"]:
            #print "Match for user_list: ", user_list
            llama_object.save(user_list)
            print "Added to database!"
            #print "Type: ", type(user_list)# Should say 'list'
            return "Points added"
        else:
            #print "No match for user_list: ", user_list 
            return str(", ".join(user_dict["chatters"]["moderators"]) + ", " + ", ".join(user_dict["chatters"]["viewers"]))
    except:
        return "Failure"

def llama():
    return "working on it" 