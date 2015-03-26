from testing.TwitchIrc import TwitchIrc
import unittest
import threading
from bot import Roboraj

import src.lib.functions_commands
src.lib.functions_commands.is_on_cooldown = lambda cmd, chn: None

TEST_CHANNEL = "#theepicsnail"

# Replace the get_dict_for_users function with something that returns
# the right users.
import src.lib.commands.llama as llama
llama.get_dict_for_users = lambda: (
    {'chatters':
        {'moderators': ["theepicsnail_", "singlerider"],
        'global_mods': [],
        'admins': [],
        'viewers': [],
        'staff': []
        },
    '_links': {},
    'chatter_count': 0},
    ['', ''])


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
        "cron":[],
    })
    threading.Thread(target=client.run).start()

    server.getOutput() #User
    server.getOutput() #Pass
    server.getOutput() #Nick
    server.getOutput() #Join


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
                    chan = "#theepicsnail", user="randomUser", msg=desc['return'].encode('utf-8'))

                # validate
                self.assertEqual(out, expected)


import src.lib.commands.pokemon as pokemon_lib
class TestPokemon(unittest.TestCase):
    def setUp(self):
        # Save a copy of the methods we (possibly) modify
        self.initials = {
            "randomPokemon": pokemon_lib.randomPokemon
        }
    def tearDown(self):
        for name, val in self.initials.items():
            setattr(pokemon_lib, name, val) # Restore each.
    def test_pokemon_battle(self):
        # These tests don't have any sensible asserts, but do exercise the code.
        # if the code is broken these tests should crash

        # bulbasaur vs ivysaur, they both have mods.
        pokemon_lib.randomPokemon = ["Bulbasaur", "Ivysaur"].pop
        simulateMessage("randomUser", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        # neither affects the other.
        pokemon_lib.randomPokemon = ["Bulbasaur", "Missingno"].pop
        simulateMessage("randomUser", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        # both first and second has a mod while the other doesn't
        pokemon_lib.randomPokemon = ["Omastar", "Golbat"].pop
        simulateMessage("randomUser", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        pokemon_lib.randomPokemon = ["Golbat", "Omastar"].pop
        simulateMessage("randomUser", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

    def test_capture_and_me(self):
        simulateMessage("randomUser", "!pokemon me")
        original = server.getOutput()

        simulateMessage("randomUser", "!capture")
        self.assertIn("Somebody else beat you to it", server.getOutput())
        # release a pokemon
        pokemon = pokemon_lib.cron()[7:-10]

        simulateMessage("randomUser", "!capture")
        self.assertIn("caught it", server.getOutput())

        simulateMessage("randomUser", "!pokemon me")
        self.assertNotEqual(original, server.getOutput(), "Pokemon didn't change")


class TestTreats(unittest.TestCase):
    def test_normal_cant_add_treats(self):
      simulateMessage("randomUser", "!treats set randomUser 1000")
      self.assertIn("This is a moderator-only command!", server.getOutput())

    def test_mod_can_add_treats(self):
      #singlerider has permission to add treats but theepicsnail doesnt, even in '#theepicsnail'
      #this is weird.
      simulateMessage("randomUser", "!llama treats")

      # position 10 is where the number of treats are.
      old_treats = int(server.getOutput().split(" ")[10])

      simulateMessage("singlerider", "!treats add randomUser 1000")
      server.getOutput() # ignore the bot response

      simulateMessage("randomUser",  "!llama treats")
      new_treats = int(server.getOutput().split(" ")[10])

      self.assertEqual(old_treats + 1000, new_treats)
