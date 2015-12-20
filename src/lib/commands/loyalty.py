from src.lib.queries.points_queries import *
import globals


def loyalty(args):
    user = args[0]
    streamer_time = get_time_in_chat(globals.global_channel)
    viewer_time = get_time_in_chat(user)
    try:
        int(streamer_time)
        int(viewer_time)
    except Exception as error:
        print error, streamer_time, viewer_time
        return "I can't seem to find that user, which means they aren't loyal. Off with their 4Head !"
    loyalty = str(float(viewer_time) / (float(streamer_time)) * 100) + "%"
    return "{0} has been watching for a total of {1} minutes, compared to {2}'s {3} minutes of combined streams. That's {4} loyalty!".format(
        user, viewer_time, globals.global_channel, streamer_time, loyalty)
