import os
import random
import re
import string
import threading
import time
from unittest import TestCase

import globals
import src.lib.functions_commands
from src.bot import Bot, BotFactory
from testing.TwitchIrc import (ALT_USER, MOD_USER, REG_USER, TEST_CHAN,
                               TEST_CHANNEL, USERS, TwitchIrc)
from twisted import trial
from twisted.internet import reactor
from twisted.test import proto_helpers


API = False

src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None
server, client = None, None

now = str(time.time()).replace(".", "")

_channel = TEST_CHANNEL
_username = MOD_USER
_us = 'tbb'


def setUpModule():
    global bot, client, fake_transport
    factory = BotFactory("chat")
    bot = factory.buildProtocol(('127.0.0.1', 0))
    fake_transport = proto_helpers.StringTransport()
    bot.makeConnection(fake_transport)
    bot.signedOn()
    bot.joined(_channel)
    fake_transport.clear()
    os.system("mysql -uroot -e \"CREATE DATABASE lorenzotest" + now + "\"")
    globals.mysql_credentials = ['localhost', 'root', '', 'lorenzotest' + now]
    print globals.mysql_credentials
    print "\"CREATE DATABASE lorenzotest" + now + "\n"
    os.system('mysql -uroot lorenzotest' + now + ' < schema.sql')
    import src.lib.queries.connection as connection
    connection.initialize()

def get_output(cmd):
    all_data = bot.privmsg(REG_USER, "#" + MOD_USER, cmd)
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(REG_USER, MOD_USER))
    return data


def get_mod_output(cmd):
    all_data = bot.privmsg(MOD_USER, "#" + MOD_USER, cmd)
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(MOD_USER, MOD_USER))
    return data


def tearDownModule():
    os.system("mysql -uroot -e \"DROP DATABASE lorenzotest" + now + "\"")
    print "\nDROP DATABASE lorenzotest" + now + "\n"


def simulate_message(sender, message):
    bot.transport.write(":{user}!{user}@{user}.tmi.twitch.tv PRIVMSG {chan} \
:{line}\r\n".format(user=sender, chan=TEST_CHAN, line=message))


def alt_simulate_message(sender, message):
    bot.transport.write(":{user}!{user}@{user}.tmi.twitch.tv PRIVMSG {chan} \
:{line}\r\n".format(user=sender, chan=TEST_CHAN, line=message))


class TestCommands(TestCase):

    def test_help_command(self):
        commands = get_output('!help')
        self.assertIn("list", commands)


class TestTreats(TestCase):

    def test_normal_cant_add_treats(self):
        output = get_output("!treats set {reg_user} 1000".format(
            reg_user=REG_USER))
        self.assertIn("This is a moderator-only command!", output)

    def test_mod_can_add_treats(self):
        before = get_mod_output("!treats set {reg_user} 0".format(
            reg_user=REG_USER))

        get_mod_output("!treats add {reg_user} 1000".format(
            reg_user=REG_USER))  # ignore the bot response

        after = get_output("!llama treats")
        print after
        self.assertNotEqual(before, after)

    def test_treats_list(self):
        get_mod_output("!treats add {mod_user} 5000".format(
            mod_user=MOD_USER))  # ignore the bot response

        get_mod_output("!treats add {reg_user} 1000".format(
            reg_user=REG_USER))  # ignore the bot response

        treats_list = get_output("!llama list")
        self.assertIn("|", treats_list)


class TestShots(TestCase):

    def test_add_shots_normal_user(self):
        simulate_message(REG_USER, "!shots set 10000")
        resp = get_output(cmd)
        self.assertIn("moderator-only", resp)

    def test_add_shots_mod(self):
        simulate_message(REG_USER, "!llama shots")
        before = get_output(cmd)

        simulate_message(MOD_USER, "!shots add 1")
        get_output(cmd)

        simulate_message(REG_USER, "!llama shots")
        after = get_output(cmd)

        simulate_message(MOD_USER, "!shots set 0")
        get_output(cmd)
        self.assertNotEqual(before, after)


