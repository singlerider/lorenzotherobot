import os
import random
import string
import time
from datetime import datetime, timedelta
from unittest import TestCase

import globals
import src.bot as bot_import
import src.lib.functions_commands
from mock import Mock, patch
from src.bot import BotFactory
from testing.TwitchIrc import (ALT_USER, MOD_USER, REG_USER, TEST_CHAN,
                               TEST_CHANNEL, USERS)
from twisted.test import proto_helpers

mock_time = Mock()


def add_time():
    if type(mock_time.return_value) != float:
        mock_time.return_value = time.mktime(datetime.now().timetuple())
    else:
        mock_time.return_value = time.time() + 600


API = False

src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None
server, client = None, None

now = str(time.time()).replace(".", "")

_channel = TEST_CHANNEL
_username = MOD_USER
_us = 'tbb'


@patch('time.time', mock_time)
def setUpModule():
    global bot, whisper, client, fake_transport
    factory = BotFactory("chat")
    whisper_factory = BotFactory("whisper")
    bot = factory.buildProtocol(('127.0.0.1', 0))
    whisper = whisper_factory.buildProtocol(('127.0.0.1', 9999))
    fake_transport = proto_helpers.StringTransport()
    bot.makeConnection(fake_transport)
    bot.signedOn()
    bot.joined(_channel)
    fake_transport.clear()
    os.system("mysql -uroot -e \"CREATE DATABASE lorenzotest\"")
    globals.mysql_credentials = ['localhost', 'root', '', 'lorenzotest']
    print globals.mysql_credentials
    print "\"CREATE DATABASE lorenzotest"
    os.system('mysql -uroot lorenzotest < schema.sql')
    import src.lib.queries.connection as connection
    connection.initialize()
    bot_import.ECHOERS = {"whisper": whisper, "chat": bot}
    globals.CHANNEL_INFO[MOD_USER]['viewers'] = USERS
    add_time()


@patch('time.time', mock_time)
def get_output(cmd):
    str(bot.privmsg(REG_USER, "#" + MOD_USER, str(cmd)))
    all_data = str(fake_transport.value())
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(REG_USER, MOD_USER))
    print data
    fake_transport.clear()
    add_time()
    return data


@patch('time.time', mock_time)
def get_mod_output(cmd):
    bot.privmsg(MOD_USER, "#" + MOD_USER, cmd)
    all_data = fake_transport.value()
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(MOD_USER, MOD_USER))
    print data
    fake_transport.clear()
    add_time()
    return data


def get_specific_output(user, cmd):
    bot.privmsg(user, "#" + MOD_USER, cmd)
    all_data = fake_transport.value()
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(user, MOD_USER))
    print data
    fake_transport.clear()
    add_time()
    return data


def get_whisper_output(cmd):
    whisper.whisper(MOD_USER, "#" + MOD_USER, cmd)
    #sender = "{user}!{user}@{user}.tmi.twitch.tv".format(user=BOT_USER)
    #line = ":%s PRIVMSG #jtv :/w %s %s" % (sender, channel, resp)
    all_data = fake_transport.value()
    data = all_data.lstrip(':{0}!{0}@{0}.tmi.twitch.tv PRIVMSG {1} :'.format(MOD_USER, MOD_USER))
    print data
    fake_transport.clear()
    add_time()
    return data


def tearDownModule():
    os.system("mysql -uroot -e \"DROP DATABASE lorenzotest\"")
    print "\nDROP DATABASE lorenzotest"


class TestCommands(TestCase):

    def test_help_command(self):
        commands = get_output('!help')
        self.assertIn("useful", commands)


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

        after = get_whisper_output("!llama treats")
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
        resp = get_output("!shots set 10000")
        self.assertIn("moderator-only", resp)

    def test_add_shots_mod(self):
        before = get_output("!llama shots")

        get_mod_output("!shots add 1")

        after = get_output("!llama shots")

        get_mod_output("!shots set 0")
        self.assertNotEqual(before, after)


