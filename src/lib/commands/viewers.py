import src.lib.commands.llama as llama_import


def viewers():
    usage = "!viewers"

    user_dict, user_list = llama_import.get_dict_for_users()

    return str(int(len(user_dict["chatters"]["moderators"])) + int(len(user_dict["chatters"]["viewers"]))) + " viewers are in here. That's it?! Kreygasm"
