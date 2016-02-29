global config

import globals
import src.lib.commands.pokemon as pokemon
import src.lib.commands.treats as treats

channels_to_join = ['#singlerider']

for channel in channels_to_join:
    channel = channel.lstrip('#')
    globals.CHANNEL_INFO[channel] = {'caught': True, 'pokemon': ''}

config = {
    # details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'Pikachu__bot',
    # get this from http://twitchapps.com/tmi/
    'oauth_password': 'oauth:6yc3lsd1ho0jmw52vr58udcy2mqe32',

    'debug': True,
    'log_messages': True,

    'channels': channels_to_join,

    # Cron jobs.
    'cron': {
        '#acarlton5': [
            # time, run, callback
            (60, True, pokemon.cron),  # pokemon released every 20 minutes
            (600, True, treats.cron),  # treat handed out every 10 minutes
        ],
    },
}
