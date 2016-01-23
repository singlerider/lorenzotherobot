import threading
import unittest

import src.lib.commands.pokemon as pokemon
import src.lib.functions_commands
from bot import Roboraj
from testing.TwitchIrc import (
    TwitchIrc, MOD_USER, REG_USER,TEST_CHANNEL, TEST_CHAN, USERS)


# Replace the get_dict_for_users function with something that returns
# the right users.
src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None

server, client = None, None


def setUpModule():
    global server, client
    server = TwitchIrc()
    client = Roboraj({
        "server": "localhost",
        "port": server.getPort(),
        "username": "test_username",
        "oauth_password": "test_oauth",
        "channels": [TEST_CHANNEL],
    })
    threading.Thread(target=client.run).start()

    server.getOutput()  # User
    server.getOutput()  # Pass
    server.getOutput()  # Nick
    server.getOutput()  # Join


def tearDownModule():
    server.stop()


def simulateMessage(sender, message):
    # defaults to the TEST_CHANNEL since that's the only one we use.
    server.simulateMessage(sender, TEST_CHANNEL, message)


class TestCommands(unittest.TestCase):

    def test_simple_commands(self):
        import src.lib.command_headers as cmds
        for cmd, desc in cmds.commands.items():
            if desc['return'] != 'command':
                # non 'command's are strings we expect to see sent.

                # fire the command
                simulateMessage(REG_USER, cmd)

                # get output
                out = server.getOutput()
                expected = "PRIVMSG {chan} :({user}) : {msg}".format(
                    chan=TEST_CHANNEL, user=REG_USER, msg=desc['return'].encode('utf-8'))

                # validate
                self.assertEqual(out, expected)


class TestTreats(unittest.TestCase):

    def test_normal_cant_add_treats(self):
        simulateMessage(REG_USER, "!treats set {reg_user} 1000".format(
            reg_user=REG_USER))
        output = server.getOutput()
        self.assertIn("This is a moderator-only command!", output)

    def test_mod_can_add_treats(self):
        simulateMessage(MOD_USER, "!treats set {reg_user} 0".format(
            reg_user=REG_USER))
        server.getOutput()  # ignore the bot response
        simulateMessage(REG_USER, "!llama treats")
        server.getOutput()
        simulateMessage(MOD_USER, "!treats add {reg_user} 1000".format(
            reg_user=REG_USER))
        server.getOutput()  # ignore the bot response
        simulateMessage(REG_USER, "!llama treats")
        self.assertNotEqual("This is a moderator-only command!", server.getOutput())


class TestShots(unittest.TestCase):

    def test_add_shots_normal_user(self):
        simulateMessage(REG_USER, "!shots set 10000")
        self.assertIn("moderator-only", server.getOutput())

    def test_add_shots_mod(self):
        simulateMessage(REG_USER, "!llama shots")
        before = server.getOutput()
        simulateMessage(MOD_USER, "!shots add 1")
        server.getOutput()
        simulateMessage(REG_USER, "!llama shots")
        after = server.getOutput()
        simulateMessage(MOD_USER, "!shots set 0")
        server.getOutput()
        self.assertNotEqual(before, after)
