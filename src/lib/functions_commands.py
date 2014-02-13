import time

global_cooldown = 0

valid_commands = {
	'!test': {
		'limit': 5,
		'return': 'This is a test!'
	},

	'!roboraj_test': {
		'limit': 10,
		'return': 'This is a second test!'
	},

	'!add': {
		'limit': 0,
		'argc': 2,
		'return': 'command'
	}
}




def command_add(args):
	try:
		resp = int(args[0]) + int(args[1])
		return resp
	except ValueError:
		return 'I can only add numbers, fool. DansGame'







for command in valid_commands:
	valid_commands[command]['last_used'] = 0

def is_valid_command(command):
	if command in valid_commands:
		return True

def update_last_used(command):
	valid_commands[command]['last_used'] = time.time()

def get_command_limit(command):
	return valid_commands[command]['limit']

def is_on_cooldown(command):
	if time.time() - valid_commands[command]['last_used'] < valid_commands[command]['limit']:
		return True

def check_has_return(command):
	if valid_commands[command]['return'] and valid_commands[command]['return'] != 'command':
		return True

def get_return(command):
	return valid_commands[command]['return']


def check_has_args(command):
	if valid_commands[commmand]['has_args']:
		return True

def check_has_correct_args(message, command):
	message = message.split(' ')
	if len(message) - 1 == valid_commands[command]['argc']:
		return True


def pass_to_function(command, args):
	command = 'command_' + command.replace('!', '')

	return globals()[command](args)

