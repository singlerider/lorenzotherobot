import threading
import unittest

import src.lib.commands.pokemon as pokemon
import src.lib.functions_commands
from src.lib.twitch import get_dict_for_users
from bot import Roboraj
from testing.TwitchIrc import TwitchIrc

TEST_CHANNEL = "#theepicsnail_"


# Replace the get_dict_for_users function with something that returns
# the right users.


def get_dict_for_users(a=None):
    return {'chatters':
            {'moderators': ["theepicsnail_", "singlerider"],
             'global_mods': [],
             'admins': [],
             'viewers': ["randomUser"],
             'staff': []
             },
            '_links': {},
            'chatter_count': 3},
    ["theepicsnail_", "singlerider", "randomUser"]

print get_dict_for_users()

src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None

server, client = None, None


def setUpModule():
    global server, client
    server = TwitchIrc()
    client = Roboraj({
        "server": "localhost",
        "port": server.getPort(),
        "username": "testUsername",
        "oauth_password": "testOauth",
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
                simulateMessage("randomUser", cmd)

                # get output
                out = server.getOutput()
                expected = "PRIVMSG {chan} :({user}) : {msg}".format(
                    chan=TEST_CHANNEL, user="randomUser", msg=desc['return'].encode('utf-8'))

                # validate
                self.assertEqual(out, expected)


class TestTreats(unittest.TestCase):

    def test_normal_cant_add_treats(self):
        simulateMessage("randomUser", "!treats set randomUser 1000")
        self.assertIn("This is a moderator-only command!", server.getOutput())

    def test_mod_can_add_treats(self):
        # singlerider has permission to add treats but theepicsnail_ doesnt, even in '#theepicsnail_'
        # this is weird.
        simulateMessage("randomUser", "!llama treats")

        # position 10 is where the number of treats are.
        old_treats = int(server.getOutput().split(" ")[10])

        simulateMessage("singlerider", "!treats add randomUser 1000")
        server.getOutput()  # ignore the bot response
        print "server.getOutput()", server.getOutput()

        simulateMessage("randomUser", "!llama treats")
        new_treats = int(server.getOutput().split(" ")[10])

        print old_treats, new_treats

        self.assertEqual(old_treats + 1000, new_treats)


class TestShots(unittest.TestCase):

    def test_add_shots_normal_user(self):
        simulateMessage("randomUser", "!shots add 10000")
        self.assertIn("moderator-only", server.getOutput())

    def test_add_shots_mod(self):
        simulateMessage("randomUser", "!llama shots")
        before = server.getOutput()
        simulateMessage("singlerider", "!shots add 1")
        server.getOutput()
        simulateMessage("randomUser", "!llama shots")
        after = server.getOutput()
        self.assertNotEqual(before, after)
