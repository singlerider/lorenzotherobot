"""
Simple IRC Bot for Twitch.tv

Developed by Aidan Thomson <aidraj0@gmail.com>
"""


from imports import *

class Roboraj:

	def __init__(self, config):
		self.irc = irc_.irc()
		self.config = config
		self.socket = self.irc.get_irc_socket_object(config)


	def run(self):
		irc = self.irc
		sock = self.socket
		
		# start threads for channels that have cron messages to run
		for channel in config['channels']:
			if channel in config['cron']:
				if config['cron'][channel]['run_cron']:
					thread.start_new_thread(cron.cron(irc, channel).run, ())

		irc.join_channels(irc.channels_to_string(config['channels']))

		while True:
			data = sock.recv(1024).rstrip()

			if config['debug']:
				print data

			# check for ping, reply with pong
			irc.check_for_ping(data)

			if irc.check_for_message(data):
				message_dict = irc.get_message(data)

				ppi(message_dict['channel'], message_dict['message'], message_dict['username'])

				channel = message_dict['channel']
				message = message_dict['message']
				username = message_dict['username']

				# check if message is a command with no arguments
				if commands.is_valid_command(message) or commands.is_valid_command(message.split(' ')[0]):
					command = message

					if commands.check_returns_function(command.split(' ')[0]):
						if commands.check_has_correct_args(command, command.split(' ')[0]):
							args = command.split(' ')
							del args[0]

							command = command.split(' ')[0]

							if commands.is_on_cooldown(command):
								pbot('Command is on cooldown. (%s) (%s)' % (command, username), channel)
							else:
								pbot('Command is valid an not on cooldown. (%s) (%s)' % (command, username), channel)
								
								result = commands.pass_to_function(command, args)
								
								if result:
									resp = '(%s) > %s' % (username, result)
									pbot(resp, channel)
									irc.send_message(channel, resp)

					else:
						if commands.is_on_cooldown(command):
							pbot('Command is on cooldown. (%s) (%s)' % (command, username), channel)
						elif commands.check_has_return(command):
							pbot('Command is valid and not on cooldown. (%s) (%s)' % (command, username), channel)
							commands.update_last_used(command)

							resp = '(%s) > %s' % (username, commands.get_return(command))
							pbot(resp, channel)
							irc.send_message(channel, resp)
