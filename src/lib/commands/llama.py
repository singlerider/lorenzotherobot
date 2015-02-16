"""
Developed by dustinbcox

Adjustments by Shane Engelman <me@5h4n3.com>
"""

import sqlite3
import os
#import src.lib.user_data as user_data
import urllib2
import ast
import requests, json
import src.lib.commands.pokemon as pokemon_import



DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "llama.db"))



def get_dict_for_users():
    response = urllib2.urlopen('https://tmi.twitch.tv/group/user/curvyllama/chatters') #change username to your channel
    user_dict = ast.literal_eval(response.read())
    user_list = ast.literal_eval("['" + str("', '".join(user_dict["chatters"]["moderators"])) + "', '" + str("', '".join(user_dict["chatters"]["viewers"])) + "']")
    return user_dict, user_list

def get_stream_status():
    url = 'https://api.twitch.tv/kraken/streams/curvyllama'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    if data["stream"] != None:
        return True

stream_status = get_stream_status()

def get_stream_followers():
    url = 'https://api.twitch.tv/kraken/channels/curvyllama/follows'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    return data
    
"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""

stream_data = get_stream_status() 
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
        llama_object.save(user_list)
        #print "Added to database!"
        return "Treats added"
    except:
        return "Failure"

def llama(args):
    grab_user = args[0].lower()
    get_treats = UserData(DATABASE_FILE)
    return_treats = get_treats.get_user(grab_user)
    return_individual_treats = get_treats.get_user(user_data_name)
    return_treats_all = get_treats.get_users(grab_user)

    
    usage = "!llama (list, treats, stream, [username], viewers, followers, usage)"
    
    if grab_user == "list":
        return return_treats_all  
    elif grab_user == "treats":
        return str(user_data_name) + ", you've got a total of " + str(return_individual_treats) + " Llama treats. You go, girl!"
    elif grab_user == "print":
        return get_stream_status()
    elif grab_user == "stream":
        url = 'https://api.twitch.tv/kraken/streams/curvyllama'
        resp = requests.get(url=url)
        data = json.loads(resp.content)
        try:
            return str(data["stream"]["channel"]["status"]) + " " + str(data["stream"]["channel"]["display_name"]) + " " + "playing " + str(data["stream"]["game"])
        except:
            return str(data["stream"]["channel"]["display_name"]) + "doesn't appear to be online?"
    elif grab_user == "viewers":
        user_dict, user_list = get_dict_for_users()
        return str(str(user_dict["chatters"]["moderators"]) + ", " + str(user_dict["chatters"]["viewers"])).replace("[", "").replace("]", "").replace("'", "")
    elif grab_user == "followers":
        stream_followers = get_stream_followers()
        follower_list = str(stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(stream_followers["follows"][2]["user"]["display_name"]) + ", " + str(stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(stream_followers["follows"][4]["user"]["display_name"])
        return "In case you missed them, here are the five most recent Llamas: " + follower_list
    elif grab_user == "usage":
        return usage
    elif return_treats is not None:
        return str(args[0]) + " has a total of " + str(return_treats) + " Llama treats. Keep it up!"
    else:
        print get_stream_status()
        return "No entry found for " + str(args[0])
