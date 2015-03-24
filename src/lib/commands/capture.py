import src.lib.commands.llama as llama_import
import globals
import os
import sqlite3

user_data_name = globals.CURRENT_USER

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../..", "pokemon.db"))

pokemon = globals.POKEMON


class UserData (object):

    """ Save the pokemon to a database """

    def __init__(self, filepath):
        """ Initialize the database as needed """
        self.filepath = filepath
        conn = sqlite3.connect(self.filepath)
        conn.execute("""CREATE TABLE IF NOT EXISTS users
                    (user_data_name VARCHAR(50) PRIMARY KEY,
                    pokemon_value VARCHAR);""")
        conn.commit()
        conn.close()

    # Saves user and points to database
    def save(self, users, entry):
        print "3"
        try:
            for user in users:
                if user is not 'current':  # added as test
                    if self.get_pokemon(user) is None:
                        print "14"
                        conn = sqlite3.connect(self.filepath)
                        # Let's add the user then
                        conn.execute("INSERT INTO users VALUES(?,?)", (user,
                                                                       entry))
                        conn.commit()
                        conn.close()
                    else:
                        print "15"
                        conn = sqlite3.connect(self.filepath)
                        # Let's update the existing user
                        conn.execute("UPDATE users SET pokemon_value = ?" +
                                     " WHERE user_data_name = ?", (entry, user))
                        conn.commit()
                        conn.close()
        except:
            pass

# pokemon stuff is in progress
    def add_pokemon(self, user_data_name, pokemon):
        if self.get_user(poke_master) is not None:
            print self.delta[0]
            conn = sqlite3.connect(self.filepath)
            # Let's update the existing user
            conn.execute("UPDATE users SET pokemon = pokemon = ?" +
                         " WHERE username = ?", (self.pokemon, user_data_name))
            conn.commit()
            conn.close()

    def get_pokemon(self, user_data_name):
        print "10"
        users = user_data_name
        conn = sqlite3.connect(self.filepath)
        cursor = conn.execute("SELECT pokemon_value FROM users WHERE user_data_name = ?",
                              (users,))
        poke_cursor = cursor.fetchone()
        if poke_cursor is not None:
            poke_cursor = poke_cursor[0]  # get only the points from the tuple
            conn.close()
            return poke_cursor
        else:
            "Nothing found for you, BRO!"


def enter_into_database():

    # Returns tuple, gets expanded below
    # Path is relative - for Unix
    capture_object = UserData(DATABASE_FILE)
    users = [user_data_name]
    try:
        capture_object.save(users, pokemon)
        # print "Added to database!"
        return "Wild " + pokemon + " was caught!"
    except:
        return "Failure"


def pokemon_query(poke_master):

        # Returns tuple, gets expanded below
        # Path is relative - for Unix
    capture_object = UserData(DATABASE_FILE)
    try:
        user_pokemon = capture_object.get_pokemon(poke_master)
        print poke_master + " pokemaster"
        # print "Added to database!"
        return user_pokemon
    except:
        return "Failure"


def capture():
    usage = "!capture"

    if globals.CAUGHT is False:
        globals.CAUGHT = True

        return enter_into_database()
    else:
        return "Somebody else beat you to it!"
