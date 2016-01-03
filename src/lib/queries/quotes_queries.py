#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.lib.queries.connection import *
import random


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

    def remove_quotes(self, channel="testchannel"):
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                DELETE FROM quotes WHERE channel = %s
                """, [channel])

    def get_quote(self, channel="testchannel"):
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                SELECT * FROM quotes WHERE channel = %s
                    ORDER BY RAND() LIMIT 1;
                """, [channel])
            quote = cur.fetchone()
            return quote
