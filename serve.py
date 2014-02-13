from sys import argv
from src.bot import *

try:
	if argv[1][:1] != '#': argv[1] = '#' + argv[1]
	config['channel'] = argv[1]
except:
	pass
	

bot = Roboraj(config).run()