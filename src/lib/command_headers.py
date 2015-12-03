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
        'usage': '!opinion'

    },

    '!request': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'usage': '!request [insert artist name and song title here]'
    },

    '!songrequest': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'usage': '!songrequest [insert artist name and song title here]'
    },

    '!poll': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'ul': 'mod',
        'space_case': True,
        'usage': "!poll ['option A'/'option B'/'option C']"

    },

    '!vote': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!vote [option_number]'

    },


    '!llama': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!llama [treats/shots/username]"

    },

    '!weather': {
        'limit': 0,
        'return': 'command',
        'argc': 1,
        'usage': '!weather [zip_code]'

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

    '!help': {
        'limit': 15,
        'return': 'There is a super useful README for lorenzo at http://www.twitch.tv/lorenzotherobot',
        'usage': '!help'

    },

    '!me': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!me (this is a test command)'

    },

    '!test': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!test (this is a test command)'

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
        'usage': '!followers'

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
        'usage': '!uptime'

    },

    '!stream': {
        'limit': 60,
        'return': 'command',
        'argc': 0,
        'usage': '!stream'

    },

    '!winner': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!winner'

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
        'usage': "!party [position_to_check(1-6)/'members'/username]"

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
        'limit': 60,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        #'ul': 'mod',
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
        'usage': "!check ['trades'/'market'/'items'/'inventory'/username]"

    },

    '!buy': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!buy [item_number]"

    },

    '!use': {
        'limit': 0,
        'argc': 2,
        #'return': 'command',
        'return': 'command',
        'usage': '!use [item_position] [party_position]'

    },

    '!leaderboard': {
        'limit': 300,
        'argc': 0,
        'return': 'command',
        'usage': '!leaderboard'

    },

    '!define': {
        'limit': 300,
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
        'usage': '!add [!command_name] [user_level (reg/mod)] [response (to add a custom user, use "{}")]',
        'ul': 'mod'
    },

    '!rem': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!rem [!command_name]',
        'ul': 'mod'
    },

}


def initalizeCommands(config):
    for channel in config['channels']:
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
