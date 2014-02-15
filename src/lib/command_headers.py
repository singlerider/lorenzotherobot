from src.config.config import *

commands = {
	'!test': {
		'limit': 30,
		'return': 'This is a test!'
	},

	'!randomemote': {
		'limit': 180,
		'argc': 0,
		'return': 'command'
	},

	'!wow': {
		'limit': 30,
		'argc': 3,
		'return': 'command'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
