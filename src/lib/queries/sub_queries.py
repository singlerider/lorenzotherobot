from src.lib.queries.connection import get_connection


def get_oauth(channel):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT twitch_oauth FROM auth WHERE channel = %s
        """, [channel])
        oauth = cur.fetchone()
        cur.close()
        return oauth
