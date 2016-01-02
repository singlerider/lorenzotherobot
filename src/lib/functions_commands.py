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
    commands[command][channel]["last_used"] = time.time()


def get_command_limit(command):
    return commands[command]["limit"]


def is_on_cooldown(command, channel):
    if time.time() - commands[command][channel]["last_used"] < commands[command]["limit"]:
        return True
    return False


def get_cooldown_remaining(command, channel):
    return round(commands[command]["limit"] - (time.time() - commands[command][channel]["last_used"]))


def check_has_user_cooldown(command):
    if "user_limit" in commands[command]:
        return True
    else:
        return False


def is_on_user_cooldown(command, channel, username):
    if username not in user_cooldowns["channels"][channel]["commands"][
            command]["users"]:
        return False
    elif time.time() - user_cooldowns["channels"][channel]["commands"][
            command]["users"][username] < commands[command]["user_limit"]:
        return True
    return False


def get_user_cooldown_remaining(command, channel, username):
    time_remaining = int(round(commands[command]["user_limit"] - (
        time.time() - user_cooldowns["channels"][channel]["commands"][
                command]["users"][username])))
    return time_remaining


def update_user_last_used(command, channel, username):
    user_cooldowns["channels"][channel]["commands"][
            command]["users"][username] = time.time()

def command_user_level(command):
    if commands[command]["ul"]:
        return True


def check_has_return(command):
    if commands[command]["return"] and commands[command]["return"] != "command":
        return True
    return False


def get_return(command):
    return commands[command]["return"]


def check_has_args(command):
    if "argc" in commands[command]:
        return True


def check_is_space_case(command):
    """Check to see if the command is a space case
    by default it is not."""
    return commands[command].get("space_case", False)


def check_has_optional_args(command):
    if "optional" in commands[command]:
        return True
    else:
        return False


def check_has_correct_args(message, command):
    """Check to see if message has the correct number of arguments,
    if the commands[command]["argc"] == 1 then we can handle spaces, otherwise
    arguments are seperated by spaces"""
    argc = commands[command]["argc"]

    if check_has_optional_args(command):
        message_without_command = message[len(command):]
        return len(message_without_command) - 1

    else:
        if check_is_space_case(message):
            message_without_command = message[len(command):]
            return len(message_without_command) > 2
        message = message.split(" ")
        if len(message) - 1 == argc:
            return True
        else:
            return False


def check_has_ul(username, command):
    if "ul" in commands[command]:
        if "mod" in commands[command]["ul"]:
            return True
    return False


def check_returns_function(command):
    if commands[command]["return"] == "command":
        return True


def pass_to_function(command, args):
    try:
        if len(command) < 2:
            command = []
        else:
            command = command[1:]
        module = getattr(src.lib.commands, command)
        function = getattr(module, command)
        if args:
            return function(args)
        else:
            if check_has_optional_args("!" + command.lstrip("!")):
                function = getattr(module, command)
                args = []
                return function(args)
            return function()
    except Exception as error:
        print >> sys.stdout, str(error)
        traceback.print_exc(file=sys.stdout)
        try:
            return "How to use " + command + ": " + commands[
                "!" + command]["usage"]
        except:
            return "Command Unavailable"
