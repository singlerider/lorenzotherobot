from src.lib.queries.command_queries import delete_command


def rem(args, **kwargs):
    channel = kwargs.get("channel", "testchannel")
    command = args[0].lower()
    return delete_command(command, channel)
