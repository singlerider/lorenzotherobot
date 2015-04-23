from src.lib.queries.pokemon_queries import *
import globals


def trade(args):
    
    party_position = args[0]
    pokemon_to_trade = args[1]
    asking_level = args[2]
    #trade_transaction(giver, giver_position, receiver, receiver_position)
    try:
        asking_pokemon_id = get_pokemon_id_from_name(pokemon_to_trade)
        if asking_pokemon_id != "Error":
            set_pokemon_trade_status(asking_pokemon_id, asking_level, globals.CURRENT_USER, party_position)
            return "Success. Your Pokemon has been set to 'tradable' for the next 24 hours. Use !check [username] to view your listing!"
        else:
            return "spelling error"
    except Exception, error:
        return "FailFish: " + str(error)
            