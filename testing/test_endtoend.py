import os
import re
import threading
import time
from unittest import TestCase

import globals
import src.lib.functions_commands
from src.bot import Bot
from testing.TwitchIrc import (ALT_USER, MOD_USER, REG_USER, TEST_CHAN,
                               TEST_CHANNEL, USERS, TwitchIrc)

src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None
server, client = None, None

now = str(time.time()).replace(".", "")


def setUpModule():
    os.system("mysql -uroot -e \"CREATE DATABASE lorenzotest\"")
    globals.mysql_credentials = ['localhost', 'root', '', 'lorenzotest']
    print globals.mysql_credentials
    print "\"CREATE DATABASE lorenzotest"
    os.system('mysql -uroot lorenzotest < schema.sql')
    import src.lib.queries.connection as connection
    connection.initialize()
    global server, client
    server = TwitchIrc()
    client = Bot()
    threading.Thread(target=client.run).start()
    server.get_output()  # User
    server.get_output()  # Pass
    server.get_output()  # Nick
    server.get_output()  # Join


def tearDownModule():
    os.system("mysql -uroot -e \"DROP DATABASE lorenzotest\"")
    print "\n\n\n\n\nDROP DATABASE lorenzotest"
    server.stop()


def simulate_message(sender, message):
    server.simulate_message(sender, TEST_CHANNEL, message)


def alt_simulate_message(sender, message):
    server.simulate_message(sender, ALT_USER, message)


class TestCommands(TestCase):

    def test_simple_commands(self):
        import src.lib.command_headers as cmds
        for cmd, desc in cmds.commands.items():
            if desc['return'] != 'command':
                simulate_message(REG_USER, cmd)
                out = server.get_output()
                expected = "PRIVMSG {chan} :({user}) : {msg}".format(
                    chan=TEST_CHANNEL, user=REG_USER,
                    msg=desc['return'].encode('utf-8'))
                self.assertEqual(out, expected)

    def test_winner_command(self):
        simulate_message(REG_USER, '!winner')
        winner = server.get_output()
        self.assertTrue(re.match(r'^[a-zA-Z0-9_]', winner))

    def test_commands_command(self):
        simulate_message(REG_USER, '!commands')
        commands = server.get_output()
        self.assertIn(
            "A full list of commands can be found at " +
            "http://www.github.com/singlerider/lorenzotherobot", commands)


class TestTreats(TestCase):

    def test_normal_cant_add_treats(self):
        simulate_message(REG_USER, "!treats set {reg_user} 1000".format(
            reg_user=REG_USER))
        output = server.get_output()
        self.assertIn("This is a moderator-only command!", output)

    def test_mod_can_add_treats(self):
        simulate_message(MOD_USER, "!treats set {reg_user} 0".format(
            reg_user=REG_USER))
        server.get_output()  # ignore the bot response

        simulate_message(REG_USER, "!llama")
        before = server.get_output()

        simulate_message(MOD_USER, "!treats add {reg_user} 1000".format(
            reg_user=REG_USER))
        server.get_output()  # ignore the bot response

        simulate_message(REG_USER, "!llama treats")
        after = server.get_output()
        self.assertNotEqual(before, after)

    def test_treats_list(self):
        simulate_message(MOD_USER, "!treats add {mod_user} 5000".format(
            mod_user=MOD_USER))
        server.get_output()  # ignore the bot response

        simulate_message(MOD_USER, "!treats add {reg_user} 1000".format(
            reg_user=REG_USER))
        server.get_output()  # ignore the bot response

        simulate_message(REG_USER, "!llama list")
        treats_list = server.get_output()
        self.assertIn("|", treats_list)


