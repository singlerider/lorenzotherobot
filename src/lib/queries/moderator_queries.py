#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.lib.queries.connection import get_connection


def add_moderator(username, channel):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO moderators (username, channel)
                SELECT moderators.username, moderators.channel
                FROM
                  (SELECT %s username, %s channel) moderators
                WHERE NOT EXISTS (
                       SELECT 1
                       FROM moderators
                       WHERE username = %s and channel = %s)
            """, [username, channel, username, channel])
        cur.close()


def get_moderator(username, channel):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT username, channel FROM moderators
                WHERE username = %s AND channel = %s
            """, [username, channel])
        moderator = cur.fetchone()
        cur.close()
        return moderator
