global config

import src.lib.commands.pokemon as pokemon_import
import src.lib.commands.llama as llama
import random
import importlib
import globals

# Some example cron jobs.
def pokemon_cron(a):
    globals.CAUGHT = False
    pocket_monster = random.choice(pokemon_import.master_pokemon_dict.keys())
    globals.POKEMON = pocket_monster
    # text returned from a cron job goes to the channel
    return "A wild " + pocket_monster + " appeared!"


def treats_cron(a):
    if not llama.get_stream_status():
        return llama.enter_into_database()
    else:
        return "Treats are earned while Curvyllama is streaming."


config = {
    # details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'lorenzotherobot',
    'oauth_password': 'oauth:a1s2d3f4g5h6j7k8l9aassddff',

    'debug': True,
    'log_messages': True,

    # channel to join
    'channels': ['#lorenzotherobot'],


    # cron is a map of channel names to:
    # {
    #    'run_cron': True/False - Should this cron be turned on
    #    'run_time': int(seconds) - How often to run this
    #    'cron_functions': [
    #       (function, (args)),
    #       ...
    #    ]
    # }

    'cron': {
        '#lorenzotherobot':
        {
            # set this to false if you want don't want to run the
            # cronjob but you want to preserve the messages etc
            'run_cron': True,
            'run_time': 30,            # time in seconds
            'cron_functions': [
                (pokemon_cron, (pokemon_import.master_pokemon_dict,)),
                (treats_cron, ())
            ]
        },
    },
}
