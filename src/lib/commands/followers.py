from src.lib.twitch import *


def followers():
    username = kwargs.get("username", "testuser")
    stream_followers = get_stream_followers()
    follower_list = str(
        stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(
        stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(
            stream_followers["follows"][2]["user"]["display_name"]) + ", " + str(
                stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(
                    stream_followers["follows"][4]["user"]["display_name"])
    full_follower_list = stream_followers['follows'][0:99]
    appended_list = []
    for follower in full_follower_list:
        appended_list.append(follower['notifications'])
    mod_return = str(appended_list.count(True)) + \
        "% of the last 100 followers have opted for notifications."
    follower_return = "Most recent followers: " + follower_list + ". "
    user_dict, all_users = get_dict_for_users()
    if username in user_dict['chatters']['moderators']:
        return follower_return + mod_return
    else:
        return follower_return
