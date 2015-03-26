commands = {
    '!flip':{
        'limit': 10,
        'return': u"\u256f\u00b0\u25a1\u00b0\uff09\u256f\ufe35"
    },
    '!commands': {
        'limit': 10,
        'argc': 0,
        'return': 'command'

    },

    '!opinion': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'ul': 'reg'

    },

    '!chair': {
        'limit': 1,
        'return': "There's a chair over there!"
    },


    '!randomnumber': {
        'limit': 0,
        'argc': 0,
        'return': 'command'
    },

    '!randomemote': {
        'limit': 0,
        'argc': 0,
        'return': 'command'

    },

    '!carlpoppa': {
        'limit': 0,
        'return': 'Jiggy Jar Jar Do!'
    },

    '!hookah': {
        'limit': 30,
        'return': 'She is smoking hookah with no weed in it.'
    },


    '!fb': {
        'limit': 10,
        'return': "https://www.facebook.com/AmandaDefrance"

    },


    '!ig': {
        'limit': 10,
        'return': "http://instagram.com/amanda_defrance"

    },

    '!twitter': {
        'limit': 10,
        'return': "https://twitter.com/Amanda_Defrance"

    },

    '!vine': {
        'limit': 10,
        'return': "https://vine.co/AmandaDefrance"

    },

    '!yt': {
        'limit': 10,
        'return': 'https://www.youtube.com/channel/UC4RGs5bL4wIKbmS5kG64ABg'

    },


    '!gt': {
        'limit': 10,
        'return': "curvy8ubbles"

    },

    '!rules': {
        'limit': 20,
        'return': "1. No sexual harassment 2.Be respectful in the chat 3. No asking for mod, it will be earned 4. No advertising channels 5. Don't be annoying with spam in the chat. Lastly, have fun!"
    },

    '!welcome': {
        'limit': 20,
        'return': "Welcome to the Llama family. Sit down, relax, and have a bisqwuit (in other words thanks for following)! If you'd like to know how we do things, type !rules."
    },

    '!pwv': {
        'limit': 5,
        'return': 'If you would like to play with Amanda send the message INV to curvy8ubbles.'

    },


    '!daddy': {
        'limit': 0,
        'return': 'DADDYS BACK YOU BITCHES!!!!!!!!'

    },


    '!cry': {
        'limit': 0,
        'return': 'BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump '

    },

    '!saturday': {
        'limit': 0,
        'return': 'Saturdays are #shityourpantssaturday (#syps). Amanda plays scary games all night.'
    },


    '!pokemon': {
        'limit': 0,
        'argc': 1,
        'return': 'command'

    },


    '!buyprints': {
        'limit': 15,
        'return': 'Check out some model/cosplay prints & posters Amanda has for sale here: https://www.facebook.com/media/set/?set=a.695350670512515.1073741836.276081062439480'

    },

    '!playlist': {
        'limit': 15,
        'return': 'https://www.youtube.com/playlist?list=PLN5FU2O1KYjlkturlsYgNyCLZ8gsH6UZg'

    },

    '!request': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'space_case': True
    },

    '!songrequest': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'space_case': True
    },

    '!poll': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'ul': 'mod',
        'space_case': True

    },

    '!vote': {
        'limit': 0,
        'argc': 1,
        'return': 'command'

    },


    '!llama': {
        'limit': 0,
        'argc': 1,
        'return': 'command'

    },

    '!weather': {
        'limit': 0,
        'return': 'command',
        'argc': 1,
        'ul': 'mod'

    },

    '!specs': {
        'limit': 15,
        'return': "Case: Phanteks ATX-Full, MoBo: Gigabyte GA 990-FXA-UD3, CPU: AMD FX-4300, RAM: 8GB G-Skill 1600, GPU: AMD R9 270, PSU: 450 Watt, "

    },

    '!treats': {
        'limit': 0,
        'return': 'command',
        'argc': 3,
        'ul': 'mod'

    },

    '!shots': {
        'limit': 0,
        'return': 'command',
        'argc': 2,
        'ul': 'mod'

    },

    '!help': {
        'limit': 15,
        'return': 'There is a super useful README for lorenzo at htp://www.github.com/singlerider/lorenzotherobot'

    },

    '!me': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!viewers': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!highlight': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!followers': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!uptime': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!stream': {
        'limit': 0,
        'return': 'command',
        'argc': 0

    },

    '!kappa': {
        'limit': 0,
        'return': 'Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa',

    },

    '!winner': {
        'limit': 0,
        'argc': 0,
        'return': 'command'

    },

    '!capture': {
        'limit': 0,
        'argc': 0,
        'return': 'command'

    }



}


def initalizeCommands(config):
    for channel in config['channels']:
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
