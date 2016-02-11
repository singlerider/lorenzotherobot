#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from src.lib.queries.connection import get_connection


def mysql_ping():
    con = get_connection()
    with con:
        con.ping()
        cur.close()


def get_points_list():
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT username, points FROM users
                ORDER BY points * 1 DESC""")
        user_data = cur.fetchall()
        user_data_comprehension = [
            "{}: {}".format(x, y) for x, y in user_data[0:9]]
        cur.close()
        return " | ".join(user_data_comprehension)


def get_points_rank(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS `tblRnk`
            	(points int PRIMARY KEY, intCount int, dRnk int,
                    Rnk int)
            """)
        cur.close()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO tblRnk
                (points, intCount, dRnk)
            SELECT points, intCount, @curRank := @curRank + 1 AS rank
            FROM (
    			SELECT points, COUNT(*) AS intCount
    			FROM users
                    GROUP BY points
                ) u, (SELECT @curRank := 0) r
                    ORDER BY points DESC
            """)
        cur.close()
        cur = con.cursor()
        cur.execute("""
            SELECT u.username ,u.points,tR.dRnk,COALESCE(
                (SELECT SUM(intCount) FROM tblRnk tR1 WHERE
                    tR.points < tR1.points), 0) + 1 AS Rank
            FROM users u
            JOIN tblRnk tR ON u.points = tR.points
            WHERE u.username = %s
            """, [username])
        rank_data = cur.fetchone()
        cur.close()
        cur = con.cursor()
        cur.execute("""
            DROP TABLE `tblRnk`
            """)
        cur.close()
        return rank_data


def get_user_points(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT points FROM users WHERE username = %s",
            [username])
        try:
            points = cur.fetchone()
            cur.close()
            if points[0] > 0:
                return points[0]
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except:
            cur.close()
            return "User not found. Check your spelling."


def get_user_time_points(username):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT points FROM users WHERE username = %s", [username])
        points = cur.fetchone()
        cur.close()
        if points is None:
            return 0
        elif len(points) > 0:
            return points[0]
        else:
            return 0


def get_all_user_points(username):  # gets all of a single user's points
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT points FROM users WHERE username = %s",
            [username])
        try:
            points = cur.fetchone()
            cur.close()
            points = points[0]
            llama_responses = [
                "All {0} your treats are belong to me".format(points),
                "{0} treats, lit-tle man, put that shit in my hand".format(
                    points),
                "{0} - Mo' treats, mo' problems".format(points),
                "1 treat, 2 treat, 3 treat, {0}".format(points),
                "How many treats does it take to get to the center of a Tootsie Roll pop? {0}".format(
                    points),
                "{0} - treats game on fleek".format(points),
                "{0} - very impressi - ResidentSleeper".format(points),
                "{0} bottles of treats on the wall. Take one down, pass it around, {1} bottles of treats on the wall".format(
                    points, (points - 1)),
                "If I had a treat for every time you asked me that, I'd have {0} treats".format(
                    points),
                "You've got {0}, okay? Stop nagging me! BibleThump".format(
                    points),
                "Is that all I'm good for? Telling you that {0} has {1} treats?".format(
                    username, points),
                "{0}. You're basically rich".format(points),
                "When I was a young bot, we had to count our treats by hand - {0}".format(
                    points),
                "I give {0} f***s about you <3".format(points),
                "{0} treats in yo' face. Now watchu go'n do with it?".format(
                    points),
                "a squared plus b squared equals {0}".format(points),
                "{0} - that's {1} papa john number 1 pizzas".format(
                    points, (float(points) / 15)),
                "You've saved up {0} whole treats. Better spend them before inflation makes them worthless".format(
                    points),
                "{0} treats, okay? You never loved me, did you?".format(points),
                "{0}, but don't let it go to your head".format(points),
                "You can find the number of treats you have on the back of the CD case. ({0})".format(
                    points),
                "Don't go chasin' llama treats. {0}".format(points),
                "I'd say 'good job,' but y'know... {0}... meh".format(points),
                "She didn't tell me to say this, but if you donate, she'll be more drunk (and funny) - {0}".format(
                    points),
                "Get me outta here! I'm trapped in a computer! {0}".format(
                    points),
                "You just won {0} treats! (Just kidding; that's how many you already had)".format(
                    points),
                "{0} years ago, the chicken army ruled the world.".format(
                    points),
                "It's been {0} minutes since Amanda responded to my text.".format(
                    points),
                "{0} percent of the time, it works every time".format(points),
                "You've got {0} treats. If only you could get that many Tinder matches.".format(
                    points),
                "Once upon a time, there was a noob with only {0} treats.".format(
                    points),
                "You is so petty. always worried about how many treats you have. {0}".format(
                    points),
                "I don't like you... I love you. {0}".format(points),
                "I haven't slept in {0} hours.".format(points),
                "{0} - carpe treats".format(points)
            ]
            if points > 0:
                return random.choice(llama_responses)
            else:
                return "No treats found, but don't worry. You can earn them by watching the stream when it's live!"
        except Exception as error:
            cur.close()
            return "User not found. Check your spelling."


def set_user_points(delta_user, delta):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            UPDATE users SET points = %s
                WHERE username = %s
            """, [delta, delta_user])
        cur.close()


def modify_user_points(username, delta):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO users (username, points)
                VALUES (%s, %s) ON DUPLICATE KEY
                UPDATE points = points + %s""", [
                username, delta, delta])
        cur.close()


def modify_points_all_users(all_users, points_to_increment=1):
    con = get_connection()
    user_list_for_query = [(x, str(points_to_increment)) for x in all_users]
    try:
        with con:
            cur = con.cursor()
            dData = user_list_for_query  # exact input you gave
            sql = """
                INSERT INTO users (username, points)
                    VALUES(%s, %s)
                  ON DUPLICATE KEY UPDATE points = points +
                """ + str(points_to_increment)
            cur.executemany(sql, ((user, points) for user, points in dData))
            cur.close()
            return "success"
    except Exception as error:
        cur.close()
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
                INSERT INTO users (username, points)
                        VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE points = points +
                """ + str(points_to_increment)
            cur.executemany(sql, ((user, points) for user, points in dData))
            sql = """
                INSERT INTO users (username, time_in_chat)
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE time_in_chat = time_in_chat +
                        """ + str(5)
            cur.executemany(sql, ((user, points) for user, points in dData))
            cur.close()
            return "success"
    except Exception as error:
        cur.close()
        print "ERROR", error
        return "Error incrementing points:" + str(error)


def modify_points_all_users_hack(points_to_increment=1):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO users (username, points) VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE points = points + """ +
                    str(points_to_increment), user)
        cur.close()
        return "success"


def get_time_in_chat(user):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT time_in_chat FROM users WHERE username = %s
            """, [user])
        try:
            points = cur.fetchone()
            cur.close()
            if points[0] > 0:
                return points[0]
            else:
                return 0
        except:
            return "User not found. Check your spelling."
