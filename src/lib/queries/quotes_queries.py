#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from src.lib.queries.connection import get_connection


class Quotes:

    def __init__(self):
        self.con = get_connection()

    def add_quote(
            self, channel="testchannel", user="testuser",
            quote="quote", game="testgame"):
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                SELECT count(0) FROM quotes WHERE channel = %s
                """, [channel])
            count = cur.fetchone()[0]
            cur.execute("""
                INSERT INTO quotes VALUES (NULL, %s, %s, %s, %s, %s)
                """, [channel, user, quote, count + 1, game])
            cur.close()

    def remove_quotes(self, channel="testchannel"):  # pragma: no cover
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                DELETE FROM quotes WHERE channel = %s
                """, [channel])
            cur.close()

    def get_quote(self, channel="testchannel"):
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                SELECT count(0) FROM quotes WHERE channel = %s;
                """, [channel])
            result = cur.fetchone()
            print result
            if result[0] == 0:
                return 0
            random_quote = random.choice(range(result[0]))
            cur.execute("""
                SELECT * FROM quotes WHERE channel = %s;
                """, [channel])
            quote = cur.fetchall()[random_quote - 1]
            cur.close()
            return quote
