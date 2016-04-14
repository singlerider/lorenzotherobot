import globals

commands = {
    '!report': {
        'limit': 200,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'ul': 'mod',
        'usage': "!report [insert bug report text here]"
    },
    '!commands': {
        'limit': 10,
        'argc': 0,
        'return': 'command',
        'usage': '!commands'
    },
    '!opinion': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'ul': 'reg',
        'usage': '!opinion',
        'user_limit': 30
    },
    '!llama': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!llama ['treats'/'shots'/username/'list']",
        'optional': True,
        'user_limit': 30
    },
    '!treats': {
        'limit': 0,
        'return': 'command',
        'argc': 3,
        'ul': 'mod',
        'usage': '!treats [add/remove/set] [username] [number]'
    },
    '!shots': {
        'limit': 0,
        'return': 'command',
        'argc': 2,
        'ul': 'mod',
        'usage': '!shots [add/remove/set] [number]'
    },
    '!wins': {
        'limit': 0,
        'return': 'command',
        'argc': 2,
        'optional': True,
        'usage': '!wins [add/remove/set] [number]'
    },
    '!help': {
        'limit': 15,
        'return': 'There is a super useful README for lorenzo at http://www.twitch.tv/lorenzotherobot',
        'usage': '!help',
        'user_limit': 30
    },
    '!highlight': {
        'limit': 15,
        'return': 'command',
        'argc': 0,
        'usage': '!highlight'
    },
    '!followers': {
        'limit': 30,
        'return': 'command',
        'argc': 0,
        'usage': '!followers',
        'user_limit': 30,
    },
    '!follower': {
        'limit': 0,
        'return': 'command',
        'argc': 1,
        'usage': '!follower [username]',
        'ul': 'mod'
    },
    '!uptime': {
        'limit': 15,
        'return': 'command',
        'argc': 0,
        'usage': '!uptime',
        'user_limit': 30,
    },
    '!stream': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!stream'
    },
    '!winner': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!winner',
        'user_limit': 30,
    },
    '!catch': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!catch'
    },
    '!release': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': '!release [party_position_number_to_be_released] [your_username]'
    },
    '!arbitrary': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!arbitrary ['number'/'emote']"
    },
    '!party': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!party [position_to_check(1-6)/'members'/username]",
        'optional': True,
        'user_limit': 30,
    },
    '!battle': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': "!battle [position_to_battle_with] [opponent_username]"
    },
    '!tallgrass': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': "!tallgrass [number_of_treats_to_sacrifice]"
    },
    '!gift': {
        'limit': 0,
        'argc': 3,
        'return': 'command',
        'ul': 'mod',
        'usage': "!gift [username] [Pokemon_name/'item'] [starting_level/'item_number']"
    },
    '!evolve': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!evolve [position_to_evolve]'
    },
    '!nickname': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': '!nickname [position_to_update] [nickname(must not contain spaces)]'
    },
    '!popularity': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'usage': '!popularity [name_of_game]'
    },
    '!trade': {
        'limit': 0,
        'argc': 3,
        'return': 'command',
        'usage': "!trade [party_position] [requested_pokemon] [minimum_asking_level]"
    },
    '!redeem': {
        'limit': 0,
        'argc': 3,
        'return': 'command',
        'usage': "!redeem [party_position_to_trade] [username_to_trade] [party_position_to_redeem_from_user]"
    },
    '!check': {
        'limit': 10,
        'argc': 1,
        'return': 'command',
        'usage': "!check ['trades'/'market'/'items'/'inventory'/username]",
        'user_limit': 30
    },
    '!buy': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': "!buy [\"pokemon\"/\"item\"] [item_number/pokemon_position]"
    },
    '!use': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': '!use [item_position] [party_position]'
    },
    '!leaderboard': {
        'limit': 300,
        'argc': 0,
        'return': 'command',
        'usage': '!leaderboard',
        'user_limit': 300,
    },
    '!stats': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!stats',
        'user_limit': 1000,
    },
    '!define': {
        'limit': 30,
        'user_limit': 300,
        'argc': 1,
        'space_case': True,
        'return': 'command',
        'usage': '!define [insert_word_here]'
    },
    '!caster': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!caster [streamer_username]',
        'ul': 'mod'
    },
    '!donation': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': '!donation [username] [dollar_amount]',
        'ul': 'mod'
    },
    '!add': {
        'limit': 0,
        'argc': 4,
        'return': 'command',
        'usage': '!add [!command_name] [user_level (reg/mod)] [response (to add a custom user, use "{}") (to include message count, use "[]")]',
        'ul': 'mod'
    },
    '!rem': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!rem [!command_name]',
        'ul': 'mod'
    },
    '!edit': {
        'limit': 0,
        'argc': 4,
        'return': 'command',
        'usage': '!edit [!command_name] [user_level (reg/mod)] [response (to add a custom user, use "{}")]',
        'ul': 'mod'
    },
    '!weather': {
        'limit': 0,
        'argc': 2,
        'return': 'command',
        'usage': '!weather [units (metric/imperial)] [location (any format)]',
        'ul': 'mod'
    },
    '!loyalty': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!loyalty [username]',
        'ul': 'mod'
    },
    '!addquote': {
        'limit': 0,
        'argc': 1,
        'user_limit': 15,
        'return': 'command',
        'usage': '!addquote [quote]',
        'space_case': True
    },
    '!quote': {
        'limit': 0,
        'argc': 0,
        'user_limit': 5,
        'return': 'command',
        'usage': '!quote'
    },
    '!subcount': {
        'limit': 0,
        'argc': 0,
        'ul': 'mod',
        'return': 'command',
        'usage': '!subcount'
    },
    '!testcommand': {
        'limit': 0,
        'argc': 0,
        'ul': 'mod',
        'return': 'command',
        'usage': '!testcommand'
    },
    # '!join': {
    #     'limit': 0,
    #     'argc': 0,
    #     'return': 'command',
    #     'usage': '!join'
    # },
    # '!leave': {
    #     'limit': 0,
    #     'argc': 0,
    #     'return': 'command',
    #     'usage': '!leave'
    # },
    '!blacklist': {
        'limit': 0,
        'argc': 0,
        'ul': 'superuser',
        'return': 'command',
        'usage': '!blacklist ["add"/"remove"] [username]'
    }
}

user_cooldowns = {"channels": {}}


def initalizeCommandsAfterRuntime(channel):
    if channel not in user_cooldowns["channels"]:
        user_cooldowns["channels"][channel] = {"commands": {}}
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
            if "user_limit" in commands[command]:
                user_cooldowns["channels"][channel]["commands"][command] = {
                    "users": {}}
        channel = channel.lstrip('#')
        globals.CHANNEL_INFO[channel] = {'caught': True, 'pokemon': ""}


def deinitializeCommandsAfterRuntime(channel):
    if channel in user_cooldowns["channels"]:
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
            if "user_limit" in commands[command]:
                user_cooldowns["channels"][channel]["commands"][command] = {
                    "users": {}}
        del user_cooldowns["channels"][channel]
        channel = channel.lstrip('#')
        del globals.CHANNEL_INFO[channel]


def initalizeCommands(config):
    for channel in config['channels']:
        user_cooldowns["channels"][channel] = {"commands": {}}
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
            if "user_limit" in commands[command]:
                user_cooldowns["channels"][channel]["commands"][command] = {
                    "users": {}}

if __name__ == "__main__":  # pragma: no cover
    print "\n".join(["    " + key + ": " + commands[key][
        "usage"] for key in commands])
