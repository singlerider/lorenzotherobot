from src.lib.queries.pokemon_queries import *
from src.lib.queries.points_queries import *

usage = '!gift [username] [pokemon_name] [level]'


def gift(args):

    username = str(args[0].lower())
    open_position, occupied_positions = find_open_party_positions(username)
    name = args[1]
    level = abs(int(args[2]))

    try:
        get_user_points(username)

        if name == "item":
            id = args[2]
            return gift_items(id, username)
        else:
            if len(open_position) > 0:
                if level <= 100:
                    try:
                        get_pokemon_id_from_name(name)
                        id_from_name = get_pokemon_id_from_name(name)
                        globals.CAUGHT = True
                        return insert_user_pokemon(username, username, open_position[0], id_from_name, level, id_from_name, None, None)
                    except:
                        return "Check your spelling and capitalization!"
                else:
                    return "There is a level cap of 100"
            else:
                return "No open slots in their party."
    except:
        return "Are you sure that user exists?"
