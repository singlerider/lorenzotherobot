import globals
from src.lib.twitch import *


def highlight():
    if globals.CURRENT_CHANNEL == 'shedeviil_09':
        return None
    uptime = get_stream_uptime()
    form_url = "http://goo.gl/UyWYKg"
    channel = globals.CURRENT_CHANNEL
    if get_stream_status():
        return "The current !uptime is '" + \
            str(uptime) + "'. Head to " + form_url + \
            " and input the current !uptime result in the form for " + channel + "!"
    else:
        return "If you'd like to report a hightlight. Head to " + \
            form_url + " and submit the timestamp for " + channel + "!"
