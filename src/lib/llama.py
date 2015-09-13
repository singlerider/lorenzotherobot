import sqlite3
import os

DATABASE_FILE = os.path.abspath(os.path.join(__file__, "../llama.db"))
conn = sqlite3.connect(DATABASE_FILE)
conn.execute("""CREATE TABLE IF NOT EXISTS users
                  (username VARCHAR(50) PRIMARY KEY,
                  points INTEGER);""")
conn.commit()


def newConnection():
    # Needed for multiple threads working in the db.
    # cron thread calls and uses this for its changes.
    return Connection()


class Connection:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE)

    def setPoints(self, user, points):
        cmd = "INSERT OR REPLACE INTO users VALUES (?,?)"
        print("Set points", user, points)
        self.conn.execute(cmd, (user, points))
        self.conn.commit()

    def addPoints(self, user, delta):
        points = self.getPoints(user)
        self.setPoints(user, delta + points)

    def getPoints(self, user):
        print("Get points:", user)
        cmd = "SELECT points FROM users WHERE username = ?"
        cursor = self.conn.execute(cmd, (user,))
        self.conn.commit()
        row = cursor.fetchone()
        if row is None:
            return 0
        return row[0]

    def hasUser(self, user):
        print("---- has user", user)
        cmd = "SELECT points FROM users WHERE username = ?"
        row = self.conn.execute(cmd, (user,)).fetchone()
        return row is not None

    def getTopUsers(self):
        cmd = "SELECT username, points FROM users ORDER BY points*1 DESC LIMIT 13"
        cursor = self.conn.execute(cmd)
        rows = cursor.fetchall()
        out = []
        for user, points in rows:
            out.append("{} {}".format(user, points))
        return " | ".join(out)
