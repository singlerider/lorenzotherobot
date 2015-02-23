"""
Developed by dustinbcox and Shane Engelman <me@5h4n3.com>
"""

import sqlite3
import os
import urllib2
import ast
import requests, json
import src.lib.commands.pokemon as pokemon_import
import random
import src.bot
import sys
import datetime
import time

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "llama.db"))



def get_dict_for_users():
    response = urllib2.urlopen('https://tmi.twitch.tv/group/user/curvyllama/chatters') #change username to your channel
    user_dict = ast.literal_eval(response.read())
    user_list = ast.literal_eval("['" + str("', '".join(user_dict["chatters"]["moderators"])) + "', '" + str("', '".join(user_dict["chatters"]["viewers"])) + "']")
    return user_dict, user_list

def get_stream_status():
    get_stream_status_url = 'https://api.twitch.tv/kraken/streams/curvyllama'
    get_stream_status_resp = requests.get(url=get_stream_status_url)
    online_data = json.loads(get_stream_status_resp.content)
    if online_data["stream"] != None:
        return True
    
def get_stream_uptime():
    try:
        format = "%Y-%m-%d %H:%M:%S"
        get_stream_uptime_url = 'https://api.twitch.tv/kraken/streams/curvyllama'
        get_stream_uptime_resp = requests.get(url=get_stream_uptime_url)
        uptime_data = json.loads(get_stream_uptime_resp.content)
        start_time = str(uptime_data['stream']['created_at']).replace("T", " ").replace("Z", "")
        stripped_start_time = datetime.datetime.strptime(start_time, format)
        time_delta = datetime.datetime.utcnow() - stripped_start_time
        return time_delta
    except:
        return "She's offline, duh."
    
def get_offline_status():
    get_offline_status_url = 'https://api.twitch.tv/kraken/streams/curvyllama'
    get_offline_status_resp = requests.get(url=get_offline_status_url)
    offline_data = json.loads(get_offline_status_resp.content)
    if offline_data["stream"] != None:
        return True

stream_status = get_stream_status()

def get_stream_followers():
    url = 'https://api.twitch.tv/kraken/channels/curvyllama/follows'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    return data

def random_highlight():
    get_highlight_url = "https://api.twitch.tv/kraken/channels/curvyllama/videos?limit=20"
    get_highlight_resp = requests.get(url=get_highlight_url)
    highlights = json.loads(get_highlight_resp.content)
    random_highlight_choice = random.choice(highlights["videos"])
    return str(str(random_highlight_choice["title"]) + " | " + str(random_highlight_choice["description"]) + " | " + str(random_highlight_choice["length"]) + " minutes | " + str(random_highlight_choice["url"]) + " | Tags: " + str(random_highlight_choice["tag_list"])).replace("\n", " ").replace("\r", " ")

    
"""Database in progress. This will run as a cron job and will serve as the points counter and Pokemon assigning tool"""

stream_data = get_stream_status() 
class UserData (object):
    """ Save the points to a database """
 
    # Start off with 5 points, add incrementally this value each time ran
    INITIAL_VALUE = 1
    
    delta = []
 
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
        
    def special_save(self, users):
        if self.get_user(users) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
                # Let's update the existing user
            conn.execute("UPDATE users SET points = points + ?" +
                         " WHERE username = ?", (self.delta[0], users))
            conn.commit()
            conn.close()
            
    def special_remove(self, users):
        if self.get_user(users) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
                # Let's update the existing user
            conn.execute("UPDATE users SET points = points - ?" +
                         " WHERE username = ?", (self.delta[0], users))
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
    user_dict, user_list = get_dict_for_users()
    llama_object.save(user_list)
    print "Users:"
    for user in user_list:
        if user is not '':#added as test
            print "User:", user, " ",
            print llama_object.get_user(user)
    
"""Gets list of users and returns them to the chat"""
def enter_into_database():
    try:
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
    except:
        return "Major error reconciled. Notify singlerider (Shane) to let him know he can remove this message."

def delta_treats(add_remove, delta_user, delta):
    users = delta_user
    UserData.delta.append(delta)
    print "1"
    if add_remove == "add":
        print "2"
        llama_object = UserData(DATABASE_FILE)
        try:
            llama_object.special_save(users)
            return "Success! " + delta + " treats added for " + delta_user + "!"
        except:
            return "failure"
    elif add_remove == "remove":
        print "3"
        llama_object = UserData(DATABASE_FILE)
        try:
            llama_object.special_remove(users)
            return "Success! " + delta + " treats removed from " + delta_user + "!"
        except:
            return "failure"
    
        

def llama(args):
    grab_user = args[0].lower()
    get_treats = UserData(DATABASE_FILE)
    return_treats = get_treats.get_user(grab_user)
    return_individual_treats = get_treats.get_user(user_data_name)
    return_treats_all = get_treats.get_users(grab_user)

    
    usage = "!llama (list, treats, stream, [username], highlight, viewers, followers, usage, uptime)"
    
    if grab_user == "list":
        return return_treats_all  
    elif grab_user == "treats":
        return str(user_data_name) + ", you've got a total of " + str(return_individual_treats) + " Llama treats. You go, girl!"
    elif grab_user == "print":
        return get_stream_status()
    elif grab_user == "stream":
        get_offline_status_url = 'https://api.twitch.tv/kraken/channels/curvyllama'
        get_offline_status_resp = requests.get(url=get_offline_status_url)
        offline_data = json.loads(get_offline_status_resp.content)
        try:
            return str(offline_data["status"]) + " | " + str(offline_data["display_name"]) + " playing " + str(offline_data["game"])
        except:
            return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"
    elif grab_user == "viewers":
        user_dict, user_list = get_dict_for_users()
        return str(str(user_dict["chatters"]["moderators"]) + ", " + str(user_dict["chatters"]["viewers"])).replace("[", "").replace("]", "").replace("'", "")
    elif grab_user == "highlight":
        try:
            return random_highlight()
        except:
            return "Listen, man. Don't blame me. Blame the Twitch API."
    elif grab_user == "followers":
        stream_followers = get_stream_followers()
        follower_list = str(stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(stream_followers["follows"][2]["user"]["display_name"]) + ", " + str(stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(stream_followers["follows"][4]["user"]["display_name"])
        return "In case you missed them, here are the five most recent Llamas: " + follower_list
    elif grab_user == "uptime":
        return get_stream_uptime()
    
    elif grab_user == "usage":
        return usage
    elif return_treats is not None:
        return str(args[0]) + " has a total of " + str(return_treats) + " Llama treats. Keep it up!"
    else:
        print get_stream_status()
        return "No entry found for " + str(args[0])
