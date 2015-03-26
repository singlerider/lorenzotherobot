import src.lib.commands.llama as llama_import # for channel wide treats
from src.lib import llama as llamadb

import globals


def treats(args):

    usage = "!treats (add/remove [username] [amount])"

    approved_list = [
        'curvyllama', 'peligrosocortez', 'singlerider', 'newyork_triforce']

    add_remove = args[0]
    delta_user = args[1].lower()

    try:
      delta = int(args[2])
    except:
      return "ammount has to be a number, ya dingus!"

    mod_name = globals.CURRENT_USER

    if mod_name not in approved_list:
        return "Only " + ", ".join(approved_list) + " are allowed to do that!"

    if add_remove == "remove":
      delta *= -1

    if delta_user == "all":
      llama_import.enter_into_database_all(delta)
    else:
      llamadb.newConnection().addPoints(delta_user, delta)

    return "{} treats for {}!".format(delta, delta_user)
