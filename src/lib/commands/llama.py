import src.lib.commands.shots as shots_import
import src.lib.commands.wins as wins_import
import src.lib.queries.points_queries as points_import
from src.lib.twitch import *


def llama(args):
    if len(args) < 1:
        return points_import.get_all_user_points(globals.CURRENT_USER)
    grab_user = args[0].lower()
    if grab_user == "list":
        return points_import.get_points_list()
    elif grab_user == "treats":
        return points_import.get_all_user_points(globals.CURRENT_USER)
    elif grab_user == "shots":
        shot_count = shots_import.readShots()
        if shot_count != 0:
            return str(shots_import.readShots()) + \
                " shots left. She's already dru... ResidentSleeper"
        else:
            return "No shots found. Donate before she goes crazy! DansGame"
    elif points_import.get_user_points(grab_user) is not None:
        rank_data = points_import.get_points_rank(grab_user)
        if rank_data is not None:
            username, points, dense, rank = rank_data
            return "With {points} treats, {username} is  #{rank}!".format(
                username=username, points=points, rank=rank)
        else:
            return "User not found. That makes them the biggest loser!"
    else:
        return "No entry found for " + str(args[0])


def whisper_llama(args):
    username = args[0]
    return points_import.get_all_user_points(username)
