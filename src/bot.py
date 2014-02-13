"""
Simple IRC Bot for Twitch.tv

Developed by Aidan Thomson <aidraj0@gmail.com>
"""


from imports import *

class Roboraj:

	def __init__(self, config):
		self.irc = irc_.irc(config)
		self.config = config
		self.socket = self.irc.get_irc_socket_object(config)

	def run(self):
		irc = self.irc
		sock = self.socket

		pp('Starting main loop.')
		#irc.send_message('Roboraj has entered da room! 4Head')

		pbot('Starting cron thread.')
		thread.start_new_thread(cron.cron(irc).run, ())

		while True:
			data = sock.recv(2048).rstrip()

			irc.check_for_ping(data)

			if irc.check_for_connected(data):
				pp('Connected to %s on TMI.' % self.config['channel'])


			if irc.check_for_message(data):
				message_dict = irc.get_message(data)

				ppi(message_dict['message'], message_dict['username'])

				message = message_dict['message']
				username = message_dict['username']

				# check if message is a command with no arguments
				if commands.is_valid_command(message):
					command = message

					if commands.is_on_cooldown(command):
						pbot('Command is on cooldown. (%s) (%s)' % (command, username))
					elif commands.check_has_return(command):
						pbot('Command is valid and not on cooldown. (%s) (%s)' % (command, username))
						commands.update_last_used(command)

						irc.send_message('(%s) > (%s)' % (username, commands.get_return(command)))

				# check if message is a command with arguments
				if commands.is_valid_command(message.split(' ')[0]):
					if commands.check_has_correct_args(message, message.split(' ')[0]):
						if commands.is_on_cooldown(message.split(' ')[0]):
							pbot('Command is on cooldown. (%s) (%s)' % (message.split(' ')[0], username))
						else:
							pbot('Command is valid an not on cooldown. (%s) (%s)' % (message.split(' ')[0], username))
							command = message.split(' ')[0]
													
							args = message.split(' ')
							del args[0]

							result = commands.pass_to_function(command, args)
							
							if result:
								irc.send_message('(%s) > %s' % (username, result))

						


				
