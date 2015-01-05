from src.config.config import *

def addcom():
    pass

commands = {

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
	
	'!rules': {
		'limit': 20,
		'return': "1. No sexual harassment 2.Be respectful in the chat 3. No asking for mod, it will be earned 4. No advertising channels 5. Don't be annoying with spam in the chat. Lastly, have fun!"		
	}
}









for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
