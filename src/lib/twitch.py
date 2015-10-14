import globals
import requests
import json
import random
import datetime
from src.bot import *
import src.lib.user_commands as user_commands_import

# making this comment from Github's Oval Office

user_data_name = globals.CURRENT_USER


def get_dict_for_users(channel=None):
    if channel != None:
        globals.global_channel = channel.lstrip('#')
    get_dict_for_users_url = 'http://tmi.twitch.tv/group/user/' + \
        globals.global_channel + '/chatters'
    get_dict_for_users_resp = requests.get(url=get_dict_for_users_url)
    try:
        users = json.loads(get_dict_for_users_resp.content)
    except:
        return "Twitch's backend is down. Sorry, dawg. Treats will return once that gets fixed."
    user_dict = users
    all_users = []
    for user in users['chatters']['moderators']:
        all_users.append(str(user))
    for user in users['chatters']['viewers']:
        all_users.append(str(user))
    for user in users['chatters']['staff']:
        all_users.append(str(user))
    for user in users['chatters']['admins']:
        all_users.append(str(user))
    # print "all_users: " + str(all_users)
    return user_dict, all_users


def get_stream_status(channel=None):
    if channel != None:
        globals.global_channel = channel.lstrip('#')
    get_stream_status_url = 'https://api.twitch.tv/kraken/streams/' + \
        globals.global_channel
    get_stream_status_resp = requests.get(url=get_stream_status_url)
    online_data = json.loads(get_stream_status_resp.content)
    if online_data["stream"] != None:
        return True


def get_stream_uptime():
    if get_stream_status():
        format = "%Y-%m-%d %H:%M:%S"
        get_stream_uptime_url = 'https://api.twitch.tv/kraken/streams/' + \
            globals.global_channel
        get_stream_uptime_resp = requests.get(url=get_stream_uptime_url)
        uptime_data = json.loads(get_stream_uptime_resp.content)
        start_time = str(uptime_data['stream']['created_at']).replace(
            "T", " ").replace("Z", "")
        stripped_start_time = datetime.datetime.strptime(start_time, format)
        time_delta = datetime.datetime.utcnow() - stripped_start_time
        return str(time_delta)
    else:
        return "The streamer is offline, duh."


def get_offline_status():
    get_offline_status_url = 'https://api.twitch.tv/kraken/streams/' + \
        globals.global_channel
    get_offline_status_resp = requests.get(url=get_offline_status_url)
    offline_data = json.loads(get_offline_status_resp.content)
    if offline_data["stream"] != None:
        return True


def get_user_command():
    try:
        user_command = user_commands_import.user_command_dict[
            user_data_name]["return"]
        return user_command
    except:
        return "Dude... stop. You don't have a user command... yet. R)"


def get_stream_followers():
    url = 'https://api.twitch.tv/kraken/channels/' + \
        globals.global_channel + '/follows?limit=100'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    return data


def random_highlight():
    get_highlight_url = "http://api.twitch.tv/kraken/channels/" + \
        globals.global_channel + "/videos?limit=20"
    get_highlight_resp = requests.get(url=get_highlight_url)
    highlights = json.loads(get_highlight_resp.content)
    random_highlight_choice = random.choice(highlights["videos"])
    return "{title} | {description} | {length} time units | {url} | Tags: {tag_list}".format(**random_highlight_choice).replace("\n", " ").replace("\r", " ")


def get_game_popularity(game):

    try:
        game_http_request = game.replace(' ', '%20')

        url = 'https://api.twitch.tv/kraken/search/streams?q=' + \
            game_http_request + '&limit=100'
        resp = requests.get(url=url)
        data = json.loads(resp.content)

        first_streamer = str(data["streams"][0]["channel"]["display_name"])
        second_streamer = str(data["streams"][1]["channel"]["display_name"])
        third_streamer = str(data["streams"][2]["channel"]["display_name"])

        first_viewers = str(data["streams"][0]["viewers"])
        second_viewers = str(data["streams"][1]["viewers"])
        third_viewers = str(data["streams"][2]["viewers"])

        top_three = first_streamer + ": " + first_viewers + ", " + second_streamer + \
            ": " + second_viewers + ", " + third_streamer + ": " + third_viewers
        return "The top three streamers playing " + game + " are: " + top_three

    except:
        return "Avoid using special characters and check your spelling."

def get_follower_status(user):
    try:
        url = "https://api.twitch.tv/kraken/users/{}/follows/channels/{}".format(user.lower().lstrip("@"), globals.global_channel)
        resp = requests.get(url=url)
        data = json.loads(resp.content)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                  "Sep". "Oct", "Nov", "Dec"]

        date_split = data["created_at"][:10].split("-")
        year = date_split[0]
        month = months[int(date_split[1]) - 1]
        day = date_split[2]
        follower_since = "{} {}, {}".format(month, day, year)
        notifications = data["notifications"]
        followers = data["channel"]["followers"]

        return "{} has been following {} since {}.".format(user, globals.global_channel, follower_since)
    except:
        return "{} doesn't follow {}.".format(user, globals.global_channel)
