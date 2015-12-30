from src.lib.twitch import *
import globals


def uptime():

    uptime = get_stream_uptime()

    if get_stream_status():
        return "The current !uptime is " + str(uptime)
    else:
        return "The streamer is offline!"
