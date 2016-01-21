import globals
import src.lib.command_headers as command_headers
from src.lib.queries.command_queries import *


def rem(args):
    command = args[0].lower()
    return delete_command(command)
