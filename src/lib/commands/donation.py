from src.lib import llama as llamadb
import src.lib.twitch as twitch
from src.lib.queries.points_queries import *
import globals


def donation(args):
    user = args[0].lower()
    amount = args[1]
    try:
        amount = int(float(amount.lstrip("$")))

    except Exception as error:
        print error
        return "amount has to be a number, ya dingus!"
    if globals.global_channel == 'curvyllama':
        mod_name = globals.CURRENT_USER
        user_dict, __ = get_dict_for_users(None)
        treats_to_add = int(amount/10) * 750
        modify_user_points(user, treats_to_add)
        thanks_message = "Let's get some curvyFireball in the chat for {0}'s ${1} donation!".format(user, amount)
        return "{} treats for {}! {}".format(treats_to_add, user, thanks_message)
