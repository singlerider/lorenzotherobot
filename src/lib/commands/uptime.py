from src.lib.twitch import *
import globals

def uptime():
    usage = "!uptime"
    
    channels_excluded = ['shedeviil_09']

    if globals.global_channel not in channels_excluded: 
        uptime = get_stream_uptime()
        channel = globals.global_channel
    
        if get_stream_status():
        
            return "The current !uptime is EXACTLY " + str(uptime)
        else:
            return "The streamer is offline, ya dingus ;)"

    else:
        return
