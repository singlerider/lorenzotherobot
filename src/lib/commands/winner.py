import llama as llama_import
import random

usage = "!winner"

def winner():
    if globals.global_channel == 'shedeviil_09':
        return None
    user_dict, all_users = llama_import.get_dict_for_users()
    stream_winner = random.choice(all_users)
    random.shuffle(all_users)

    return stream_winner
