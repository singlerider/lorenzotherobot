import globals
from src.lib.queries.pokemon_queries import *


def redeem(args):
    position_to_trade = args[0]
    username_to_trade = args[1]
    position_to_redeem = args[2]
    tradable_pokemon = show_user_tradable_pokemon(username_to_trade)
    if len(tradable_pokemon) >= 0:
        receiver_trade_status = get_receiver_trade_status(
            position_to_trade, globals.CURRENT_USER)
        giver_trade_status = get_giver_trade_status(
            position_to_redeem, username_to_trade)
        required_id = giver_trade_status[0][0]
        required_level = giver_trade_status[0][1]
        receiver_id = receiver_trade_status[0][0]
        receiver_level = receiver_trade_status[0][1]
        if required_id == receiver_id:
            if receiver_level >= required_level:
                trade_transaction(
                    username_to_trade,
                    position_to_redeem,
                    globals.CURRENT_USER,
                    position_to_trade)
                return "Trade complete!"
            else:
                return "That pokemon's level is not high enough."
        else:
            return "That's not the pokemon being asked for."
    else:
        return username_to_trade + " has no tradable Pokemon!"
