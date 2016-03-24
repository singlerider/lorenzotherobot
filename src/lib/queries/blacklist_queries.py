from src.lib.queries.connection import get_connection


def add_to_blacklist(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO blacklist (id, username) VALUES (NULL, %s)
            """, [username])
        cur.close()


def remove_from_blacklist(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            DELETE FROM blacklist WHERE username = %s
            """, [username])
        cur.close()


def check_for_blacklist(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT username FROM blacklist WHERE username = %s
            """, [username])
        user = cur.fetchone()
        cur.close()
    return user
