from src.lib.twitch import *

def viewers():
    usage = "!viewers"

    user_dict, all_users = get_dict_for_users()
    
    chatter_count = user_dict['chatter_count']

    return str(chatter_count) + " chatters are in here. That's it?! PogChamp"
