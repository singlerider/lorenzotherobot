import time

red = "\033[01;31m{0}\033[00m"
grn = "\033[1;36m{0}\033[00m"


def pp(message, mtype='INFO'):
	mtype = mtype.upper()

	print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(message, username):
	print '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), grn.format(username.lower()), message)

def pbot(message):
	print '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), red.format('BOT'), message)