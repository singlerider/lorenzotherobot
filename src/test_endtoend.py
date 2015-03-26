from testing.TwitchIrc import TwitchIrc
import unittest
import threading
from bot import Roboraj


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
        "channels": ["#theepicsnail"],
        "cron":[],
    })
    threading.Thread(target=client.run).start()

    server.getOutput() #User
    server.getOutput() #Pass
    server.getOutput() #Nick
    server.getOutput() #Join

def tearDownModule():
    server.stop()

class TestCommands(unittest.TestCase):
    def test_simple_commands(self):
        import src.lib.command_headers as cmds
        for cmd, desc in cmds.commands.items():
            if desc['return'] != 'command':
                # non 'command's are strings we expect to see sent.

                # fire the command
                server.simulateMessage("randomUser", "#theepicsnail", cmd)

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
        server.simulateMessage("randomUser", "#theepicsnail", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        # neither affects the other.
        pokemon_lib.randomPokemon = ["Bulbasaur", "Missingno"].pop
        server.simulateMessage("randomUser", "#theepicsnail", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        # both first and second has a mod while the other doesn't
        pokemon_lib.randomPokemon = ["Omastar", "Golbat"].pop
        server.simulateMessage("randomUser", "#theepicsnail", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

        pokemon_lib.randomPokemon = ["Golbat", "Omastar"].pop
        server.simulateMessage("randomUser", "#theepicsnail", "!pokemon battle")
        self.assertIn("randomUser", server.getOutput())

class TestTreats(unittest.TestCase):
    def test_normal_cant_add_treats(self):
      server.simulateMessage("randomUser", "#theepicsnail", "!treats set randomUser 1000")
      self.assertIn("This is a moderator-only command!", server.getOutput())

    def test_mod_can_add_treats(self):
      #singlerider has permission to add treats but theepicsnail doesnt, even in '#theepicsnail'
      #this is weird.
      server.simulateMessage("randomUser", "#theepicsnail", "!llama treats")

      # position 10 is where the number of treats are.
      old_treats = int(server.getOutput().split(" ")[10])

      server.simulateMessage("singlerider", "#theepicsnail", "!treats add randomUser 1000")
      server.getOutput()

      server.simulateMessage("randomUser", "#theepicsnail", "!llama treats")
      new_treats = int(server.getOutput().split(" ")[10])

      self.assertEqual(old_treats + 1000, new_treats)