class TestShots(TestCase):

    def test_add_shots_normal_user(self):
        simulate_message(REG_USER, "!shots set 10000")
        resp = server.get_output()
        self.assertIn("moderator-only", resp)

    def test_add_shots_mod(self):
        simulate_message(REG_USER, "!llama shots")
        before = server.get_output()

        simulate_message(MOD_USER, "!shots add 1")
        server.get_output()

        simulate_message(REG_USER, "!llama shots")
        after = server.get_output()

        simulate_message(MOD_USER, "!shots set 0")
        server.get_output()
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
        caught = server.get_output()
        self.assertIn("was caught", caught)

    def test_normal_cant_gift_pokemon(self):
        simulate_message(REG_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        resp = server.get_output()
        self.assertIn("moderator-only", resp)

    def test_mod_can_gift_pokemon(self):
        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        resp = server.get_output()
        self.assertIn("was caught", resp)

        simulate_message(REG_USER, "!party members")
        party = server.get_output()
        self.assertIn("lvl", party)

        simulate_message(REG_USER, "!party 1")
        party = server.get_output()
        self.assertIn("lvl", party)

        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        released = server.get_output()
        self.assertIn("Released", released)

    def test_party_full(self):
        for i in range(6):
            simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
                reg_user=REG_USER))
            server.get_output()

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        party_full = server.get_output()
        self.assertIn("No open slots", party_full)

        for i in range(6):
            simulate_message(REG_USER, "!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))
            server.get_output()

    def test_tallgrass(self):
        simulate_message(MOD_USER, "!treats add {reg_user} 1000".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(REG_USER, "!llama {reg_user}".format(
            reg_user=REG_USER))
        treats = server.get_output()
        self.assertIn(" 1000", treats)

        simulate_message(REG_USER, "!tallgrass 1000".format(
            reg_user=REG_USER))
        released = server.get_output()
        self.assertIn("appeared", released)

        simulate_message(REG_USER, "!llama {reg_user}".format(
            reg_user=REG_USER))
        treats = server.get_output()
        self.assertIn(" 0", treats)

        simulate_message(REG_USER, "!tallgrass 1000".format(
            reg_user=REG_USER))
        released = server.get_output()
        self.assertIn("need more treats", released)

    def test_battle(self):
        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(MOD_USER, "!treats add {mod_user} 0".format(
            mod_user=MOD_USER))
        server.get_output()

        simulate_message(MOD_USER, "!treats add {alt_user} 0".format(
            alt_user=ALT_USER))
        server.get_output()

        simulate_message(MOD_USER, "!treats add {test_chan} 0".format(
            test_chan=TEST_CHAN))
        server.get_output()

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(MOD_USER, "!gift {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))
        server.get_output()

        simulate_message(MOD_USER, "!gift {test_chan} Charmander 10".format(
            test_chan=TEST_CHAN))
        server.get_output()

        simulate_message(MOD_USER, "!battle 1 {mod_user}".format(
            mod_user=MOD_USER))
        results = server.get_output()
        self.assertIn("You can't battle yourself", results)

        simulate_message(REG_USER, "!battle 1 {alt_user}".format(
            alt_user=ALT_USER))
        results = server.get_output()
        self.assertIn("Your opponent must be in this channel", results)

        simulate_message(MOD_USER, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = server.get_output()
        self.assertIn("draw", results)

        simulate_message(TEST_CHAN, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = server.get_output()
        self.assertNotIn("was", results)

        simulate_message(MOD_USER, "!battle 1 {reg_user}".format(
            reg_user=REG_USER))
        results = server.get_output()
        self.assertIn("heal", results)

        simulate_message(MOD_USER, "!release 1 {mod_user} Bulbasaur 10".format(
            mod_user=MOD_USER))
        server.get_output()

        simulate_message(TEST_CHAN, "!release 1 {test_chan} Bulbasaur 10".format(
            test_chan=TEST_CHAN))
        server.get_output()

        simulate_message(REG_USER, "!release 1 {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        server.get_output()


class TestDonation(TestCase):

    def test_normal_cant_add_donation(self):
        simulate_message(REG_USER, "!donation {reg_user} 10".format(
            reg_user=REG_USER))
        resp = server.get_output()
        self.assertIn("moderator-only", resp)

    def test_mod_can_add_donation(self):
        simulate_message(MOD_USER, "!donation {reg_user} 10".format(
            reg_user=REG_USER))
        resp = server.get_output()
        self.assertIn("donation", resp)

        simulate_message(MOD_USER, "!treats set {reg_user} 0".format(
            reg_user=REG_USER))
        server.get_output()


class TestSubscriberNotifications(TestCase):

    def test_first_time_subscriber(self):
        simulate_message("twitchnotify", "{reg_user} just subscribed \
to {test_chan}".format(reg_user=REG_USER, test_chan=TEST_CHAN))
        resp = server.get_output()
        self.assertIn("first time subscription", resp)

    def test_repeast_subscriber(self):
        simulate_message("twitchnotify", "{reg_user} subscribed to {test_chan} \
for 7 months in a row".format(reg_user=REG_USER, test_chan=TEST_CHAN))
        resp = server.get_output()
        self.assertIn("months straight", resp)


class TestCustomCommands(TestCase):

    def test_custom_commands(self):
        test_message = "Test Message"
        simulate_message(MOD_USER, "!add !testcommand1 mod {test_message} []{{}}".format(
            test_message=test_message))
        added = server.get_output()
        self.assertIn("successfully added", added)

        simulate_message(MOD_USER, "!add !testcommand2 reg {test_message}".format(
            test_message=test_message))
        server.get_output()

        simulate_message(MOD_USER, "!testcommand1")
        message = server.get_output()
        self.assertIn(test_message, message)

        simulate_message(MOD_USER, "!add !test reg {test_message}".format(
            test_message=test_message))
        added = server.get_output()
        self.assertIn("already built in", added)

        simulate_message(MOD_USER, "!testcommand1")
        message = server.get_output()
        self.assertIn(test_message, message)

        simulate_message(REG_USER, "!testcommand2")
        message = server.get_output()
        self.assertIn(test_message, message)

        simulate_message(MOD_USER, "!rem !testcommand1")
        removed = server.get_output()
        self.assertIn("successfully removed", removed)

        simulate_message(MOD_USER, "!rem !testcommand2")
        server.get_output()


class TestItems(TestCase):

    def test_mod_can_gift_items(self):
        simulate_message(MOD_USER, "!gift {reg_user} item 11".format(
            reg_user=REG_USER))
        successful = server.get_output()
        self.assertIn("Gift successful", successful)

        simulate_message(REG_USER, "!check inventory")
        inventory = server.get_output()
        self.assertIn("(11) Rare Candy, 1", inventory)

    def test_user_can_check_items(self):
        simulate_message(REG_USER, "!check items")
        items = server.get_output()
        self.assertIn("""(1) Fire Stone, 750 | (2) Water Stone, 750 | (3) \
Thunder Stone, 750 | (4) Leaf Stone, 750 | (5) Moon Stone, 750 | (11) \
Rare Candy, 1000""", items)

    def test_user_can_use_items(self):
        for i in range(6):
            simulate_message(REG_USER, "!release {position} {reg_user}".format(
                position=i + 1, reg_user=REG_USER))
            server.get_output()

        simulate_message(MOD_USER, "!treats add {reg_user} 0".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(MOD_USER, "!gift {reg_user} Bulbasaur 10".format(
            reg_user=REG_USER))
        server.get_output()

        simulate_message(REG_USER, "!party 1".format(
            reg_user=REG_USER))
        before = server.get_output()

        simulate_message(REG_USER, "!use 11 1")
        inventory = server.get_output()
        self.assertIn("LEVEL UP", inventory)

        simulate_message(REG_USER, "!party 1".format(
            reg_user=REG_USER))
        after = server.get_output()
        self.assertNotEqual(before, after)

        simulate_message(REG_USER, "!release 1 {reg_user}".format(
            reg_user=REG_USER))
        server.get_output()
