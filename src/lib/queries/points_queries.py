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
                "{0} - treats game on fleek".format(total),
                "{0} - very impressi - ResidentSleeper".format(total),
                "{0} bottles of treats on the wall. Take one down, pass it around, {1} bottles of treats on the wall".format(
                    total, (total - 1)),
                "If I had a treat for every time you asked me that, I'd have {0} treats".format(
                    total),
                "You've got {0}, okay? Stop nagging me! BibleThump".format(total),
                "Is that all I'm good for? Telling you that {0} has {1} treats?".format(
                    username, total),
                "{0}. You're basically rich".format(total),
                "When I was a young bot, we had to count our treats by hand - {0}".format(total),
                "{0}, but only {1} are from donations Kappa".format(
                    total, (donation_points)),
                "I give {0} f***s about you <3".format(total),
                "{0} treats in yo' face. Now watchu go'n do with it?".format(total),
                "a squared plus b squared equals {0}".format(total),
                "{0} - that's {1} papa john number 1 pizzas".format(
                    total, (float(total) / 15)),
                "You've saved up {0} whole treats. Better spend them before inflation makes them worthless".format(
                    total),
                "{0} treats, okay? You never loved me, did you?".format(total),
                "{0}, but don't let it go to your head".format(total),
                "You can find the number of treats you have on the back of the CD case. ({0})".format(total),
                "Don't go chasin' llama treats. {0}".format(total),
                "I'd say 'good job,' but y'know... {0}... meh".format(total),
                "She didn't tell me to say this, but if you donate, she'll be more drunk (and funny) - {0}".format(
                    total),
                "Get me outta here! I'm trapped in a computer! {0}".format(
                    total),
                "You just won {0} treats! (Just kidding; that's how many you already had)".format(total),
                "{0} years ago, the chicken army ruled the world.".format(total),
                "It's been {0} minutes since Amanda responded to my text.".format(total),
                "{0} percent of the time, it works every time".format(total),
                "You've got {0} treats. If only you could get that many Tinder matches.".format(total)
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
