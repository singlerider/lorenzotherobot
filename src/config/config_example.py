global config

import src.lib.save_to_drive as save_to_drive
import src.lib.commands.poll as poll
import src.lib.commands.trade as trade
import src.lib.commands.advertisement as advertisement
import src.lib.commands.party as party
import src.lib.commands.pokemon as pokemon
import src.lib.commands.treats as treats
import globals

save_to_drive.get_credentials()

channels_to_join = ['#acarlton5']

for channel in channels_to_join:
    channel = channel.lstrip('#')
    globals.channel_info[channel] = {'caught': True, 'pokemon': ''}

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
            #time, run, callback
            (60, True, pokemon.cron),  # pokemon released every 20 minutes
            (600, True, treats.cron),  # treat handed out every 10 minutes
        ],
    },
}
