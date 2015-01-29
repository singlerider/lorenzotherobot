global config

import src.lib.commands as commands
import src.lib.commands.pokemon as pokemon_import
import random

def test_cron(a):
    pocket_monster = [x[0] for x in pokemon_import.master_pokemon]
    monster = random.choice(pocket_monster)
    return "A wild " + monster + " appeared!"

def test_cronb():
    return "cronb - from the return yeah"


config = {
        
        # details required to login to twitch IRC server
        'server': 'irc.twitch.tv',
        'port': 6667,
        'username': 'username',
        'oauth_password': 'oauth:abcdefghijklmnop', # get this from http://twitchapps.com/tmi/
        
        # channel to join
        'channels': ['#channel1', '#channel2'],

        # if set to true will display any data received
        'debug': False,

        # To run cron_functions, pass in a tuple (function_without_parans,(arg0,arg1,arg2,arg3))  
        
            'user_groups':
        {
        'admin':
                {
            'username': [
                'channel_admin_username1',
                'channel_admin_username2'
            ]
                },
        'mod':
                {
            'username': [
                'channel_mod_username1',
                'channel_mod_username2'
            ]
                }
        },
        
        'cron': {
                '#channel1': {
                        'run_cron': True,      # set this to false if you want don't want to run the cronjob but you want to preserve the messages etc
                        'run_time': 600,			# time in seconds
                        'cron_functions': [
								#Example syntax for function running
                                (test_cron,(pokemon_import.master_pokemon,)),
                                #(test_cronb,()),
                        ]
                },
				
				#If you'd like seaparate cron_jobs to run on the same channel, just put the same channel name below as above
				
                '#channel2': {
                        'run_cron': False,
                        'run_time': 20,
                        'cron_messages': [
                                'This is channel_two cron message one.'
                        ]
                }
        },

        # if set to true will display any data received
        'debug': True,

        # if set to true will log all messages from all channels
        # todo
        'log_messages': True,

        # maximum amount of bytes to receive from socket - 1024-4096 recommended
        'socket_buffer_size': 2048
}
