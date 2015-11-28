from src.lib import llama as llamadb
import src.lib.twitch as twitch
from src.lib.queries.points_queries import *
import globals


def donation(args):
    user = args[0]
    amount = args[1]
    try:
        amount = int(amount)
    except:
        return "amount has to be a number, ya dingus!"
    if globals.global_channel == 'curvyllama':
        mod_name = globals.CURRENT_USER
        user_dict, __ = get_dict_for_users(None)
        treats_to_add = int(amount/10) * 750
        modify_user_points(user, treats_to_add)
        return "{} treats for {}!".format(treats_to_add, user)
