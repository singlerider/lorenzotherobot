"""
Developed by dustinbcox

Adjustments by Shane Engelman <me@5h4n3.com>
"""

import sqlite3
import os
#import src.lib.user_data as user_data
import urllib2
import ast


DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "llama.db"))


def get_dict_for_users():
    response = urllib2.urlopen('https://tmi.twitch.tv/group/user/curvyllama/chatters') #change username to your channel
    user_dict = ast.literal_eval(response.read())
    user_list = ast.literal_eval("['" + str("', '".join(user_dict["chatters"]["moderators"])) + "', '" + str("', '".join(user_dict["chatters"]["viewers"])) + "']")
    return user_dict, user_list
    
"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""

 
class UserData (object):
    """ Save the points to a database """
 
    # Start off with 5 points, add incrementally this value each time ran
    INITIAL_VALUE = 1
 
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
    def get_users(self, username):
        """ Get all of the users point data ordered by point value"""
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT username,points FROM users ORDER BY points * 1 DESC")
        user_data = cursor.fetchall()
        conn.close()
        return str(user_data[2:12]).replace("[", "").replace("(u'", "").replace(", ", " | ").replace("]", "").replace(")", "")

# If run interactively from shell as $ python2 llama.py
if __name__ == "__main__":
    llama_object = UserData(DATABASE_FILE)
    print llama_object.get_users()
 
    #user_list = ['greg', 'jerry', 'larry', 'sam', 'jenny', 'moe', 'cindy',
    #            'shane']
    user_dict, user_list = get_dict_for_users()
    llama_object.save(user_list)
    print "Users:"
    for user in user_list:
        if user is not '':#added as test
            print "User:", user, " ",
            print llama_object.get_user(user)
    
"""Gets list of users and returns them to the chat"""
def enter_into_database():
    # Returns tuple, gets expanded below
    user_dict, user_list = get_dict_for_users()

    # Path is relative - for Unix
    llama_object = UserData(DATABASE_FILE)
    try:
        if user_dict["chatters"]["viewers"] is None:
            return "No treats are added when only moderators are online"
        elif "curvyllama" in user_dict["chatters"]["moderators"]:
            #print "Match for user_list: ", user_list
            llama_object.save(user_list)
            print "Added to database!"
            #print "Type: ", type(user_list)# Should say 'list'
            return "Treats added"
        else:
            #print "No match for user_list: ", user_list 
            return "Treats will only be added when Curvyllama is online."
    except:
        return "Failure"

def llama(args):
    grab_user = args[0].lower()
    get_treats = UserData(DATABASE_FILE)
    return_treats = get_treats.get_user(grab_user)
    return_treats_all = get_treats.get_users(grab_user)
    if grab_user == "list":
        return return_treats_all    
    elif return_treats is not None:
        return str(args[0]) + " has a total of " + str(return_treats) + " Llama treats. Keep it up!"
    else:
        return "No entry found for " + str(args[0])
