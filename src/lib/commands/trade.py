import datetime
from datetime import timedelta

from src.lib.queries.pokemon_queries import *


def reset_timestamp():
    now = datetime.datetime.utcnow()
    reset_countdown = now - timedelta(minutes=1440)
    reset_trade_timestamp(reset_countdown)


def cron(a=None):
    reset_timestamp()


def trade(args, **kwargs):
    username = kwargs.get("username", "testuser")
    trade_set_time = str(datetime.datetime.utcnow())
    party_position = args[0]
    pokemon_to_trade = args[1]
    asking_level = args[2]
    try:
        try:
            if int(args[0]) and int(args[2]):
                if int(args[2]) <= 100:
                    if int(args[2]) >= 5:
                        asking_pokemon_id = get_pokemon_id_from_name(
                            pokemon_to_trade)
                        if asking_pokemon_id != "Error":
                            set_pokemon_trade_status(
                                trade_set_time,
                                asking_pokemon_id,
                                asking_level,
                                username,
                                party_position)
                            return "Success. Your Pokemon has been set to 'tradable' for the next 24 hours. Use !check [username] to view your listing!"
                        else:
                            return "spelling error"
                    else:
                        return "The requested level must be at least 5."
                else:
                    return "The requested level must be lower than 100."
        except:
            return "Position and requested level must be numbers!"
    except Exception as error:  # pragma: no cover
        return "FailFish: " + str(error)
