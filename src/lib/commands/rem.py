from src.lib.queries.command_queries import *


def rem(args):
    command = args[0].lower()
    return delete_command(command)
