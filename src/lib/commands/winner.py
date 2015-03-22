import llama as llama_import
import random


def winner():
    usage = "!winner"
    user_dict, user_list = llama_import.get_dict_for_users()
    stream_winner = random.choice(user_list)
    random.shuffle(user_list)

    return stream_winner
