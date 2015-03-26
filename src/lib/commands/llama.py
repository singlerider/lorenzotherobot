"""
Developed by dustinbcox and Shane Engelman <me@5h4n3.com>
"""

import sqlite3
import os
import importlib
import src.lib.commands.shots as shots_import
from src.lib.twitch import *

user_commands_import = importlib.import_module('src.lib.user_commands')
# reload(user_commands_import)

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "llama.db"))

class UserData (object):

    """ Save the points to a database """

    # Start off with 5 points, add incrementally this value each time ran
    INITIAL_VALUE = 1

    delta = []

# NEED TO ADD ALTER TABLE for pokemon IF NOT EXISTS

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
                if user is not '':  # added as test
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
            conn = sqlite3.connect(self.filepath)
            # Let's update the existing user
            conn.execute("UPDATE users SET points = points + ?" +
                         " WHERE username = ?", (self.delta[0], users))
            conn.commit()
            conn.close()

    def special_save_all(self, users):
        try:
            for user in users:
                if user is not '':  # added as test
                    if self.get_user(user) is None:
                        conn = sqlite3.connect(self.filepath)
                        # Let's add the user then
                        conn.execute("INSERT INTO users VALUES(?,?)", (user,
                                                                       self.delta[0]))
                        conn.commit()
                        conn.close()
                    else:
                        conn = sqlite3.connect(self.filepath)
                        # Let's update the existing user
                        conn.execute("UPDATE users SET points = points + ?" +
                                     " WHERE username = ?", (self.delta[0], user))
                        conn.commit()
                        conn.close()
        except:
            pass

    def special_remove(self, users):
        if self.get_user(users) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
            # Let's update the existing user
            conn.execute("UPDATE users SET points = points - ?" +
                         " WHERE username = ?", (self.delta[0], users))
            conn.commit()
            conn.close()

    def special_set(self, users):
        if self.get_user(users) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
            # Let's update the existing user
            conn.execute("UPDATE users SET points = points == ?" +
                         " WHERE username = ?", (self.delta[0], users))
            conn.commit()
            conn.close()


    def get_user(self, username):
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT points FROM users WHERE username = ?",
                              (username,))
        points = cursor.fetchone()
        if points is not None:
            points = points[0]  # get only the points from the tuple
        conn.close()
        return points

    def get_users(self, username):
        """ Get all of the users point data ordered by point value"""
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute(
            "SELECT username,points FROM users ORDER BY points * 1 DESC")
        user_data = cursor.fetchall()
        conn.close()
        return str(user_data[0:12]).replace("[", "").replace("(u'", "").replace(", ", " | ").replace("]", "").replace(")", "")

# If run interactively from shell as $ python2 llama.py
if __name__ == "__main__":
    llama_object = UserData(DATABASE_FILE)
    print llama_object.get_users()
    user_dict, user_list = get_dict_for_users()
    llama_object.save(user_list)
    print "Users:"
    for user in user_list:
        if user is not '':  # added as test
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
            # print "Added to database!"
            return "Treats added"
        except:
            return "Failure"
    except:
        return "Http error. Call/text/email Anarchy_2 IMMEDIATEL.. ResidentSleeper"


def enter_into_database_all(delta):
    try:
        UserData.delta.append(delta)
        # Returns tuple, gets expanded below
        user_dict, user_list = get_dict_for_users()
        # Path is relative - for Unix
        llama_object = UserData(DATABASE_FILE)
        try:
            llama_object.special_save_all(user_list)
            # print "Added to database!"
            return str(delta) + " treats added to everyone in the chat! Raise your Kappas! \Kappa/"
        except:
            return "Failure"
    except:
        return "Major error reconciled. Notify singlerider (Shane) to let him know he can remove this message."


def delta_treats(add_remove, delta_user, delta):
    users = delta_user
    UserData.delta.append(delta)
    if add_remove == "add":
        llama_object = UserData(DATABASE_FILE)
        llama_object.special_save(users)
        return "Success! " + delta + " treats added for " + delta_user + "!"
    elif add_remove == "remove":
        llama_object = UserData(DATABASE_FILE)
        llama_object.special_remove(users)
        return "Success! " + delta + " treats removed from " + delta_user + "!"
       
    elif add_remove == "set":
        llama_object = UserData(DATABASE_FILE)
        llama_object.special_set(users)
        return "Success! " + delta_user + "'s treats set to " + delta + "!"
    else:
        return "You must choose either 'add', 'remove', or 'set'"


def llama(args):
    grab_user = args[0].lower()
    get_treats = UserData(DATABASE_FILE)
    return_treats = get_treats.get_user(grab_user)
    return_individual_treats = get_treats.get_user(user_data_name)
    return_treats_all = get_treats.get_users(grab_user)
    return_shots = shots_import.return_shots

    usage = "!llama (list, treats, me, stream, [username], highlight, viewers, followers, usage, uptime, shots)"

    if grab_user == "list":
        return return_treats_all
    elif grab_user == "treats":
        return str(user_data_name) + ", you've got a total of " + str(return_individual_treats) + " Llama treats. You go, girl!"
    elif grab_user == "me":
        return get_user_command()
    elif grab_user == "stream":
        get_offline_status_url = 'https://api.twitch.tv/kraken/channels/' + \
            globals.channel
        get_offline_status_resp = requests.get(url=get_offline_status_url)
        offline_data = json.loads(get_offline_status_resp.content)
        try:
            return str(offline_data["status"]) + " | " + str(offline_data["display_name"]) + " playing " + str(offline_data["game"])
        except:
            return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"

    elif grab_user == "viewers":
        user_dict, user_list = get_dict_for_users()
        # if user_data_name in user_dict["chatters"]["moderators"]:
        return str(int(len(user_dict["chatters"]["moderators"])) + int(len(user_dict["chatters"]["viewers"]))) + " viewers are in here. That's it?! Kreygasm"
        # return str(str(user_dict["chatters"]["moderators"]) + ", " + str(user_dict["chatters"]["viewers"])).replace("[", "").replace("]", "").replace("'", "")
        # else:
        # return "Only moderators can flood the chat window with a bunch of
        # text :/"
    elif grab_user == "highlight":
        try:
            return random_highlight()
        except:
            return "Listen, man. Don't blame me. Blame the Twitch API."
    elif grab_user == "followers":
        stream_followers = get_stream_followers()
        follower_list = str(stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(stream_followers[
            "follows"][2]["user"]["display_name"]) + ", " + str(stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(stream_followers["follows"][4]["user"]["display_name"])
        return "In case you missed them, here are the five most recent Llamas: " + follower_list + " HeyGuys"
    elif grab_user == "uptime":
        return get_stream_uptime()

    elif grab_user == "usage":
        return usage

    elif grab_user == "shots":
        if return_shots is not None:
            return str(return_shots) + " shots left. She's already dru... ResidentSleeper"
        else:
            return "No shots found. Donate before she goes crazy! Kreygasm"
    elif return_treats is not None:
        user_return = str(args[0]) + " has a total of " + \
            str(return_treats) + " Llama treats. Keep it up!"
        if grab_user in user_commands_import.user_command_dict:
            return user_commands_import.user_command_dict[grab_user]["return"] + " | " + user_return
        else:
            return user_return

    else:
        print get_stream_status()
        return "No entry found for " + str(args[0])
