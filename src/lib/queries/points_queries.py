#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.lib.queries.connection import *
import random

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


def get_user_points(username):  # only gets donation_points
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute(
            "select donation_points from users where username = %s",
            [username])
        try:
            points = cur.fetchone()
            if points[0] > 0:
                return points[0]
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except:
            return "User not found. Check your spelling."


def get_user_time_points(username):  # only gets donation_points
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute(
            "select time_points from users where username = %s", [username])
        points = cur.fetchone()
        if len(points) > 0:
            return points[0]
        else:
            return 0


def get_all_user_points(username):  # gets all of a single user's points
    con = get_connection()
    with con:

        cur = con.cursor()
        cur.execute("select donation_points, time_points from users where username = %s", [username])
        try:
            points = cur.fetchone()
            donation_points = points[0]
            time_points = points[1]
            total = donation_points + time_points
            llama_responses = [
                "All {0} your treats are belong to me".format(total),
                "{0} treats, lit-tle man, put that shit in my hand".format(
                    total),
                "{0} - Mo' treats, mo' problems".format(total),
                "1 treat, 2 treat, 3 treat, {0}".format(total),
                "How many treats does it take to get to the center of a Tootsie Roll pop? {0}".format(
                    total),
                "{0} - the answer to the meaning of life.".format(total),
                "{0} - treats game on fleek".format(total),
                "{0} - very impressi - ResidentSleeper".format(total)
                ]

            print cur.fetchone()#, donation_points, time_points
            if time_points > 0 or donation_points > 0:
                return random.choice(llama_responses)
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except Exception as error:
            print error
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
        cur.execute("""INSERT INTO users (username, donation_points) VALUES (%s, %s) ON DUPLICATE KEY UPDATE donation_points = donation_points + %s""",
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
              (username, donation_points)
            VALUES
              (%s, %s)
            ON DUPLICATE KEY UPDATE
              donation_points = donation_points + """ + str(points_to_increment)
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
