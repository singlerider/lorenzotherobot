"""
Simple IRC Bot for Twitch.tv

Developed by Aidan Thomson <aidraj0@gmail.com>
"""

import lib.irc as irc_
from lib.functions_general import *
import lib.functions_commands as commands

class Roboraj:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_irc_socket_object()


	def run(self):
		irc = self.irc
		sock = self.socket
		config = self.config

		while True:
			data = sock.recv(config['socket_buffer_size']).rstrip()

			if len(data) == 0:
				po('Connection was lost, reconnecting.')
				sock = self.irc.get_irc_socket_object()

			if config['debug']:
				print data

			# check for ping, reply with pong
			irc.check_for_ping(data)

			if irc.check_for_message(data):
				message_dict = irc.get_message(data)

				channel = message_dict['channel']
				message = message_dict['message']
				username = message_dict['username']

				ppi(channel, message, username)

				# check if message is a command with no arguments
				if commands.is_valid_command(message) or commands.is_valid_command(message.split(' ')[0]):
					command = message

					if commands.check_returns_function(command.split(' ')[0]):
						if commands.check_has_correct_args(command, command.split(' ')[0]):
							args = command.split(' ')
							del args[0]

							command = command.split(' ')[0]

							if commands.is_on_cooldown(command, channel):
								pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
									command, username, commands.get_cooldown_remaining(command, channel)), 
									channel
								)
							else:
								pbot('Command is valid an not on cooldown. (%s) (%s)' % (
									command, username), 
									channel
								)
								
								result = commands.pass_to_function(command, args)
								commands.update_last_used(command, channel)

								if result:
									resp = '(%s) > %s' % (username, result)
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
							commands.update_last_used(command, channel)

							resp = '(%s) > %s' % (username, commands.get_return(command))
							commands.update_last_used(command, channel)

							pbot(resp, channel)
							irc.send_message(channel, resp)
