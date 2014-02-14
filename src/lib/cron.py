import time
from src.imports import *

class cron:

	def __init__(self, irc):
		self.messages = [
			'This is cron message one.',
			'This is the second cron message.'
		]

		self.runtime = 0 # set to 0 to disable cron messages
		self.last_index = 0
		self.last_ran = time.time()
		self.irc = irc

	def get_next_message(self):
		next_index = self.last_index + 1
		if next_index > 1:
			next_index = 0

		self.last_index = next_index

		return next_index

	def run(self):
		if self.runtime == 0:
			pbot('Cronjob runtime set to 0, exiting thread.')
			exit()
		while True:
			if time.time() - self.last_ran > self.runtime:
				index = self.get_next_message()

				pbot('Sending cron message.')

				self.irc.send_message(self.messages[index])

				self.last_ran = time.time()