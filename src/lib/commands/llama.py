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

response = urllib2.urlopen('https://tmi.twitch.tv/group/user/freshnica/chatters')#change username to your channel
user_dict = ast.literal_eval(response.read())

"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""
import sqlite3
 
 
class UserData (object):
    """ Save the points to a database """
 
    # Start off with 5 points
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
 
    def save(self, users):
        for user in users:
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
 
 
if __name__ == "__main__":
    llama = UserData("sample_sqlite_database.db")
 
    my_users = ['greg', 'jerry', 'larry', 'sam', 'jenny', 'moe', 'cindy',
                'shane']
    llama.save(my_users)
    print "Users:"
    for user in my_users:
        print "User:", user, " ",
        print llama.get_user(user)
    
    return str("Viewers: " + ", ".join(user_dict["chatters"]["moderators"]) + ", " + ", ".join(user_dict["chatters"]["viewers"]))
    
"""Gets list of users and returns them to the chat"""



#def llama():

#    return str("Viewers: " + ", ".join(user_dict["chatters"]["moderators"]) + ", " + ", ".join(user_dict["chatters"]["viewers"]))