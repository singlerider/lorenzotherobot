Try it out! Code is live at
http://www.twitch.tv/curvyllama
===============================

Roboraj
=======

Lorenzotherobot
===============

This is a Twitch chat/irc bot written in python (2.7).

Installation
============
* Open up your terminal/shell of choice.
* Install the [http://docs.python-requests.org/en/latest/](Requests library) if you haven't already using 'pip install requests'. I tested this application on Python 2.7.5.
* 
* Clone the Git repository.
* Move config/config_example.py to config/config.py. Replace all of the placeholders there with your own username/oauth token/channels to join etc (tips are given in the file).
* Type 'chmod +x /serve.py'. To run, you simply need to execute the file by typing './serve.py'.


Commands
========

So, what can the bot do? Here are a list of current commands in no particular order with a description of each (if one is needed):

    '!commands'* - has different results, depending on whether or not a moderator sent the command
    '!opinion' - acts as a magic 8 ball
    '!chair'
    '!randomnumber' - returns a random number between 1 and 100
    '!randomemote' - returns a random emote from Twitch's standard emotes library
    '!carlpoppa'
    '!hookah'
    '!fb'
    '!ig'
    '!twitter'
    '!vine'
    '!yt'  
    '!gt'
    '!rules'
    '!welcome'
    '!pwv'
    '!daddy'
    '!cry'
    '!pokemon' 'battle' - forces two random pokemon to battle. at the end, a winner is declared
    '!buyprints'
    '!playlist' - depracated spotify playlist
    '!request' ['artist name and song title'] - adds requested search query result to a youtube playlist, specified by bot admin
    '!poll'* ['choice 1/choice 2/choice 3'] - mod can establish things for users to vote on from within the chat window
    '!vote' [number] - users simply send a number to decide the choice they'd like
    '!llama' 'usage' - shows everything the 'llama suite' can do - see below for more detailed instructions
    '!weather'* [zip_code] - shows current weather and forecast for any US zip code
    '!specs'
    '!treats'* ['add'/'remove'] ['username'] [amount] - allows mod to decide how many treats a user either gets added to them or removed
    '!help'

Adding your own commands
========================

You're going to need to know basic Python if you want to add your own commands. Open up 'lib/command_headers.py'. There are examples of pre-made commands in there as examples. The limit parameter is the amount of times a command can be used in seconds, if you don't want a limit to be enforced put in 0.

If your command is only going to return a string, ex - '!hello' returns 'Welcome!', don't include the 'argc' parameter. Place the string you wish to be returned to the user in the 'return' parameter. For example, if you wanted to create a command such as this and limit it to being used ever 30 seconds, you would add in:

'''python
'!hello': {
		'limit': 10,
		'return': 'Welcome!'
}
'''

However, if your command has to have some logic implemented and if the command is just going to return whatever a function returns, set the 'return' parameter on the command to 'command', and set 'argc' to '0'. If your command is going to take arguments, ex '!hello <name>', set argc to '1' or however many arguments the command is going to take in.

Make a new file in 'lib/commands/' and give the filename 'command.py' where command is the command name. If your 'argc' was set to '0', don't include 'args' in the functions parameters, else set the only parameter to 'args'. Args will contain a list of whatever arguments were passed to the command.

This command will contain whatever logic needs to be carried out. You should validate the arguments in there. After you have the response that you want a user to see, just 'return' it.

Let's say we want to add a command which will take two arguments, we will call it '!random' and it will take a 'minimum' and 'maximum' argument. We will limit this command to be allowed to be called every 20 seconds.

Add the following to the 'commands' dictionary:

'''python
'!random': {
		'limit': 20,
		'argc': 2,
		'return': 'command',
		'ul': 'mod',
		'space_case': True
}
'''

'limit' refers to the cooldown. The cooldown is only active per separate channel
'argc' refers to the number of arguments a command accepts, separated by spaces. If the command does not have 'command' as its 'return' value, this is not necessary. However, even if there are no arguments and 'command' is listed, 0 should be used.
If a command is not intended for use by moderators, there is no need for 'ul' to be included
a 'space_case' is a special scenario where you would like a command to have a single argument, but no limits to the number of separate strings you can input, such as '!requests', wherein directly after you would type an entire set of search items, but they should not be counted as arguments. Normally, arguments are separated by spaces.

Pokemon
=======

Built in are several work-in-progress functions for returning "random battles" of the first generation of Pokemon. The idea, in the end is that a user will have a Pokemon assigned to them that they would catch as one is released randomly in the chat. Users will compete to be the first to catch the Pokemon with a separate command.

Currently, the main command combination to use is "!pokemon battle".

Llama
=====

The Llama family of features is associated with tracking user activity and returning it at will. The data is stored in a SQLite3 database. Every five minutes, if the streamer is currently streaming, points (or "treats") are added incrementally, one every time the function runs as a cron job. For a user to retrieve another user's or their own treats amount, the would type "!llama <username>". If they would like to see a list of the top ten users in descending order, they would type "!llama list".

Type "!llama usage" to find out everything you can do!

'list' - shows a list in descending order of users with most treats
'treats' - shows the user that types the command's treat amount
'me' - shows a user-specific command (if earned/applicable) along with current treats
'stream' - shows description of current stream
'[username]' - shows the typed user's user-specific command (if earned/applicable) along with their current treats
'highlight' - returns a random highlight from the channel
'viewers' - returns a list of all viewers in a channel
'followers' - returns a list of previous five followers
'usage' - returns 'list, treats, me, stream, [username], highlight, viewers, followers, usage, uptime'
'uptime' - shows how long the current stream has been online

Requests
========

IMPORTANT: The first time running the bot when this command is used, serve.py MUST be run as './serve --noauth_local_webserver' to be able to properly authenticate

Built with YouTube API integration. If a user types "!request <anything you can imagine>", a YouTube video link, along with its associated title will appear in the chat and the result will append to an existing YouTube playlist. This allows a streamer to have a completely automated listening experience as determined by users and mods.