class TestPokemon(TestCase):

    def test_release_pokemon(self):
        globals.CHANNEL_INFO[TEST_CHAN]["caught"] = False
        globals.CHANNEL_INFO[TEST_CHAN]["pokemon"] = "Bulbasaur"
        self.assertEqual(globals.CHANNEL_INFO[TEST_CHAN]["caught"], False)
        self.assertEqual(globals.CHANNEL_INFO[TEST_CHAN][
            "pokemon"], "Bulbasaur")

    def test_user_catch_pokemon(self):
        simulate_message(REG_USER, "!catch")
        caught = get_output(cmd)
        self.assertIn("was caught", caught)

    def test_normal_cant_gift_pokemon(self):
        simulate_message(REG_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("moderator-only", resp)

    def test_mod_can_gift_pokemon(self):
        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("was caught", resp)

        simulate_message(REG_USER, "!party members")
        party = get_output(cmd)
        self.assertIn("lvl", party)

        simulate_message(REG_USER, "!party 1")
        party = get_output(cmd)
        self.assertIn("lvl", party)

        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        released = get_output(cmd)
        self.assertIn("Released", released)

    def test_party_full(self):
        for i in range(6):
            simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
                reg_user=REG_USER))
            get_output(cmd)

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        party_full = get_output(cmd)
        self.assertIn("No open slots", party_full)

        for i in range(6):
            simulate_message(REG_USER, "!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))
            get_output(cmd)

    def test_tallgrass(self):
        simulate_message(MOD_USER, "!treats add {reg_user} 1000".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(REG_USER, "!llama {reg_user}".format(
            reg_user=REG_USER))
        treats = get_output(cmd)
        self.assertIn(" 1000", treats)

        simulate_message(REG_USER, "!tallgrass 1000".format(
            reg_user=REG_USER))
        released = get_output(cmd)
        self.assertIn("appeared", released)

        simulate_message(REG_USER, "!llama {reg_user}".format(
            reg_user=REG_USER))
        treats = get_output(cmd)
        self.assertIn(" 0", treats)

        simulate_message(REG_USER, "!tallgrass 1000".format(
            reg_user=REG_USER))
        released = get_output(cmd)
        self.assertIn("need more treats", released)

    def test_battle(self):
        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!treats add {mod_user} 0".format(
            mod_user=MOD_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!treats add {alt_user} 0".format(
            alt_user=ALT_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!treats add {test_chan} 0".format(
            test_chan=TEST_CHAN))
        get_output(cmd)

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!gift {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!gift {test_chan} Charmander 10".format(
            test_chan=TEST_CHAN))
        get_output(cmd)

        simulate_message(MOD_USER, "!battle 1 {mod_user}".format(
            mod_user=MOD_USER))
        results = get_output(cmd)
        self.assertIn("You can't battle yourself", results)

        simulate_message(REG_USER, "!battle 1 {alt_user}".format(
            alt_user=ALT_USER))
        results = get_output(cmd)
        self.assertIn("Your opponent must be in this channel", results)

        simulate_message(MOD_USER, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = get_output(cmd)
        self.assertIn("draw", results)

        simulate_message(TEST_CHAN, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = get_output(cmd)
        self.assertNotIn("was", results)

        simulate_message(MOD_USER, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = get_output(cmd)
        self.assertIn("heal", results)

        simulate_message(MOD_USER, "!release 1 {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))
        get_output(cmd)

        simulate_message(TEST_CHAN, "!release 1 {test_chan} Bulbasaur 10".format(
            test_chan=TEST_CHAN))
        get_output(cmd)

        simulate_message(REG_USER, "!release 1 {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        get_output(cmd)


class TestDonation(TestCase):

    def test_normal_cant_add_donation(self):
        simulate_message(REG_USER, "!donation {reg_user} 10".format(
            reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("moderator-only", resp)

    def test_mod_can_add_donation(self):
        simulate_message(MOD_USER, "!donation {reg_user} 10".format(
            reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("donation", resp)

        simulate_message(MOD_USER, "!treats set {reg_user} 0".format(
            reg_user=REG_USER))
        get_output(cmd)


class TestSubscriberNotifications(TestCase):

    def test_first_time_subscriber(self):
        simulate_message("twitchnotify", "{reg_user} just subscribed".format(
            reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("first time subscription", resp)

    def test_repeast_subscriber(self):
        simulate_message("twitchnotify", "{reg_user} subscribed for 7 months \
in a row".format(reg_user=REG_USER))
        resp = get_output(cmd)
        self.assertIn("months straight", resp)


class TestCustomCommands(TestCase):

    def test_custom_commands(self):
        test_message = "Test Message"
        simulate_message(MOD_USER, "!add !testcommand1 mod {test_message} []{{}}".format(
            test_message=test_message))
        added = get_output(cmd)
        self.assertIn("successfully added", added)

        simulate_message(MOD_USER, "!add !testcommand2 reg {test_message}".format(
            test_message=test_message))
        get_output(cmd)

        simulate_message(MOD_USER, "!testcommand1")
        message = get_output(cmd)
        self.assertIn(test_message, message)

        simulate_message(MOD_USER, "!add !test reg {test_message}".format(
            test_message=test_message))
        added = get_output(cmd)
        self.assertIn("already built in", added)

        simulate_message(MOD_USER, "!testcommand1")
        message = get_output(cmd)
        self.assertIn(test_message, message)

        simulate_message(REG_USER, "!testcommand2")
        message = get_output(cmd)
        self.assertIn(test_message, message)

        simulate_message(MOD_USER, "!rem !testcommand1")
        removed = get_output(cmd)
        self.assertIn("successfully removed", removed)

        simulate_message(MOD_USER, "!rem !testcommand2")
        get_output(cmd)


class TestItems(TestCase):

    def test_mod_can_gift_items(self):
        simulate_message(MOD_USER, "!gift {reg_user} item 11".format(
            reg_user=REG_USER))
        successful = get_output(cmd)
        self.assertIn("Gift successful", successful)

        simulate_message(REG_USER, "!check inventory")
        inventory = get_output(cmd)
        self.assertIn("(11) Rare Candy, 1", inventory)

    def test_user_can_check_items(self):
        simulate_message(REG_USER, "!check items")
        items = get_output(cmd)
        self.assertIn("""(1) Fire Stone, 750 | (2) Water Stone, 750 | (3) \
Thunder Stone, 750 | (4) Leaf Stone, 750 | (5) Moon Stone, 750 | (11) \
Rare Candy, 1000""", items)

    def test_user_can_use_items(self):
        for i in range(6):
            simulate_message(REG_USER, "!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))
            get_output(cmd)

        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        get_output(cmd)

        simulate_message(REG_USER, "!party 1".format(
            reg_user=REG_USER))
        before = get_output(cmd)

        simulate_message(REG_USER, "!use 11 1")
        inventory = get_output(cmd)
        self.assertIn("LEVEL UP", inventory)

        simulate_message(REG_USER, "!party 1".format(
            reg_user=REG_USER))
        after = get_output(cmd)
        self.assertNotEqual(before, after)

        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        get_output(cmd)


class TestQuotes(TestCase):

    def test_moderator_can_add_quote(self):
        def random_word(length=201):
            return ''.join(random.choice(
                string.lowercase) for i in range(length))
        if API:
            simulate_message(REG_USER, "!quote")
            resp = get_output(cmd)
            self.assertIn("No quotes found", resp)

            quote = random_word()
            simulate_message(TEST_CHAN, "!addquote {quote}".format(
                quote=random_word()))
            resp = server.get_output(timeout=2)
            self.assertIn("Let's keep it below 200 characters?", resp)

            quote = "HeyGuys Kappa"
            simulate_message(MOD_USER, "!addquote {quote}".format(
                quote=quote))
            resp = server.get_output(timeout=2)
            self.assertIn(quote, resp)

            simulate_message(MOD_USER, "!quote")
            resp = get_output(cmd)
            self.assertIn(quote, resp)


class TestWeather(TestCase):

    def test_weather(self):
        if API:
            simulate_message(MOD_USER, "!weather Moscow, Russia")
            resp = get_output(cmd)
            self.assertIn("You must specify 'imperial' or 'metric'", resp)

            simulate_message(MOD_USER, "!weather imperial Moscow, Russia")
            resp = server.get_output(timeout=2)
            self.assertIn("neat", resp)
