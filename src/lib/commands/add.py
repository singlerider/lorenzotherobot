import globals
import src.lib.command_headers as command_headers
from src.lib.queries.command_queries import *


def add(args):
    command = args[0].lower()
    user_level = args[1]
    response = " ".join(args[2:])
    creator = globals.CURRENT_USER
    if command[0] is "!":
        if command not in command_headers.commands:
            if user_level == "reg" or user_level == "mod":
                return save_command(command, creator, user_level, response)
            else:
                return "User level must be 'reg' or 'mod'"
        else:
            return "{} already built in to Lorenzo.".format(command)
    else:
        return "Command must begin with '!'"
