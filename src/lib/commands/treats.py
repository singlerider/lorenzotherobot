from src.lib import llama as llamadb
import src.lib.twitch as twitch
from src.lib.queries.points_queries import *
import globals


def cron():
  treatsForAll(1)

def treatsForAll(delta):
    user_dict, user_list = twitch.get_dict_for_users()
    modify_points_all_users(1)
    #for user in user_list:
    #    llamadb.newConnection().addPoints(user, delta)
    # return str(delta) + " treats added to everyone in the chat! Raise your Kappas! \Kappa/"


def treats(args):

    usage = "!treats (add/remove [username] [amount])"

    approved_list = [
        'curvyllama', 'peligrosocortez', 'singlerider', 'newyork_triforce']

    add_remove = args[0]
    delta_user = args[1].lower()

    try:
      delta = int(args[2])
    except:
      return "amount has to be a number, ya dingus!"

    mod_name = globals.CURRENT_USER

    if mod_name not in approved_list:
        return "Only " + ", ".join(approved_list) + " are allowed to do that!"

    if add_remove == "remove":
      delta *= -1

    if delta_user == "all":
      return treatsForAll(delta)
    else:
      llamadb.newConnection().addPoints(delta_user, delta)

    return "{} treats for {}!".format(delta, delta_user)
