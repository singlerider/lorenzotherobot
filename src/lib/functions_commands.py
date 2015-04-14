import time

import src.lib.commands
from commands import *
from command_headers import *
import sys
import traceback


def is_valid_command(command):
    if command in commands:
        return True


def update_last_used(command, channel):
    commands[command][channel]['last_used'] = time.time()


def get_command_limit(command):
    return commands[command]['limit']


def is_on_cooldown(command, channel):
    if time.time() - commands[command][channel]['last_used'] < commands[command]['limit']:
        return True
    return False


def get_cooldown_remaining(command, channel):
    return round(commands[command]['limit'] - (time.time() - commands[command][channel]['last_used']))


def command_user_level(command):
    if commands[command]['ul']:
        return True


# def get_user_level(username, channel):
#	if '+o' is in data.stream:
#		return True

def check_has_return(command):
    if commands[command]['return'] and commands[command]['return'] != 'command':
        return True
    return False


def get_return(command):
    return commands[command]['return']


def check_has_args(command):
    if 'argc' in commands[command]:
        return True


def check_is_space_case(command):
    """Check to see if the command is a space case
    by default it's not."""
    return commands[command].get("space_case", False)



def check_has_correct_args(message, command):
    """Check to see if message has the correct number of arguments,
    if the commands[command]['argc'] == 1 then we can handle spaces, otherwise
    arguments are seperated by spaces"""
    argc = commands[command]['argc']

    if check_is_space_case(message):
        # As long as it has a length > 1
        message_without_command = message[len(command):]
        # Cool show
        # length of string wihtout command will have one space and one
        # character min
        return len(message_without_command) > 2
    message = message.split(' ')
    if len(message) - 1 == argc:
        return True
    else:
        return False


def check_has_ul(username, command):
    if 'ul' in commands[command]:
        if 'mod' in commands[command]['ul']:
            return True
    return False


def check_returns_function(command):
    if commands[command]['return'] == 'command':
        return True


def pass_to_function(command, args):
    try:
        command=command[1:]
        print("command:", command)
        print(dir(src.lib.commands))
        module = getattr(src.lib.commands, command)
        print("module:", module)
        function = getattr(module, command)
        print("Function:", function)
        if args:
            return function(args)
        else:
            return function()
    except Exception as error:
        print >> sys.stdout, str(error)
        traceback.print_exc(file=sys.stdout)
        try:
            return "usage for " + command + ": " + commands['!' + command]['usage']
        except:
            return "Command Unavailable"
