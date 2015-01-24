from src.config.config import *

def addcom():
    return "hey dude"



commands = {
            
    '!commands': {
        'limit': 10,
        'argc': 0,
        'return': 'command',
        'ul': 'mod'
                  
    },
            
    '!opinion': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'ul': 'reg'
                 
    },
            
    '!addcom': {
        'limit': 0,
        'argc': 3,
        'return': 'command'
                
    },
    
    '!weather': {
        'limit': 10,
        'argc': 2,
        'return': 'command'
                 
    },
            
    '!wow': {
        'limit': 0,
        'argc': 3,
        'return': 'command'     
    },

	'!addlorenzo': {
		'limit': 5,
		'return': addcom()
		
	},

	'!dellorenzo': {
		'limit': 5,
		'return': 'Dude, one step at a time.'
	},

	'!chair': {
		'limit': 1,
		'return': "There's a chair over there!"
	},

	'!rails': {
		'limit': 1,
		'return': "RUST, GIVE ME THE FUNKIN' RAILS"
	},

	'!boom': {
		'limit': 0,
		'return': 'boom! headshot!'
	},
		
	'!whatever': {
		'limit': 1,
		'return': 'idclol'
	},
		
	'!randomnumber': {
		'limit': 0,
		'argc': 0,
		'return': 'command'
	},
            
	'!mball': {
        	'limit': 0,
        	'argc': 0,
        	'return': 'command'           
    },
		
	'!q': {
		'limit': 0,
		'return': 'QQQQqQqqqqqqQQQQQqQqqQQQQQQQQQqQqqQqQQQQqQQQQqQqQqqQqQQqqQqQQQQqQqQQqQQqQQ E'
	},
	
	'!carlpoppa': {
		'limit': 0,
		'return': 'Jiggy Jar Jar Do!'
	},
		
	'!hookah': {
		'limit': 30,
		'return': 'She is smoking hookah with no weed in it.'
	},
		
	'!social': {
		'limit': 30,
		'return': 'https://www.facebook.com/AmandaDefrance http://instagram.com/amanda_defrance https://twitter.com/Amanda_Defrance https://vine.co/AmandaDefrance https://www.youtube.com/channel/UC4RGs5bL4wIKbmS5kG64ABg'
	
	},
            
    '!facebook': {
        'limit': 10,
        'return': "https://www.facebook.com/AmandaDefrance"
                  
    },
            
     '!fb': {
        'limit': 10,
        'return': "https://www.facebook.com/AmandaDefrance"
                  
    },
            
     '!instagram': {
        'limit': 10,
        'return': "http://instagram.com/amanda_defrance"
                  
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
            
	'!youtube': {
        'limit': 10,
        'return': 'https://www.youtube.com/channel/UC4RGs5bL4wIKbmS5kG64ABg'
                 
    },
    
    '!yt': {
        'limit': 10,
        'return': 'https://www.youtube.com/channel/UC4RGs5bL4wIKbmS5kG64ABg'
                 
    },
            
    '!gt': {
        'limit': 10,
        'return': "curvy8ubbles"
            
    },
            
    '!gamertag': {
        'limit': 10,
        'return': "curvy8ubbles"
                  
    },
    
	'!rules': {
		'limit': 20,
		'return': "1. No sexual harassment 2.Be respectful in the chat 3. No asking for mod, it will be earned 4. No advertising channels 5. Don't be annoying with spam in the chat. Lastly, have fun!"		
	},
		
	'!welcome': {
		'limit': 20,
		'return': "Welcome to the stream. You are now a Llama! If you'd like to know how we do things, type !rules."
	},
		
	'!pwv': {
		'limit': 5,
		'return': 'If you would like to play with Amanda send the message INV to curvy8ubbles.'	
			
	},
		
	'!links': {
		'limit': 5,
		'return': 'DO NOT POST LINKS unless its approved by mods or curvy!'
			
	},
		
	'!daddy': {
		'limit': 0,
		'return': 'DADDYS BACK YOU BITCHES!!!!!!!!'	
			
	},
            
    '!kavinsky': {
        'limit': 5,
        'return': 'And it will forever be known as... the ghost car.'
                  
    },
            
    '!sunday': {
        'limit': 0,
        'return': '(Metal Gear) Solid Sundays with Amanda and Shane!'
    }, 
    
    '!monday': {
        'limit': 0,
        'return': 'Minecraft Mondays with JoeCow and Phin!'
    },
    
    '!shane':  {
        'limit': 10,
        'return': "Shane's the robot dude that helps Amanda stream sometimes. He has a chip implanted in his left hand and a magnet implanted in each ring finger and nanomachines Kappa. His username is 'singlerider'."
                
    },
            
    '!james': {
        'limit': 10,
        'return': "James is the guy the you guys commonly hear in the background while Amanda streams. He does IT work as his job and is really good with computers. His username is 'peligrosocortez'."               
    },
            
    '!cry': {
        'limit': 0,
        'return': 'BibleThump BibleThump BibleThump'
             
    },
    
    '!duck': {
        'limit': 0,
        'return': 'FUCK DUCK! FUCK DUCK!'
              
    },
            
    '!saturday': {
        'limit': 0,
        'return': 'Saturdays are #shityourpantssaturday (#syps). Amanda plays scary games all night.'
    },
            
    '!rustemperor': {
        'limit': 100000,
        'return': "Rust is Curvyllama's most famous troll. If only he'd remember that she's going for a subscribe button..."
     #   'return': 'FUCK RUST! FUCK RUST!'
          
    },
    
    '!ny': {
        'limit': 10,
        'return': "NewYork_Triforce is here to RKO trolls outta nowhere!!!"
    
    },
            
    '!emmo': {
        'limit': 10,
        'return': 'Would you like a brew, momma? <3'
              
    },
            
    '!aj': {
        'limit': 10,
        'return': 'Aj used ban on troll, it was super effective!!!'
            
    },
            
    '!rebecca': {
        'limit': 0,
        'return': 'dat fat bitch and her baby needs 2 die.'
                 
    },
    
    '!clem': {
        'limit': 0,       
        'return': 'Leave little Carl alone! BibleThump!'
    
    },
            
    '!lee': {
        'limit': 0,
        'return': '"Clem, keep that hair short."'
             
    },

	'!friendly': {
		'limit': 0,
		'return': "Friendly!! Don't shoot! \Kappa/"

    },

            
    '!pokemon' : {
        'limit': 0,
        'argc': 0,
        'return': 'command'
                  
    },

	'!ben': {
		'limit': 0,
		'return': 'fuck ben! fuck ben!'


	},

	'!zombie': {

		'limit': 15,
		'return': 'the_polite_zombie is the original quicker picker upper'
	},
            
    '!data': {
        'limit': 0,
        'argc': 0,
        'return': 'command'
               
    },
            
    '!buyprints': {
        'limit': 15,
        'return': 'Information on buying a print from Amanda is coming soon!'
                   
    },
            
    '!playlist': {
        'limit': 15,
        'return': 'Song request is not used on this channel. Please feel free to add songs to this community playlist on Spotify. http://open.spotify.com/user/jamesypaulmichael/playlist/2HejukmtRzlcan06cXMkGG'
                  
    },
            
    '!songrequest': {
        'limit': 0,
        'argc': 3,
        'return': 'command'
                     
    }            
            
    #'!pokemon2' : {
    #    'limit': 0,
    #    'argc': 0,
    #    'return': 'command'
                   
    #}
            
}




for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
