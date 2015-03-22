import src.lib.commands.request as request


def songrequest(args):

    usage = '!songrequest [artist name and song title]'

    return request.request(args)
