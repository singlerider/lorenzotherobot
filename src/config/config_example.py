global config

import src.lib.commands.pokemon as pokemon
import src.lib.commands.treats as treats

config = {
    # details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'YourUsername',
    'oauth_password': 'YourOauthToken',# get this from http://twitchapps.com/tmi/

    'debug': True,
    'log_messages': True,

    # channel to join
    'channels': ['#lorenzotherobot'],

    # Cron jobs.
    'cron': {
        '#lorenzotherobot': [
            #time, run, callback
            (120, True, pokemon.cron), # pokemon released every 2 minutes
            (300, True, treats.cron), # treat handed out every 5 minutes
        ],
    },
}
