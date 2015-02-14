import time
from src.config.config import *
from functions_general import *

class cron:

	def __init__(self, irc, channel):
		#self.messages = config['cron'][channel]['cron_messages']
		self.run_time = config['cron'][channel]['run_time']
		self.functions = [funcs[0] for funcs in config['cron'][channel]['cron_functions']]
		self.args = [args[1:] for args in config['cron'][channel]['cron_functions']]
		for func in self.functions:
			if not callable(func):
				raise ValueError("Not a function, consider that the odds of winning are very low")
		self.last_index = 0
		self.irc = irc
		self.channel = channel

	def get_next_message(self):
		next_index = self.last_index + 1


		if next_index > len(self.functions) - 1:
			next_index = 0

		self.last_index = next_index

		return next_index

	def run(self):
		time.sleep(self.run_time)
		while True:
			try:
				index = self.get_next_message()
				# "("+ ",".join(self.args[index]) + ")"
				pbot('[CRON] ' + self.functions[index].__name__ , self.channel)
				
				message = str(self.functions[index](self.args[index]))
				
				if message != None:
				
					self.irc.send_message(self.channel, message[:120])
		
					self.last_ran = time.time()
		
					time.sleep(self.run_time)
				
				else:
					
					pass
			except:
				return "error"
			
			
