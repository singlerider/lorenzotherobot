from src.lib.queries.pokemon_queries import *
import globals


def redeem(args):

    position_to_trade = args[0]
    username_to_trade = args[1]
    position_to_redeem = args[2]

    entry_to_check = []
    tradable_pokemon = show_user_tradable_pokemon(username_to_trade)
    # print "tradable_pokemon", tradable_pokemon
    for entry in tradable_pokemon:
        print "entry", entry

    # print "entry_to_check", entry_to_check
    # print "len(entry_to_check)", entry_to_check
    if len(tradable_pokemon) >= 0:

        receiver_trade_status = get_receiver_trade_status(
            position_to_trade, globals.CURRENT_USER)
        giver_trade_status = get_giver_trade_status(
            position_to_redeem, username_to_trade)

        required_id = giver_trade_status[0][0]
        required_level = giver_trade_status[0][1]
        # print "giver_trade_status", giver_trade_status[0]
        # print "required_id", required_id
        # print "required_level", required_level

        receiver_id = receiver_trade_status[0][0]
        receiver_level = receiver_trade_status[0][1]
        # print "receiver_trade_status", receiver_trade_status
        # print "receiver_id", receiver_id
        # print "receiver_level", receiver_level

        if required_id == receiver_id:
            if receiver_level >= required_level:
                trade_transaction(
                    username_to_trade, position_to_redeem, globals.CURRENT_USER, position_to_trade)
                return "Trade complete!"
            else:
                return "That pokemon's level is not high enough."
        else:
            return "That's not the pokemon being asked for."
    else:
        return username_to_trade + " has no tradable Pokemon!"
