Try it out! Code is live at
http://www.twitch.tv/curvyllama
===============================

Roboraj
=======

Lorenzotherobot
===============

This is a simple Twitch chat/irc bot written in python.

Installation
============
* Open up your terminal/shell of choice.
* Install the [http://docs.python-requests.org/en/latest/](Requests library) if you haven't already using `pip install requests`. I tested this application on Python 2.7.5.
* 
* Clone the Git repository.
* Move config/config_example.py to config/config.py. Replace all of the placeholders there with your own username/oauth token/channels to join etc (tips are given in the file).
* Type `chmod +x /serve.py`. To run, you simply need to execute the file by typing `./serve.py`.


Adding your own commands
========================

You're going to need to know basic Python if you want to add your own commands. Open up `lib/command_headers.py`. There are examples of pre-made commands in there as examples. The limit parameter is the amount of times a command can be used in seconds, if you don't want a limit to be enforced put in 0.

If your command is only going to return a string, ex - `!hello` returns `Welcome!`, don't include the `argc` parameter. Place the string you wish to be returned to the user in the `return` parameter. For example, if you wanted to create a command such as this and limit it to being used ever 30 seconds, you would add in:

```python
'!hello': {
		'limit': 10,
		'return': 'Welcome!'
}
```

However, if your command has to have some logic implemented and if the command is just going to return whatever a function returns, set the `return` parameter on the command to `command`, and set `argc` to `0`. If your command is going to take arguments, ex `!hello <name>`, set argc to `1` or however many arguments the command is going to take in.

Make a new file in `lib/commands/` and give the filename `command.py` where command is the command name. If your `argc` was set to `0`, don't include `args` in the functions parameters, else set the only parameter to `args`. Args will contain a list of whatever arguments were passed to the command.

This command will contain whatever logic needs to be carried out. You should validate the arguments in there. After you have the response that you want a user to see, just `return` it.

Let's say we want to add a command which will take two arguments, we will call it `!random` and it will take a `minimum` and `maximum` argument. We will limit this command to be allowed to be called every 20 seconds.

Add the following to the `commands` dictionary:

```python
'!random': {
		'limit': 20,
		'argc': 2,
		'return': 'command'
}
```

Working with Pokemon
====================

Built in are several work-in-progress functions for returning "random battles" of the first generation of Pokemon. The idea, in the end is that a user will have a Pokemon assigned to them that they would catch as one is released randomly in the chat. Users will compete to be the first to catch the Pokemon with a separate command.

Currently, the main command combination to use is "!pokemon battle".
Similarly, users can have have random battles with Street Fighter characters by typing in "!streetfighter".

Llama
=====

The Llama family of features is associated with tracking user activity and returning it at will. The data is stored in a SQLite3 database. Every five minutes, if the streamer is currently streaming, points (or "treats") are added incrementally, one every time the function runs as a cron job. For a user to retrieve another user's or their own treats amount, the would type "!llama <username>". If they would like to see a list of the top ten users in descending order, they would type "!llama list".

Type "!llama usage" to find out everything you can do!

Requests
========

YouTube API integration is currently being built in to append user-requested songs to existing YouTube playlists. Currently, if a user types "!request <anything you can imagine>", a YouTube video link, along with its associated title will appear in the chat.
