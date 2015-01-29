import socket, re, time, sys
from functions_general import *
import cron
import thread


threshold = 5 * 60 # five minutes, make this whatever you want

class irc:
	
	def __init__(self, config):
		self.config = config

	def check_for_message(self, data):
		if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data):
			return True
		
	def check_for_join(self, data):
		if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) JOIN #[a-zA-Z0-9_]', data):
			return True
		
	def check_for_part(self, data):
		if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PART #[a-zA-Z0-9_]', data):
			return True
	
	#broken code
	#def check_mod(self, data):
	#	if re.match(r':jtv + MODE + #[a-zA-Z0-9_] +o [a-zA-Z0-9_]'):
	#		return True
		
	def check_is_command(self, message, valid_commands):
		for command in valid_commands:
			if command == message:
				return True

	def check_for_connected(self, data):
		if re.match(r'^:.+ 001 .+ :connected to TMI$', data):
			return True
		
	def get_logged_in_users(self, data):
		if data.find ( '353'):
			return True
			#:lorenzotherobot.tmi.twitch.tv 353 lorenzotherobot = #curvyllama :l0rd_bulldog agentsfire workundercover69 the_polite_zombie jalenxweezy13 curvyllama hmichaelh2015 steven0405 armypenguin91 hionas22 prophecymxxm singlerider bentleet tesylesor vipervenom2u zombiesdelux115 lorenzotherobot nerdy0rgyparty michaelcycle gewgled jconnfilm rustemperor frozelio

	def check_for_ping(self, data):
		
		last_ping = time.time()
		#if data[0:4] == "PING":
		if data.find ( 'PING' ) != -1:
			self.sock.send( 'PONG ' + data.split() [ 1 ] + '\r\n' )
			last_ping = time.time()
		if (time.time() - last_ping) > threshold:
			sys.exit()

	def get_message(self, data):
		return {
			'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
			'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
			'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0].decode('utf8')
		}

	def get_user(self, data):
		return {
			'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
			'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ JOIN (.*?) :', data)[0]
		}
		

	

	def check_login_status(self, data):
		if re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data):
			return False
		else:
			return True
		
		

	def send_message(self, channel, message):
		self.sock.send('PRIVMSG %s :%s\n' % (channel, message.encode('utf-8')))

	def get_irc_socket_object(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(10)

		self.sock = sock

		try:
			sock.connect((self.config['server'], self.config['port']))
		except:
			pp('Cannot connect to server (%s:%s).' % (self.config['server'], self.config['port']), 'error')
			sys.exit()

		sock.settimeout(None)

		sock.send('USER %s\r\n' % self.config['username'])
		sock.send('PASS %s\r\n' % self.config['oauth_password'])
		sock.send('NICK %s\r\n' % self.config['username'])

		if self.check_login_status(sock.recv(1024)):
			pp('Login successful.')
		else:
			pp('Login unsuccessful. (hint: make sure your oauth token is set in self.config/self.config.py).', 'error')
			sys.exit()

		# start threads for channels that have cron messages to run
		for channel in self.config['channels']:
			if channel in self.config['cron']:
				if self.config['cron'][channel]['run_cron']:
					# This is where the thread for cron_job is initiated
					print "cron_job thread init"
					thread.start_new_thread(cron.cron(self, channel).run, ())
					print "cron_job thread kill"

		self.join_channels(self.channels_to_string(self.config['channels']))


		return sock

	def channels_to_string(self, channel_list):
		return ','.join(channel_list)

	def join_channels(self, channels):
		pp('Joining channels %s.' % channels)
		self.sock.send('JOIN %s\r\n' % channels)
		pp('Joined channels.')

	def leave_channels(self, channels):
		pp('Leaving channels %s,' % channels)
		self.sock.send('PART %s\r\n' % channels)
		pp('Left channels.')