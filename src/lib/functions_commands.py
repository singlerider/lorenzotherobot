# coding: utf-8

import time, requests, random
from src.imports import config

valid_commands = {
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





def command_add(args):
	try:
		resp = int(args[0]) + int(args[1])
		return resp
	except ValueError:
		return 'I can only add numbers, fool. DansGame'




def command_randomemote():
	try:
		resp = requests.get('http://twitchemotes.com/global.json').json()
	except:
		return 'Error connecting to API.'

	emote = random.choice(resp.keys())

	return '%s = %s' % (
		emote,
		emote[:1] + '​'.decode('utf8') + emote[1:]
	)





def command_wow(args):
	usage = 'Usage: !wow <region> <realm> <name>'

	region = args[0].lower()
	realm = args[1].replace("'", '').replace('_', ' ').lower().encode('utf8')
	name = args[2]

	realms = []
	
	races = {
		1: 'A:Human', 2: 'H:Orc', 3:'A:Dwarf', 4:'A:Night Elf',
		5: 'H:Undead', 6: 'H:Tauren', 7:'A:Gnome', 8:'H:Troll',
		9: 'H:Goblin', 10: 'H:Blood Elf', 11: 'A:Draenei', 24:'A:Pandaren',
		22: 'A:Worgen', 25: 'A:Pandaren', 26: 'H:Pandaren'
	}

	classes = {
		1: 'Warrior', 2: 'Paladin', 3: 'Hunter', 4: 'Rogue',
		5: 'Priest', 6:'Death Knight', 7: 'Shaman', 8: 'Mage',
		9: 'Warlock', 10: 'Monk', 11: 'Druid'
	}

	if region not in ['us', 'eu']:
		return usage

	try:
		realmlist = requests.get('http://%s.battle.net/api/wow/realm/status' % region).json()

		for realm_object in realmlist['realms']:
			realms.append(realm_object['name'].lower().replace("'", '').encode('utf8'))

		if realm not in realms:
			return 'Invalid realm. (instead of using spaces in a realm name, use an underscore, ex Aerie_Peak) (%s)' % realm
	except:
		return 'Error connecting to Battle.net API.'



	try:
		character_object = requests.get('http://%s.battle.net/api/wow/character/%s/%s?fields=achievements,guild' % (
			region, realm, name
		)).json()

		try:
			return character_object['reason']
		except KeyError:
			try:
				name = name.title()
				realm = realm.title()
				level = character_object['level']
				totalhks = character_object['totalHonorableKills']
				achievp = character_object['achievementPoints']
				race = races[character_object['race']].split(':')[1].title()
				class_ = classes[character_object['class']].title()

				if 'guild' in character_object:
					guild = character_object['guild']['name'].title()
				else:
					guild = ''

				resp = '%s of <%s> is a level %s %s %s from %s. They have %s achievement points and %s honorable kills.' % (
					name, guild, level, race, class_, realm, achievp, totalhks
				)

				resp = resp.replace(' of <>', '')

				return resp
			except:
				return 'Error parsing data from API.'

	except:
		return 'Error connecting to the Battle.net API.'



























for channel in config['channels']:
	for command in valid_commands:
		valid_commands[command][channel] = {}
		valid_commands[command][channel]['last_used'] = 0


def is_valid_command(command):
	if command in valid_commands:
		return True

def update_last_used(command, channel):
	valid_commands[command][channel]['last_used'] = time.time()

def get_command_limit(command):
	return valid_commands[command]['limit']

def is_on_cooldown(command, channel):
	if time.time() - valid_commands[command][channel]['last_used'] < valid_commands[command]['limit']:
		return True

def get_cooldown_remaining(command, channel):
	return round(valid_commands[command]['limit'] - (time.time() - valid_commands[command][channel]['last_used']))

def check_has_return(command):
	if valid_commands[command]['return'] and valid_commands[command]['return'] != 'command':
		return True

def get_return(command):
	return valid_commands[command]['return']


def check_has_args(command):
	if 'argc' in valid_commands[command]:
		return True

def check_has_correct_args(message, command):
	message = message.split(' ')
	if len(message) - 1 == valid_commands[command]['argc']:
		return True

def check_returns_function(command):
	if valid_commands[command]['return'] == 'command': 
		return True

def pass_to_function(command, args):
	command = 'command_' + command.replace('!', '')

	if args:
		return globals()[command](args)
	else:
		return globals()[command]()

