from src.lib.twitch import *
import globals


def highlight():
    if globals.global_channel == 'shedeviil_09':
        return None

    usage = "!highlight"

    uptime = get_stream_uptime()
    form_url = "http://goo.gl/UyWYKg"
    channel = globals.global_channel

    if get_stream_status():

        return "The current !uptime is '" + str(uptime) + "'. Head to " + form_url + " and input the current !uptime result in the form for " + channel + "!"
    else:
        return "If you'd like to report a hightlight. Head to " + form_url + " and submit the timestamp for " + channel + "!"
