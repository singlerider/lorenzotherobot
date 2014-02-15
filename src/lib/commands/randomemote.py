# coding: utf8

import random, json

def randomemote():
	
	filename = 'src/res/global_emotes.json'

	try:
		data = json.loads(file(filename, 'r').read())
	except:
		return 'Error reading %s.' % filename

	emote = random.choice(data.keys())

	return '%s = %s' % (
		emote,
		emote[:1] + '​'.decode('utf8') + emote[1:]
	)