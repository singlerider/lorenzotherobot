from src.lib.queries.pokemon_queries import *
import globals
from datetime import datetime, timedelta


def reset_timestamp():
    now = datetime.utcnow()
    reset_countdown = now - timedelta(minutes=1440)
    reset_trade_timestamp(reset_countdown)


def cron(a=None):
    reset_timestamp()


def trade(args):

    trade_set_time = str(datetime.utcnow())

    party_position = args[0]
    pokemon_to_trade = args[1]
    asking_level = args[2]
    #trade_transaction(giver, giver_position, receiver, receiver_position)
    try:
        try:
            if int(args[0]) and int(args[2]):
                if int(args[2]) <= 100:
                    if int(args[2]) >= 5:
                        asking_pokemon_id = get_pokemon_id_from_name(
                            pokemon_to_trade)
                        if asking_pokemon_id != "Error":
                            set_pokemon_trade_status(
                                trade_set_time, asking_pokemon_id, asking_level, globals.CURRENT_USER, party_position)
                            return "Success. Your Pokemon has been set to 'tradable' for the next 24 hours. Use !check [username] to view your listing!"
                        else:
                            return "spelling error"
                    else:
                        return "The requested level must be at least 5."
                else:
                    return "The requested level must be lower than 100."
        except:
            return "Position and requested level must be numbers!"
    except Exception, error:
        return "FailFish: " + str(error)
