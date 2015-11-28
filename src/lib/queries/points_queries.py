#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.lib.queries.connection import *


def mysql_ping():
    con = get_connection()
    with con:

        con.ping()
        print "pinging database"


def get_points_list():
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute(
            """SELECT username, donation_points FROM users ORDER BY points * 1 DESC""")
        user_data = cur.fetchall()
        user_data_comprehension = [
            "{}: {}".format(x, y) for x, y in user_data[0:9]]
        return " | ".join(user_data_comprehension)


def get_user_points(username):
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute("select donation_points from users where username = %s", [username])
        try:
            points = cur.fetchone()
            if points[0] > 0:
                return points[0]
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except:
            return "User not found. Check your spelling."


def set_user_points(delta_user, delta):
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute("update users set donation_points = %s where username = %s", [
                    delta, delta_user])


def modify_user_points(delta_user, delta):
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute("""INSERT INTO users (username, points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE points = points + %s""",
                    [delta_user, delta, delta])


def modify_points_all_users(all_users, points_to_increment=1):
    con = get_connection()
    user_list_for_query = [(x, str(points_to_increment)) for x in all_users]
    try:
        with con:
            cur = con.cursor()

            dData = user_list_for_query  # exact input you gave

            sql = """
            INSERT INTO users
              (username, points)
            VALUES
              (%s, %s)
            ON DUPLICATE KEY UPDATE
              points = points + """ + str(points_to_increment)
            cur.executemany(sql, ((user, points) for user, points in dData))
            return "success"

    except Exception, error:
        print "ERROR", error
        return "Error incrementing points:" + str(error)


def modify_points_all_users_timer(all_users, points_to_increment=1):
    con = get_connection()
    user_list_for_query = [(x, str(points_to_increment)) for x in all_users]
    try:
        with con:
            cur = con.cursor()

            dData = user_list_for_query  # exact input you gave

            sql = """
            INSERT INTO users
              (username, time_points)
            VALUES
              (%s, %s)
            ON DUPLICATE KEY
                UPDATE time_points = time_points + """ + str(points_to_increment)
            cur.executemany(sql, ((user, points) for user, points in dData))
            sql = """
            INSERT INTO users
              (username, time_in_chat)
            VALUES
              (%s, %s)
            ON DUPLICATE KEY
                UPDATE time_in_chat = time_in_chat + """ + str(5)
            cur.executemany(sql, ((user, points) for user, points in dData))
            return "success"

    except Exception, error:
        print "ERROR", error
        return "Error incrementing points:" + str(error)


def modify_points_all_users_hack(points_to_increment=1):
    con = get_connection()
    with con:
        print unicode(all_users)
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE points = points + " +
                    str(points_to_increment), user)
        return "success"


def get_time_in_chat(user):
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute("select time_in_chat from users where username = %s", [username])
        try:
            points = cur.fetchone()
            if points[0] > 0:
                return points[0]
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except:
            return "User not found. Check your spelling."
