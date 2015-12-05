Try it out! Code is live at
http://www.twitch.tv/curvyllama
===============================

# Lorenzotherobot

This is a Twitch chat/irc bot written in Python (2.6 / 2.7).

## Installation

### Google API
This is for saving logs to your Google Drive directory

#### Python Quickstart

Use the wizard at:

https://console.developers.google.com/flows/enableapi?apiid=drive

to get started creating your application and managing your auth flow.

Once the Google Drive API is enabled, go the the "Credentials" tab in the
Developer's Console.

#### Add Credentials

Click "Add Credentials" and generate an API Key (Server Key) and an OAuth
2.0 Client ID (Other)

Download your generated client_secret json file and rename it to
"client_secrets.json" then place it in your project's root directory - PyDrive
looks for this specific file in this specific place.

### Virtual Environment

I would recommend running this in a virtual environment to keep your
dependencies in check. If you'd like to do that, run:

`sudo pip install virtualenv`

Followed by:

`virtualenv venv`

This will create an empty virtualenv in your project directory in a folder
called "venv." To enable it, run:

`source venv/bin/activate`

and your console window will be in that virtualenv state. To deactivate, run:

`deactivate`

### Dependencies

To install all dependencies locally (preferably inside your activated
virtualenv), run:

`pip install -r requirements.txt`

### Further Steps

Make a copy of the example config file:

`cp src/config/config_example.py src/config/config.py`

Make a copy of the example globals file:

`cp globals_example.py globals.py`

#### MySQL Installation

Depending on your distribution, starting the server will be different, on a mac, this is accomplished by doing

`brew install mysql`

`mysql.server start`

From here, you need to enter the mysql console as root:

`mysql -u root`

Create your database and name it whatever you want:

`CREATE DATABASE databasename;`

Create a user that you will use to connect with the database with (you do not
want to connect as root for security reasons) - replace "newuser" and
"password" with whatever you'd like:

`CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';`

Grant the appropriate privileges for your databases(s) to your new user:

`GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';`

Exit out of the console with:

`\q`

Create your schema from my blank template:

`mysql -u newuser -ppassword databasename < schema.sql`

#### Globals and Config Files

Head into src/config/config.py and enter the correct channels and cron jobs
you'd like to run, then go into globals.py and at the very least replace the
mysql credentials. Leave global_channel, CURRENT_USER, VARIABLE, and
channel_info alone.

## Commands

So, what can the bot do? Here are a list of current commands in no particular
order with a description of each (if one is needed):
An asterisk (*) marks a moderator-only command

    '!report'* [insert bug report text here]
    '!commands'* - has different results, depending on whether or not a moderator sent the command
    '!opinion' - acts as a magic 8 ball
    '!chair'
    '!randomnumber' - returns a random number between 1 and 100
    '!randomemote' - returns a random emote from Twitch's standard emotes library
    '!cry' - BibleThump times a bunch
    '!buyprints' - Link to Streamer's Posters for Sale
    '!playlist' - YouTube playlist
    '!request' ['artist name and song title'] - adds requested search query result to a youtube playlist, specified by bot admin
    '!songrequest' - Same as '!request'
    '!poll'* ['choice 1/choice 2/choice 3'] - mod can establish things for users to vote on from within the chat window
    '!vote' [number] - users simply send a number to decide the choice they'd like
    '!llama' - shows everything the 'llama suite' can do - see below for more detailed instructions
    '!weather' [zip_code] - shows current weather and forecast for any US zip code
    '!specs'
    '!treats'* ['add'/'remove'/'set'] ['username'] [amount] - allows mod to decide how many treats a user either gets added to them or removed
    '!help'
    '!shots'* ['add'/'remove'/'set'] [amount] - allows mod to keep track of how many shots a streamer has remaining
    '!viewers' - Shows a Count of the Number of Viewers
    '!highlight' - Shows a Link to Random Highlight from Streamer's Archive
    '!followers' - Shows Streamer's 5 Most Recent Followers
    '!uptime' - Time Stream has been Online, if it is in fact Online
    '!stream' - Shows Streamer's Current Stream Title

## Make It Do

### Adding your own commands

You're going to need to know basic Python if you want to add your own commands. Open up 'lib/command_headers.py'. There are examples of pre-made commands in there as examples. The limit parameter is the amount of times a command can be used in seconds, if you don't want a limit to be enforced put in 0.

If your command is only going to return a string, ex - '!hello' returns 'Welcome!', don't include the 'argc' parameter. Place the string you wish to be returned to the user in the 'return' parameter. For example, if you wanted to create a command such as this and limit it to being used ever 30 seconds, you would add in:

```python
'!hello': {
		'limit': 10,
		'return': 'Welcome!'
}
```

