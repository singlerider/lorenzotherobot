from testing.TwitchIrc import TwitchIrc
import unittest
import threading
from bot import Roboraj


# Replace the get_dict_for_users function with something that returns
# the right users.
import src.lib.commands.llama as llama
llama.get_dict_for_users = lambda: (
    {'chatters':
        {'moderators': ["theepicsnail"],
        'global_mods': [],
        'admins': [],
        'viewers': [],
        'staff': []
        },
    '_links': {},
    'chatter_count': 0},
    ['', ''])



class TestCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = TwitchIrc()
        cls.client = Roboraj({
            "server": "localhost",
            "port": cls.server.getPort(),
            "username": "testUsername",
            "oauth_password": "testOauth",
            "channels": ["#theepicsnail"],
            "cron":[],
        })
        threading.Thread(target=cls.client.run).start()

        cls.server.getOutput() #User
        cls.server.getOutput() #Pass
        cls.server.getOutput() #Nick
        cls.server.getOutput() #Join


    @classmethod
    def tearDownClass(cls):
        cls.server.stop()

    def test_simple_commands(self):
        import src.lib.command_headers as cmds
        for cmd, desc in cmds.commands.items():
            if desc['return'] != 'command':
                self.server.simulateMessage("randomUser", "#theepicsnail", cmd)
                out = self.server.getOutput()
                expected = "PRIVMSG {chan} :({user}) : {msg}".format(
                    chan = "#theepicsnail", user="randomUser", msg=desc['return'].encode('utf-8'))

                self.assertEqual(out, expected)

    def test_pokemon_capture(self):
        pass
