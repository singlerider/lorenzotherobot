import time
from src.config.config import *
from functions_general import *

class cron:

	def __init__(self, irc, channel):
		#self.messages = config['cron'][channel]['cron_messages']
		self.run_time = config['cron'][channel]['run_time']
		self.functions = [funcs[0] for funcs in config['cron'][channel]['cron_functions']]
		self.args = [args[1] for args in config['cron'][channel]['cron_functions']]
		
		#Do a sanity check to make sure that we have real functions in the functions list
		for func in self.functions:
			if not callable(func):
				raise ValueError("Not a function, consider that the odds of winning are very low")
		self.irc = irc
		self.channel = channel


	def run(self):
		time.sleep(self.run_time)
		while True:
			try:
				for index in range(len(self.functions)):
					# "("+ ",".join(self.args[index]) + ")"
					pbot('[CRON] ' + self.functions[index].__name__ , self.channel)
					message = str(self.functions[index](self.args[index]))					
					if len(message) > 0 and message != str(None):					
						self.irc.send_message(self.channel, message[:120])
						self.last_ran = time.time()
						time.sleep(self.run_time)
					else:
						print "Momma likes you, but she has nothing to say"
			except Exception, error:
				print "Your momma likes it in the back door:" + str(error)
				return "error"
			
			
