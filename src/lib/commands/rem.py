from src.lib.queries.command_queries import *
import src.lib.command_headers as command_headers
import globals


def rem(args):
    command = args[0].lower()
    return delete_command(command)
