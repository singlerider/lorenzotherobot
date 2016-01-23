import os
import re
import threading
from unittest import TestCase

import globals
import src.lib.commands.pokemon as pokemon
import src.lib.functions_commands
from src.bot import Roboraj
from testing.TwitchIrc import (ALT_USER, MOD_USER, REG_USER, TEST_CHAN,
                               TEST_CHANNEL, USERS, TwitchIrc)

src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None
server, client = None, None


def setUpModule():
    os.system("mysql -uroot -e \"CREATE DATABASE lorenzotest\"")
    globals.mysql_credentials = ['localhost', 'root', '', 'lorenzotest']
    print globals.mysql_credentials
    print "\n\n\n\n\nCREATE DATABASE lorenzotest\n\n\n\n\n"
    os.system('mysql -uroot lorenzotest < schema.sql')
    import src.lib.queries.connection as connection
    connection.initialize()
    global server, client
    server = TwitchIrc()
    client = Roboraj({
        "server": "localhost",
        "port": server.get_port(),
        "username": "test_username",
        "oauth_password": "test_oauth",
        "channels": [TEST_CHANNEL, "#" + ALT_USER],
    })
    threading.Thread(target=client.run).start()
    server.get_output()  # User
    server.get_output()  # Pass
    server.get_output()  # Nick
    server.get_output()  # Join


def tearDownModule():
    os.system("mysql -uroot -e \"DROP DATABASE lorenzotest\"")
    print "\n\n\n\n\nDROP DATABASE lorzenzotest\n\n\n\n\n"
    server.stop()


def simulate_message(sender, message):
    # defaults to the TEST_CHANNEL since that's the only one we use.
    server.simulate_message(sender, TEST_CHANNEL, message)


def alt_simulate_message(sender, message):
    server.simulate_message(sender, ALT_USER, message)
    globals.CURRENT_CHANNEL = ALT_USER


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

        simulate_message(REG_USER, '!winner')
        winner = server.get_output()
        self.assertTrue(re.match(r'^[a-zA-Z0-9_]', winner))


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
        simulate_message(MOD_USER, "!add !testcommand1 mod {test_message}".format(
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

        simulate_message(MOD_USER, "!rem !testcommand1")
        removed = server.get_output()
        self.assertIn("successfully removed", removed)

        simulate_message(MOD_USER, "!rem !testcommand2")
        server.get_output()
