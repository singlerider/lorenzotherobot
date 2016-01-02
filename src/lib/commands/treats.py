import src.lib.twitch as twitch
from src.lib.queries.points_queries import *
import globals


def cron(channel):
    try:
        channel = channel.lstrip("#")
        treatsForAllTimer(channel, 1)
    except:
        pass


def treatsForAll(channel, delta):
    user_dict, all_users = twitch.get_dict_for_users(channel)
    try:
        modify_points_all_users(all_users, delta)
        return "{0} treats for everyone!".format(delta)
    except:
        return "Twitch's backend is down. Treats can't be added in this state. Moderators should monitor http://twitchstatus.com/ for updates."


def treatsForAllTimer(channel, delta):
    if twitch.get_stream_status(channel):
        user_dict, all_users = twitch.get_dict_for_users(channel)
        try:
            modify_points_all_users_timer(all_users, delta)
            # print "Treats added to " + str(all_users)
        except:
            return "Twitch's backend is down. Treats can't be added in this state. Moderators should monitor http://twitchstatus.com/ for updates."


def treats(args):
    add_remove = args[0]
    delta_user = args[1].lower()
    try:
        delta = int(args[2])
    except:
        return "amount has to be a number, ya dingus!"
    mod_name = globals.CURRENT_USER
    user_dict, all_users = get_dict_for_users()
    if add_remove == "add":
        if delta_user == "all":
            modify_points_all_users(all_users, abs(delta))
        else:
            modify_user_points(delta_user, abs(delta))
    elif add_remove == "remove":
        delta *= -1
        modify_user_points(delta_user, abs(delta) * -1)
    elif add_remove == "set":
        set_user_points(delta_user, delta)
    return "{} treats for {}!".format(delta, delta_user)
