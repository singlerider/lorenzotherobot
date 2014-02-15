import time
from src.config.config import *
from functions_general import *

class cron:

	def __init__(self, irc, channel):
		self.messages = config['cron'][channel]['cron_messages']
		self.run_time = config['cron'][channel]['run_time']
		self.last_index = 0
		self.irc = irc
		self.channel = channel

	def get_next_message(self):
		next_index = self.last_index + 1


		if next_index > len(self.messages) - 1:
			next_index = 0

		self.last_index = next_index

		return next_index

	def run(self):
		time.sleep(self.run_time)
		while True:
			index = self.get_next_message()

			pbot('[CRON] %s' % self.messages[index], self.channel)

			self.irc.send_message(self.channel, self.messages[index])

			self.last_ran = time.time()

			time.sleep(self.run_time)