from src.lib.twitch import *
import globals

def uptime():
    usage = "!uptime"
    
    uptime = get_stream_uptime()
    form_url = "http://goo.gl/UyWYKg"
    channel = globals.channel
    
    if get_stream_status():
        
        return "The current !uptime is '" + str(uptime) + "'. Why not head to " + form_url + " and input the !uptime result in the form for " + channel + "?"
    else:
        return "She's offline, but if you'd like to submit a hightlight, head to " + form_url + " and submit the timestamp for " + channel + "!"