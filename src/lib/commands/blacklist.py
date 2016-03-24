from src.lib.queries.blacklist_queries import (
    add_to_blacklist, remove_from_blacklist)


def blacklist(args, **kwargs):
    action = args[0]
    user_to_block = args[1]

    if action == "add" or action == "remove":
        if kwargs.get("username") == user_to_block:
            return
        if action == "add":
            add_to_blacklist(user_to_block)
        if action == "remove":
            remove_from_blacklist(user_to_block)
    return
