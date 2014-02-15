import time

red = "\033[01;31m{0}\033[00m"
grn = "\033[01;36m{0}\033[00m"
blu = "\033[01;34m{0}\033[00m"
cya = "\033[01;36m{0}\033[00m"


def pp(message, mtype='INFO'):
	mtype = mtype.upper()

	if mtype == "ERROR":
		mtype = red.format(mtype)

	print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
	print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, grn.format(username.lower()), message)

def pbot(message, channel=''):
	if channel: msg = '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, red.format('BOT'), message)
	else: msg = '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), red.format('BOT'), message)
	
	print msg