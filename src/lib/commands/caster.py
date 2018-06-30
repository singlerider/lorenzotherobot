from src.lib.twitch import get_stream_game


def caster(args, **kwargs):
    name = args[0]
    game = get_stream_game(name)
    current_game_str = ""
    if game:
        current_game_str = " They're currently playing {0}".format(game)
    return (
        "THANK YOU {0} for the support!!! Go give their page some love at "
        "twitch.tv/{0} !{1}"
    ).format(name, current_game_str)
