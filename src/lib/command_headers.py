from src.config.config import *

commands = {

	'!addlorenzo': {
		'limit': 5,
		'return': 'working on it'
		
	},

	'!dellorenzo': {
		'limit': 5,
		'return': 'Dude, one step at a time.'
	},

	'!chair': {
		'limit': 30,
		'return': "There's a chair over there!"
	},

	'!rails': {
		'limit': 180,
		'return': "RUST, GIVE ME THE FUNKIN' RAILS"
	},

	'!boom': {
		'limit': 0,
		'return': 'boom! headshot!'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