However, if your command has to have some logic implemented and if the command is just going to return whatever a function returns, set the 'return' parameter on the command to 'command', and set 'argc' to '0'. If your command is going to take arguments, ex '!hello <name>', set argc to '1' or however many arguments the command is going to take in.

Make a new file in 'lib/commands/' and give the filename 'command.py' where command is the command name. If your 'argc' was set to '0', don't include 'args' in the functions parameters, else set the only parameter to 'args'. Args will contain a list of whatever arguments were passed to the command.

This command will contain whatever logic needs to be carried out. You should validate the arguments in there. After you have the response that you want a user to see, just 'return' it.

Let's say we want to add a command which will take two arguments, we will call it '!random' and it will take a 'minimum' and 'maximum' argument. We will limit this command to be allowed to be called every 20 seconds.

Add the following to the 'commands' dictionary:

```python
'!random': {
		'limit': 20,
		'argc': 2,
		'return': 'command',
		'ul': 'mod',
		'space_case': True
}
```

'limit' refers to the cooldown. The cooldown is only active per separate channel
'argc' refers to the number of arguments a command accepts, separated by spaces. If the command does not have 'command' as its 'return' value, this is not necessary. However, even if there are no arguments and 'command' is listed, 0 should be used.
If a command is not intended for use by moderators, there is no need for 'ul' to be included
a 'space_case' is a special scenario where you would like a command to have a single argument, but no limits to the number of separate strings you can input, such as '!requests', wherein directly after you would type an entire set of search items, but they should not be counted as arguments. Normally, arguments are separated by spaces.

### Pokemon

Built in are several work-in-progress functions for returning "random battles" of the first generation of Pokemon. The idea, in the end is that a user will have a Pokemon assigned to them that they would catch as one is released randomly in the chat. Users will compete to be the first to catch the Pokemon with a separate command.

    '!check' ['trades'/'market'/'items'/'inventory'/username] - shows pertinent information related to the argument passed
    '!buy' [item_number] - allows you to apply an item to a Pokemon (Rare candies level you up 10 levels/Stones evolve eligible pokemon)
    '!evolve' [position_number] - evolves a Pokemon if a non-item evolution condition is required and met
    '!use' [item_id] [pokemon_party_position]
        '!use 1 3' - user uses an item with the id of 1 (Fire Stone) on their position 3 Pokemon (Eevee), resulting in an evolution (to Flareon)
        '!use 11 6' - user uses
    '!catch'* - Adds Pokemon to Party if Conditions (if Pokemon is Released / An Empty Slot is Available) are Met
    '!nickname' [position] [nickname_to_give_pokemon(no spaces allowed)
        '!nickname 2 Iggy' - user nicknamed their position 2 pokemon 'Iggy'
    '!party ['members' / position_in_party]' - Displays information about user's party ('members' yields pokemon position and nicknames)([position] yields )
    	'!party 5' - yields stats for the 5th spot in your party.
    '!release [position_in_party] [your_username]' - Allows you to release a member of your party with username entered for confirmation
    	'!release 2 lorenzotherobot' - releases the 2nd slot in lorenzotherobot's own party
    '!trade' [party_position] [requested_pokemon] [minimum_asking_level]
        '!trade 2 Squirtle 5' - Puts your Pokemon in position 2 and requests a Squirtle for trade with a minimum level of 5 (higher levels will still be accepted) - available trades can be searched with '!check trades' and individual user trades can be searched with '!check [username]'
    '!redeem [party_position_to_trade] [username_to_trade] [party_position_to_redeem_from_user]
        '!redeem 2 singlerider 6' - user chooses to redeem their position 2 Pokemon (the one being requested by the trader) for the user, 'singlerider' 's position 6 (the position number listed in the trade) - if all conditions are met, the trade will go through. Traded Pokemon have a flag attached so if there are trade-specific evolution requirements, the Pokemon will then be allowed to evolve

### Llama

The Llama family of features is associated with tracking user activity and returning it at will. The data is stored in a MySQL database. Every five minutes, if the streamer is currently streaming, points (or "treats") are added incrementally, one every time the function runs as a cron job. For a user to retrieve another user's or their own treats amount, the would type "!llama <username>". If they would like to see a list of the top ten users in descending order, they would type "!llama list".

'list' - shows a list in descending order of users with most treats
'treats' - shows the user that types the command's treat amount
'shots' - shows how many shots she has left
username - shows number of treats a user has and if they have a user command, it displays that, too

### Requests (Songs)

IMPORTANT: The first time running the bot when this command is used, serve.py MUST be run as './serve --noauth_local_webserver' to be able to properly authenticate

Built with YouTube API integration. If a user types "!request [anything you can imagine]", a YouTube video with its associated title will appear in the chat and the result will append to an existing YouTube playlist. This allows a streamer to have a completely automated listening experience as determined by users and mods.

## Finally

### To run:

`./serve.py`
