from src.lib.twitch import *

def followers():
    usage = "!followers"

    stream_followers = get_stream_followers()
    follower_list = str(stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(stream_followers[
        "follows"][2]["user"]["display_name"]) + ", " + str(stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(stream_followers["follows"][4]["user"]["display_name"])
    
    full_follower_list = stream_followers['follows'][0:99]
    appended_list = []
    for follower in full_follower_list:
        appended_list.append(follower['notifications'])
    print appended_list.count(True)
    
    return globals.channel + "'s most recent followers: " + follower_list + ". " + str(appended_list.count(True)) + "% of the last 100 followers have opted for notifications."
