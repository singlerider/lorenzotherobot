import sqlite3
import os

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../../..", "pokemon.db"))

#Create the table if it doesn't exist.
conn = sqlite3.connect(DATABASE_FILE)
conn.execute("""CREATE TABLE IF NOT EXISTS users
            (user_data_name VARCHAR(50) PRIMARY KEY,
            pokemon_value VARCHAR);""")
conn.commit()


def setPokemon(user, pokemon):
  cmd = "INSERT OR REPLACE INTO users VALUES (?,?)"
  conn.execute(cmd, (user, pokemon))
  conn.commit()

def getPokemon(user):
    cmd = "SELECT pokemon_value FROM users WHERE user_data_name = ?"
    cursor = conn.execute(cmd, (user,))
    conn.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return row[0]


