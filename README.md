[![Build Status](https://travis-ci.org/singlerider/lorenzotherobot.svg?branch=master)](https://travis-ci.org/singlerider/lorenzotherobot) [![Circle CI](https://circleci.com/gh/singlerider/lorenzotherobot/tree/circle.svg?style=svg)](https://circleci.com/gh/singlerider/lorenzotherobot/tree/circle)

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

Head into `src/config/config.py` and enter the correct channels and cron jobs
you'd like to run, then go into globals.py. Leave `CURRENT_CHANNEL`, `CURRENT_USER`, `VARIABLE`, and
`CHANNEL_INFO` alone.

## Finally

### To run:

`./serve.py`

## Commands

So, what can the bot do? Here are a list of current commands in no particular
order with a description of each (if one is needed):
An asterisk (*) marks a moderator-only command

    !follower: !follower [username]
    !quote: !quote
    !opinion: !opinion
    !llama: !llama [treats/shots/username]
    !test: !test (this is a test command)
    !commands: !commands
    !arbitrary: !arbitrary ['number'/'emote']
    !addquote: !addquote [quote]
    !check: !check ['trades'/'market'/'items'/'inventory'/username]
    !caster: !caster [streamer_username]
    !define: !define [insert_word_here]
    !tallgrass: !tallgrass [number_of_treats_to_sacrifice]
    !nickname: !nickname [position_to_update] [nickname(must not contain spaces)]
    !winner: !winner
    !help: !help
    !popularity: !popularity [name_of_game]
    !followers: !followers
    !trade: !trade [party_position] [requested_pokemon] [minimum_asking_level]
    !catch: !catch
    !stream: !stream
    !buy: !buy [item_number]
    !edit: !edit [!command_name] [user_level (reg/mod)] [response (to add a custom user, use "{}")]
    !uptime: !uptime
    !release: !release [party_position_number_to_be_released] [your_username]
    !add: !add [!command_name] [user_level (reg/mod)] [response (to add a custom user, use "{}") (to include message count, use "[]")]
    !donation: !donation [username] [dollar_amount]
    !party: !party [position_to_check(1-6)/'members'/username]
    !battle: !battle [position_to_battle_with] [opponent_username]
    !gift: !gift [username] [Pokemon_name/'item'] [starting_level/'item_number']
    !rem: !rem [!command_name]]
    !leaderboard: !leaderboard
    !weather: !weather [units (metric/imperial)] [location (any format)]
    !treats: !treats [add/remove/set] [username] [number]
    !use: !use [item_position] [party_position]
    !shots: !shots [add/remove/set] [number]
    !evolve: !evolve [position_to_evolve]
    !report: !report [insert bug report text here]
    !highlight: !highlight
    !redeem: !redeem [party_position_to_trade] [username_to_trade] [party_position_to_redeem_from_user]
    !loyalty: !loyalty [username]

## Make It Do

### Adding your own commands

You're going to need to know basic Python if you want to add your own commands. Open up `src/lib/command_headers.py`. There are examples of pre-made commands in there as examples. The limit parameter is the amount of times a command can be used in seconds, if you don't want a limit to be enforced put in `0`.

If your command is only going to return a string, ex - `'!hello'` returns `'Welcome!'`, don't include the `'argc'` parameter. Place the string you wish to be returned to the user in the `'return'` parameter. For example, if you wanted to create a command such as this and limit it to being used ever 30 seconds, you would add in:

```python
'!hello': {
		'limit': 10,
		'return': 'Welcome!'
}
```

However, if your command has to have some logic implemented and if the command is just going to return whatever a function
returns, set the `'return'` parameter on the command to `'command'`, and set `'argc'` to `0`. If your command is going to
take arguments, ex `'!hello [name]'`, set `'argc'` to `'1'` or however many arguments the command is going to take in.

Make a new file in `'lib/commands/'` and give the filename `'command.py'` where `command` is the command name. If your `'argc'` was set to `0`, don't include `'args'` in the functions parameters, else set the only parameter to `'args'`. Args will contain a list of whatever arguments were passed to the command.

This command will contain whatever logic needs to be carried out. You should validate the arguments in there. After you have the response that you want a user to see, just 'return' it.

Let's say we want to add a command which will take two arguments, we will call it `'!random'` and it will take a `'minimum'` and `'maximum'` argument. We will limit this command to be allowed to be called every 20 seconds.

Add the following to the `'commands'` dictionary in `src/lib/command_headers.py`:

```python
'!random': {
		'limit': 20,
		'argc': 2,
		'return': 'command',
		'ul': 'mod',
		'space_case': True
}
```

`'limit'` refers to the cooldown. The cooldown is only active per separate channel

`'argc'` refers to the number of arguments a command accepts, separated by spaces. If the command does not have `'command'` as its `'return'` value, this is not necessary. However, even if there are no arguments and `'command'` is listed, `0` should be used.

If a command is not intended for use by moderators, there is no need for `'ul'` to be included

a `'space_case'` is a special scenario where you would like a command to have a single argument, but no limits to the number of separate strings you can input. Normally, arguments are separated by spaces.

### Pokemon

Built in are several work-in-progress functions for returning "random battles" of the first generation of Pokemon. The idea, in the end is that a user will have a Pokemon assigned to them that they would catch as one is released randomly in the chat. Users will compete to be the first to catch the Pokemon with a separate command.

    !catch
    !tallgrass [amount] (!tallgrass 1000)
    !party ['members'/ username] (!party singlerider)
    !battle [party position] (!battle 1 lorenzotherobot)
    !leaderboard
    !check ['trades'/'items'/'inventory'] (!check inventory)
    !use [item position] [party position] (!use 11 4)
    !trade [party position] [desired pokemon] [desired level] (!trade 1 Bulbasaur 5)
    !redeem [party_position_to_trade] [username_to_trade] [party_position_to_redeem_from_user] (!redeem 2 singlerider 6)


### Llama

The Llama family of features is associated with tracking user activity and returning it at will. The data is stored in a MySQL database. Every five minutes, if the streamer is currently streaming, points (or "treats") are added incrementally, one every time the function runs as a cron job. For a user to retrieve another user's or their own treats amount, the would type "!llama <username>". If they would like to see a list of the top ten users in descending order, they would type "!llama list".

    !llama
    !llama ['treats'/username/'shots'/'list']
