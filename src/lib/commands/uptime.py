from src.lib.twitch import *


def uptime(**kwargs):
    channel = kwargs.get("channel", "testchannel")
    uptime = get_stream_uptime(channel)
    if uptime is not None:
        return "The current !uptime is " + str(uptime)
    else:
        return channel + " is offline!"
