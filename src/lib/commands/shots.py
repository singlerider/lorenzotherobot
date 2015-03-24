"""
Developed Shane Engelman <me@5h4n3.com>
"""
# IN ORDER FOR THIS TO RUN CORRECTLY
# run '!shots init 0' the first time
import sqlite3
import os
import globals

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "shots.db"))

mod_name = globals.CURRENT_USER


class UserData (object):

    """ Save the points to a database """

    INITIAL_VALUE = 0

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
                if user is not '':  # added as test
                    if self.get_user(user) is None:
                        conn = sqlite3.connect(self.filepath)
                        # Let's add the user then
                        conn.execute("INSERT INTO users VALUES(?,?)", ("curvyllama",
                                                                       self.INITIAL_VALUE))
                        conn.commit()
                        conn.close()
                    else:
                        conn = sqlite3.connect(self.filepath)
                        # Let's update the existing user
                        conn.execute("UPDATE users SET points = points + ?" +
                                     " WHERE username = ?", (self.INITIAL_VALUE, "curvyllama"))
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

    def special_set(self, users):
        if self.get_user(users) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
            # Let's update the existing user
            conn.execute("UPDATE users SET points = points = ?" +
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

get_shots = UserData(DATABASE_FILE)
return_shots = get_shots.get_user("curvyllama")


def delta_shots(add_remove, delta_user, delta):
    users = globals.channel
    UserData.delta.append(delta)
    print "1"
    if add_remove == "add":
        print "2"
        shots_object = UserData(DATABASE_FILE)
        try:
            shots_object.special_save(users)
            return "Success! " + delta + " shots added!"
        except:
            return "failure"
    elif add_remove == "remove":
        print "3"
        shots_object = UserData(DATABASE_FILE)
        try:
            shots_object.special_remove(users)
            return str(delta) + " shots removed! Only " + str(return_shots - int(delta)) + " remaining!"
        except:
            return "failure"
    elif add_remove == "set":
        print "4"
        shots_object = UserData(DATABASE_FILE)
        try:
            shots_object.special_set(users)
            return "The number of shots has been set to " + delta + "! It has begun."
        except:
            return "failure"
    elif add_remove == "init":
        print "5"
        shots_object = UserData(DATABASE_FILE)
        try:
            shots_object.save(users)
            return "Success! database initialized!"
        except:
            return "failure"
    else:
        return "You must choose either 'add', 'remove', 'init', or 'set'"


def shots(args):

    usage = "!shots (add/remove/set [amount])"

    approved_list = [
        'curvyllama', 'peligrosocortez', 'singlerider', 'newyork_triforce']

    add_remove = args[0]
    delta = args[1]

    if mod_name in approved_list:
        return delta_shots(add_remove, "delta_user", delta)

    else:
        return "Only " + ", ".join(approved_list) + " are allowed to do that!"
