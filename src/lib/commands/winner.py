import random

import src.lib.twitch as twitch


def winner(**kwargs):
    user_dict, all_users = twitch.get_dict_for_users()
    stream_winner = random.choice(all_users)
    random.shuffle(all_users)
    return stream_winner
