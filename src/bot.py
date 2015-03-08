"""
Simple IRC Bot for Twitch.tv

Originally developed by Aidan Thomson <aidraj0@gmail.com>

Forked and heavily modified by Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox
"""

import lib.irc as irc_
from lib.functions_general import *
import lib.functions_commands as commands
import src.lib.user_data as info
import sys
import datetime
import traceback
import sched, time
import threading
import src.lib.commands.llama as llama_import
import importlib

END = False

class Roboraj(object):

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_irc_socket_object()

	def run(self):

		irc = self.irc
		sock = self.socket
		config = self.config

		while True:

			try:
				
				data = sock.recv(config['socket_buffer_size']).rstrip()
	
				if len(data) == 0:
					pp('Connection was lost, reconnecting.')
					sock = self.irc.get_irc_socket_object()

				if config['debug']:
					print data
						
				# check for ping, reply with pong
				irc.check_for_ping(data)

				if irc.check_for_message(data):
					llama_module = importlib.import_module('src.lib.commands.llama')
					reload(llama_module)
					treats_module = importlib.import_module('src.lib.commands.treats')
					reload(treats_module)
					commands_module = importlib.import_module('src.lib.commands.commands')
					reload(commands_module)
					vote_module = importlib.import_module('src.lib.commands.vote')
					reload(vote_module)
					capture_module = importlib.import_module('src.lib.commands.capture')
					reload(capture_module)
					shots_module = importlib.import_module('src.lib.commands.shots')
					reload(shots_module)
					message_dict = irc.get_message(data)
					channel = message_dict['channel']
					message = message_dict['message']#.lower()
					username = message_dict['username']
					llama_module.user_data_name = username
					treats_module.mod_name = username
					commands_module.mod_name = username
					shots_module.mod_name = username
					vote_module.voter = username
					capture_module.poke_master = username
					ppi(channel, message, username)
					
					# check if message is a command with no arguments
					if commands.is_valid_command(message) or commands.is_valid_command(message.split(' ')[0]):
						command = message
	
						if commands.check_returns_function(command.split(' ')[0]):
							if commands.check_has_correct_args(message, command.split(' ')[0]):
								command = command.split(' ')[0]
								if commands.check_is_space_case(message):
									# let's get crazy with space cases!
									args = []
									args.append(message[len(command):])
									# basically if we only have argc as defined in command_headers then
									# we can allow spaces.
								else:
									args = message.split(' ')[1:]
								#print "Args matey! {0}:".format(len(args)), args
								
									
								# Handles Moderator-level commands - add 'ul': 'mod' to all commands with intended restriction
								
								if commands.check_has_ul(username, command):
									#if username not in llama_import.get_dict_for_users()[0]["chatters"]["moderators"]:
									if username != "singlerider":
										resp = '(%s) : %s' % (username, "This is a moderator-only command!")
										pbot(resp, channel)
										irc.send_message(channel, resp)
										continue
								
								#if commands.command_user_level(command, channel):

								if commands.is_on_cooldown(command, channel):
									pbot('Command is on cooldown, sucka. (%s) (%s) (%ss remaining)' % (
										command, username, commands.get_cooldown_remaining(command, channel)), 
										channel
									)
								else:
									pbot('Command is valid an not on cooldown. (%s) (%s)' % (
										command, username), 
										channel
									)
									
									#if commands.command_user_level(command, channel):
									#	pbot('Command User Level is Mod. (%s) (%s) (%ss remaining)'
									#	)
									#	print "USER LEVEL MOD"
									#	
									#else:
									#	pbot('Command User Level is Not Mod. (%s) (%s) (%ss remaining)' 
									#	)
									#	print "USER LEVEL REG"
									
									result = commands.pass_to_function(command, args)
									commands.update_last_used(command, channel)
	
									if result:
										resp = '(%s) : %s' % (username, result)
										pbot(resp, channel)
										irc.send_message(channel, resp)
			
							else:
								#Remove '(%s)' ':' and 'username' to remove username prefix for message
								resp = '(%s) : %s' % (username, "Incorrect usage")
								pbot(resp, channel)
								irc.send_message(channel, resp)
						else:
							if commands.is_on_cooldown(command, channel):
								pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
										command, username, commands.get_cooldown_remaining(command, channel)), 
										channel
								)
							elif commands.check_has_return(command):
								pbot('Command is valid and not on cooldown. (%s) (%s)' % (
									command, username), 
									channel
								)
								#commands.update_last_used(command, channel)
	
								resp = '(%s) : %s' % (username, commands.get_return(command))
								commands.update_last_used(command, channel)
	
								pbot(resp, channel)
								irc.send_message(channel, resp)
			except Exception as err:
				traceback.print_exc(file=self.log)

#Logged in UTF-8
class Logger(Roboraj):
	def __init__(self, config, filename="Default.log"):
		# this should be saved in yourlogfilename.txt
		print "The following log is for " + str(datetime.date.today()) + ". "
		super(Logger, self).__init__(config)
		self.terminal = sys.stdout
		sys.stdout = self
		self.log = open(filename, "a")
	def write(self, message):
		#In the event of an error, "try", to prevent bot crash. If there is an error, print it
		try:
			safe_message = unicode(message).encode('utf8', 'ignore')
			self.terminal.write(safe_message)
			self.log.write(safe_message)
		except Exception as err:
			#Uncomment line below the print error to console when it occurs
			#self.log.write("Unhandled error:\n" + str(err))
			
			traceback.print_exc(file=self.log)
		#Log the console output to file as it comes in
		finally:
			self.log.flush()