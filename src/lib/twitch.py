import globals
import requests
import json
import random
import datetime
from src.bot import *
import src.lib.user_commands as user_commands_import

user_data_name = globals.CURRENT_USER

def get_dict_for_users():

    get_dict_for_users_url = 'http://tmi.twitch.tv/group/user/' + globals.channel + '/chatters'
    get_dict_for_users_resp = requests.get(url=get_dict_for_users_url)
    users = json.loads(get_dict_for_users_resp.content)
    user_dict = users
    user_list = users['chatters']['moderators']+users['chatters']['viewers']
    print user_list
    return user_dict, user_list

def get_stream_status():
    get_stream_status_url = 'https://api.twitch.tv/kraken/streams/' + \
        globals.channel
    get_stream_status_resp = requests.get(url=get_stream_status_url)
    online_data = json.loads(get_stream_status_resp.content)
    if online_data["stream"] != None:
        return True


def get_stream_uptime():
    if get_stream_status():
        format = "%Y-%m-%d %H:%M:%S"
        get_stream_uptime_url = 'https://api.twitch.tv/kraken/streams/' + \
            globals.channel
        get_stream_uptime_resp = requests.get(url=get_stream_uptime_url)
        uptime_data = json.loads(get_stream_uptime_resp.content)
        start_time = str(uptime_data['stream']['created_at']).replace(
            "T", " ").replace("Z", "")
        stripped_start_time = datetime.datetime.strptime(start_time, format)
        time_delta = datetime.datetime.utcnow() - stripped_start_time
        return "The stream has been live for EXACTLY " + str(time_delta) + "!"
    else:
        return "She's offline, duh."


def get_offline_status():
    get_offline_status_url = 'https://api.twitch.tv/kraken/streams/' + \
        globals.channel
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
        globals.channel + '/follows'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    return data


def random_highlight():
    get_highlight_url = "http://api.twitch.tv/kraken/channels/" + \
        globals.channel + "/videos?limit=20"
    get_highlight_resp = requests.get(url=get_highlight_url)
    highlights = json.loads(get_highlight_resp.content)
    random_highlight_choice = random.choice(highlights["videos"])
    return "{title} | {description} | {length} time units | {url} | Tags: {tag_list}".format(**random_highlight_choice).replace("\n"," ").replace("\r", " ")
