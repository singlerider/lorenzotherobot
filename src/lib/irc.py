import socket, re, time

class irc:

	def __init__(self, config):
		self.channel = config['channel']
	
	def check_for_message(self, data):
		if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.tmi\.twitch\.tv PRIVMSG #[a-zA-Z0-9_]+ :.+$', data):
			return True

	def check_is_command(self, message, valid_commands):
		for command in valid_commands:
			if command == message:
				return True

	def check_for_connected(self, data):
		if re.match(r'^:tmi.twitch.tv 001 .+ :connected to TMI$', data):
			return True

	def check_for_ping(self, data):
		if data[:4] == "PING":
			self.sock.send(data.replace('PING', 'PONG'))

	def get_message(self, data):
		return {
			'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
			'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0]
		}

	def send_message(self, message):
		self.sock.send('PRIVMSG %s :%s\n' % (self.channel, message))
		time.sleep(0.25)

	def get_irc_socket_object(self, config):
		sock = socket.socket()
		sock.connect((config['server'], config['port']))

		sock.send('USER %s\r\n' % config['username'])
		sock.send('PASS %s\r\n' % config['oauth_password'])
		sock.send('NICK %s\r\n' % config['username'])
		sock.send('JOIN %s\r\n' % config['channel'])

		self.sock = sock

		return sock