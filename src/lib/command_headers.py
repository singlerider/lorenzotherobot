commands = {
            
    '!report':{
        'limit': 200,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'ul': 'mod',
        'usage': "!report [insert bug report text here]"
               
    },
    
    '!flip':{
        'limit': 10,
        'return': u"\u256f\u00b0\u25a1\u00b0\uff09\u256f\ufe35",
        'usage': "!flip"        
    },
            
    '!maggie': {
        'limit': 10,
        'return': 'Amanda is, in reality the actual Lauren Cohan from The Walking Dead.',
        'usage': '!maggie'
                
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

    '!chair': {
        'limit': 1,
        'return': "There's a chair over there!",
        'usage': '!chair'
    },

    '!carlpoppa': {
        'limit': 0,
        'return': 'Jiggy Jar Jar Do!',
        'usage': '!carlpoppa'
    },

    '!hookah': {
        'limit': 30,
        'return': 'She is smoking hookah with no weed in it.',
        'usage': '!hookah'
    },

    '!fb': {
        'limit': 10,
        'return': "https://www.facebook.com/AmandaDefrance",
        'usage': '!fb'

    },

    '!ig': {
        'limit': 10,
        'return': "http://instagram.com/amanda_defrance",
        'usage': '!ig'

    },

    '!twitter': {
        'limit': 10,
        'return': "https://twitter.com/Amanda_Defrance - Make sure to follow Curvy on Twitter to see when she goes live!",
        'usage': '!twitter'

    },

    '!vine': {
        'limit': 10,
        'return': "https://vine.co/AmandaDefrance",
        'usage': '!vine'

    },

    '!yt': {
        'limit': 10,
        'return': 'https://www.youtube.com/channel/UC4RGs5bL4wIKbmS5kG64ABg',
        'usage': '!yt'

    },

    '!gt': {
        'limit': 10,
        'return': "curvy8ubbles",
        'usage': '!gt'

    },

    '!rules': {
        'limit': 20,
        'return': "1. No sexual harassment 2.Be respectful in the chat 3. No asking for mod, it will be earned 4. No advertising channels 5. Don't be annoying with spam in the chat. Lastly, have fun! Twitch ToS: http://www.twitch.tv/p/rules-of-conduct",
        'usage': '!rules'
    },

    '!welcome': {
        'limit': 20,
        'return': "Welcome to the Llama family. Sit down, relax, and have a bisqwuit (in other words thanks for following)! If you'd like to know how we do things, type !rules.",
        'usage': '!welcome'
    },

    '!pwv': {
        'limit': 5,
        'return': 'If you would like to play with Amanda send the message INV to curvy8ubbles.',
        'usage': '!pwv'

    },

    '!daddy': {
        'limit': 0,
        'return': 'DADDYS BACK YOU BITCHES!!!!!!!!',
        'usage': '!daddy'

    },

    '!cry': {
        'limit': 0,
        'return': 'BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump ',
        'usage': '!cry'

    },

    '!saturday': {
        'limit': 0,
        'return': 'Saturdays are #shityourpantssaturday (#syps). Amanda plays scary games all night.',
        'usage': '!saturday'
    },

    #'!pokemon': {
    #    'limit': 0,
    #    'argc': 1,
    #    'return': 'command'
    #
    #},

    '!buyprints': {
        'limit': 15,
        'return': 'Check out some model/cosplay prints & posters Amanda has for sale here: https://www.facebook.com/media/set/?set=a.695350670512515.1073741836.276081062439480',
        'usage': '!buyprints'

    },

    '!playlist': {
        'limit': 15,
        'return': 'https://www.youtube.com/playlist?list=PLN5FU2O1KYjlkturlsYgNyCLZ8gsH6UZg',
        'usage': '!playlist'

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

    '!specs': {
        'limit': 15,
        'return': "Case: Phanteks ATX-Full, MoBo: Gigabyte GA 990-FXA-UD3, CPU: AMD FX-4300, RAM: 8GB G-Skill 1600, GPU: AMD R9 270, PSU: 450 Watt, ",
        'usage': '!specs'

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
        'return': 'There is a super useful README for lorenzo at http://www.github.com/singlerider/lorenzotherobot',
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

    '!viewers': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!viewers'

    },

    '!highlight': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!highlight'

    },

    '!followers': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!followers'

    },

    '!uptime': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!uptime'

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
        'usage': "!gift [username] [Pokemon_name] [starting_level]"
              
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
        #'ul': 'mod',
        'usage': '!popularity [name_of_game]'
                    
    },
            
    '!tickets': {
        'limit': 15,
        'return': 'For every $5 donated, you get a raffle ticket. At the end of each month, 2 random viewers will be selected from the raffle\
        and be given a prize. Donate link: http://bit.ly/1s4HRig'
                 
    },
    
    '!kappa': {
        'limit': 0,
        'return': 'Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Keepo Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa Kappa',
        'usage': '!kappa'
        
    },
            
    '!trade': {
        'limit': 0,
        'argc': 3,
        'return':'command',
        'usage': "!trade [party_position] [pokemon_to_trade] [asking_level]"
    },
    
    '!redeem': {
        'limit': 0,
        'argc': 3,
        'return': 'command',
        'usage': "!redeem [party_position_to_trade] [username_to_trade] [party_position_to_redeem_from_user]"
                
    },
            
    '!check': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': "!check ['trade'/'market'/'items'/'inventory'/username]"
               
    }
}

def initalizeCommands(config):
    for channel in config['channels']:
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
