"""
Developed by dustinbcox and Shane Engelman <me@5h4n3.com>
"""

import importlib
import src.lib.commands.shots as shots_import
from src.lib.twitch import *
import src.lib.llama as llamadb

user_commands_import = importlib.import_module('src.lib.user_commands')
# reload(user_commands_import)


def random_highlight():
    get_highlight_url = "https://api.twitch.tv/kraken/channels/" + \
        globals.channel + "/videos?limit=20"
    get_highlight_resp = requests.get(url=get_highlight_url)
    highlights = json.loads(get_highlight_resp.content)
    if len(highlights["videos"]) == 0:
        return "No videos yet!"
    random_highlight_choice = random.choice(highlights["videos"])
    return "{title} | {description} | {length} time units | {url} | Tags: {tag_list}".format(**random_highlight_choice).replace("\n"," ").replace("\r", " ")

def get_user_command():
    try:
        user_command = user_commands_import.user_command_dict[user_data_name]["return"]
        return user_command
    except:
        return "Dude... stop. You don't have a user command... yet. R)"


stream_data = get_stream_status()

def enter_into_database(delta = 5):
    # This could use a more sensible name...
    user_dict, user_list = get_dict_for_users()
    for user in user_list:
        llamadb.newConnection().addPoints(user, delta)

    return str(delta) + " treats added to everyone in the chat! Raise your Kappas! \Kappa/"

def llama(args):
    grab_user = args[0].lower()
    user_data_name = globals.CURRENT_USER.lower()


    usage = "!llama (list, treats, me, stream, [username], highlight, viewers, followers, usage, uptime, shots)"
    llamadbconn = llamadb.newConnection()
    if grab_user == "list":
        return llamadbconn.getTopUsers()
    elif grab_user == "treats":
        return "{}, You've got a total of {} Llama treats. You go, girl!".format(
            user_data_name, llamadbconn.getPoints(user_data_name))

    elif grab_user == "me":
        return get_user_command()
    elif grab_user == "stream":
        get_offline_status_url = 'https://api.twitch.tv/kraken/channels/' + \
            globals.channel
        get_offline_status_resp = requests.get(url=get_offline_status_url)
        offline_data = json.loads(get_offline_status_resp.content)
        try:
            return str(offline_data["status"]) + " | " + str(offline_data["display_name"]) + " playing " + str(offline_data["game"])
        except:
            return "Dude. Either some weird HTTP request error happened, or the letters in the description are in Korean. Kappa"

    elif grab_user == "viewers":
        user_dict, user_list = get_dict_for_users()
        # if user_data_name in user_dict["chatters"]["moderators"]:
        return str(int(len(user_dict["chatters"]["moderators"])) + int(len(user_dict["chatters"]["viewers"]))) + " viewers are in here. That's it?! Kreygasm"
        # return str(str(user_dict["chatters"]["moderators"]) + ", " + str(user_dict["chatters"]["viewers"])).replace("[", "").replace("]", "").replace("'", "")
        # else:
        # return "Only moderators can flood the chat window with a bunch of
        # text :/"
    elif grab_user == "highlight":
        return random_highlight()
    elif grab_user == "followers":
        stream_followers = get_stream_followers()
        followers = []
        for follower in stream_followers["follows"][:5]:
            followers.append(str(follower["user"]["display_name"]))
        follower_list = ", ".join(followers)
        return "In case you missed them, here are the five most recent Llamas: " + follower_list + " HeyGuys"
    elif grab_user == "uptime":
        return get_stream_uptime()

    elif grab_user == "usage":
        return usage

    elif grab_user == "shots":
        if shots_import.return_shots is not None:
            return str(shots_import.return_shots) + " shots left. She's already dru... ResidentSleeper"
        else:
            return "No shots found. Donate before she goes crazy! Kreygasm"
    elif llamadbconn.hasUser(grab_user):
        user_return = "{} has a total of {} Llama treats. Key it up!".format(
            args[0], llamadbconn.getPoints(grab_user))

        if grab_user in user_commands_import.user_command_dict:
            return user_commands_import.user_command_dict[grab_user]["return"] + " | " + user_return
        else:
            return user_return

    else:
        print get_stream_status()
        return "No entry found for " + str(args[0])
