def randomviewer(irc, channel):
	print channel
	irc.sock.send('WHO %s' % channel)