global config

import src.lib.commands.pokemon as pokemon_import
import src.lib.commands.llama as llama
import random
import importlib

def pokemon_cron(a):
    pocket_monster = [x[0] for x in pokemon_import.master_pokemon]
    monster = random.choice(pocket_monster)
    return "A wild " + monster + " appeared!"
    
def treats_cron(a):
    if not llama.get_stream_status():
        try:
            return llama.enter_into_database()
        except:
            return "Error"
    else:
        return "Treats are earned while Curvyllama is streaming."
        


config = {
        
        # details required to login to twitch IRC server
        'server': 'irc.twitch.tv',
        'port': 6667,
        'username': 'usernamegoeshere',
        'oauth_password': 'oauth:klajsdkljasdaslkjdlkasjdkas', # get this from http://twitchapps.com/tmi/
        
        # channel to join
        'channels': ['#lorenzotherobot'],

        # if set to true will display any data received
        'debug': True,

        # To run cron_functions, pass in a tuple (function_without_params,(arg0,arg1,arg2,arg3))  
        

        
        'cron': {
                '#lorenzotherobot':
                {
                        'run_cron': True,      # set this to false if you want don't want to run the cronjob but you want to preserve the messages etc
                        'run_time': 2,            # time in seconds
                        'cron_functions': [
                                (pokemon_cron,(pokemon_import.master_pokemon,)),
                                 (treats_cron, ())
                        ]#,
                        #'cron_secondary': [
                        #        (test_cron,(pokemon_import.master_pokemon,)),
                        #         (test_cronb, ())
                        #]
                },

#                '#curvyllama':{
#                        'run_cron': False,
#                        'run_time': 300,
#                        'cron_messages': [
#                                'This is channel_two cron message one.'
#                        ]
#                },
        },

        # if set to true will display any data received
        'debug': True,

        # if set to true will log all messages from all channels
        # todo
        'log_messages': True,

        # maximum amount of bytes to receive from socket - 1024-4096 recommended
        'socket_buffer_size': 2048
}