class TestPokemon(TestCase):
    globals.CHANNEL_INFO[TEST_CHAN]["caught"] = False
    globals.CHANNEL_INFO[TEST_CHAN]["pokemon"] = "Bulbasaur"

    def test_release_pokemon(self):
        self.assertEqual(globals.CHANNEL_INFO[TEST_CHAN]["caught"], False)
        self.assertEqual(globals.CHANNEL_INFO[TEST_CHAN][
            "pokemon"], "Bulbasaur")

    def test_user_catch_pokemon(self):
        caught = get_output("!catch")
        self.assertIn("was caught", caught)

    def test_normal_cant_gift_pokemon(self):
        resp = get_output("!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        self.assertIn("moderator-only", resp)

    def test_mod_can_gift_pokemon(self):
        get_output("!release 1 {reg_user}".format(
            reg_user=REG_USER))

        get_mod_output("!treats add {reg_user} 0".format(
            reg_user=REG_USER))

        resp = get_mod_output("!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        self.assertIn("was caught", resp)

        party = get_output("!party members")
        self.assertIn("lvl", party)

        party = get_output("!party 1")
        self.assertIn("lvl", party)

        released = get_output("!release 1 {reg_user}".format(
            reg_user=REG_USER))
        self.assertIn("Released", released)

    def test_party_full(self):
        for i in range(6):
            get_mod_output("!gift {reg_user} Bulbasaur 10".format(
                reg_user=REG_USER))

        party_full = get_mod_output("!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        self.assertIn("No open slots", party_full)

        for i in range(6):
            get_output("!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))

    def test_tallgrass(self):
        get_mod_output("!treats set {reg_user} 1000".format(
            reg_user=REG_USER))

        treats = get_output("!llama {reg_user}".format(
            reg_user=REG_USER))
        self.assertIn(" 1000", treats)

        released = get_output("!tallgrass 1000".format(
            reg_user=REG_USER))
        self.assertIn("appeared", released)

        treats = get_output("!llama {reg_user}".format(
            reg_user=REG_USER))
        self.assertIn(" 0", treats)

        released = get_output("!tallgrass 1000".format(
            reg_user=REG_USER))
        self.assertIn("need more treats", released)

    def test_battle(self):
        get_mod_output("!treats add {reg_user} 0".format(
            reg_user=REG_USER))

        get_mod_output("!treats add {mod_user} 0".format(
            mod_user=MOD_USER))

        get_mod_output("!treats add {alt_user} 0".format(
            alt_user=ALT_USER))

        get_mod_output("!treats add {test_chan} 0".format(
            test_chan=TEST_CHAN))

        get_mod_output("!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))

        get_mod_output("!gift {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))

        get_mod_output("!gift {test_chan} Charmander 10".format(
            test_chan=TEST_CHAN))

        results = get_mod_output("!battle 1 {mod_user}".format(
            mod_user=MOD_USER))
        self.assertIn("You can't battle yourself", results)

        results = get_output("!battle 1 {alt_user}".format(
            alt_user=ALT_USER))
        self.assertIn("Your opponent must be in this channel", results)

        results = get_mod_output("!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        self.assertIn("draw", results)

        results = get_specific_output(TEST_CHAN, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        self.assertNotIn("was", results)

        results = get_mod_output("!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        self.assertIn("heal", results)

        get_mod_output("!release 1 {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))

        get_specific_output(TEST_CHAN, "!release 1 {test_chan} Bulbasaur 10".format(
            test_chan=TEST_CHAN))

        get_output("!release 1 {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))


class TestDonation(TestCase):

    def test_normal_cant_add_donation(self):
        resp = get_output("!donation {reg_user} 10".format(
            reg_user=REG_USER))
        self.assertIn("moderator-only", resp)

    def test_mod_can_add_donation(self):
        resp = get_mod_output("!donation {reg_user} 10".format(
            reg_user=REG_USER))
        self.assertIn("donation", resp)

        get_output("!treats set {reg_user} 0".format(
            reg_user=REG_USER))


class TestSubscriberNotifications(TestCase):

    def test_first_time_subscriber(self):
        resp = get_specific_output("twitchnotify", "{reg_user} just subscribed".format(
            reg_user=REG_USER))
        self.assertIn("first time subscription", resp)

    def test_repeat_subscriber(self):
        resp = get_specific_output("twitchnotify", "{reg_user} subscribed for 7 months \
in a row".format(reg_user=REG_USER))
        self.assertIn("months straight", resp)


class TestCustomCommands(TestCase):

    def test_custom_commands(self):
        test_message = "Test Message"
        added = get_mod_output("!add !testcommand1 mod {test_message} []{{}}".format(
            test_message=test_message))
        self.assertIn("successfully added", added)

        get_mod_output("!add !testcommand2 reg {test_message}".format(
            test_message=test_message))

        message = get_mod_output("!testcommand1")
        self.assertIn(test_message, message)

        added = get_mod_output("!add !test reg {test_message}".format(
            test_message=test_message))
        self.assertIn("already built in", added)

        message = get_mod_output("!testcommand1")
        self.assertIn(test_message, message)

        message = get_output("!testcommand2")
        self.assertIn(test_message, message)

        removed = get_mod_output("!rem !testcommand1")
        self.assertIn("successfully removed", removed)

        get_mod_output("!rem !testcommand2")


class TestItems(TestCase):

    def test_mod_can_gift_items(self):
        successful = get_mod_output("!gift {reg_user} item 11".format(
            reg_user=REG_USER))
        self.assertIn("Gift successful", successful)

        inventory = get_output("!check inventory")
        self.assertIn("(11) Rare Candy, 1", inventory)

    def test_user_can_check_items(self):
        items = get_output("!check items")
        self.assertIn("""(1) Fire Stone, 750 | (2) Water Stone, 750 | (3) \
Thunder Stone, 750 | (4) Leaf Stone, 750 | (5) Moon Stone, 750 | (11) \
Rare Candy, 1000""", items)

    def test_user_can_use_items(self):
        for i in range(6):
            get_output("!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))

        get_mod_output("!treats add {reg_user} 0".format(
            reg_user=REG_USER))

        get_mod_output("!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))

        before = get_output("!party 1")

        inventory = get_output("!use 11 1")
        self.assertIn("LEVEL UP", inventory)

        after = get_output("!party 1")
        self.assertNotEqual(before, after)

        get_output("!release 1 {reg_user}".format(
            reg_user=REG_USER))


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
