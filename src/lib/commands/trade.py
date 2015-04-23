from src.lib.queries.pokemon_queries import *
import globals


def trade(args):
    
    party_position = args[0]
    pokemon_to_trade = args[1]
    asking_level = args[2]
    
    if args[0] == 'redeem':
        
        username = args[1]
        position = args[2]
        #"!trade [party_position/'redeem'] [pokemon_to_trade/username] [asking_level/position_to_redeem]"
        tradeable_positions = []
        tradeable_pokemon = show_user_tradeable_pokemon(username)
        for username, pokemon_name, i, asking_for, asking_level in tradeable_pokemon:
            tradeable_positions.append(i)
        print username, tradeable_positions
        if int(position) == tradeable_positions[0]:
            get_receiver_trade_status(globals.CURRENT_USER)
            trade_transaction(username, position, globals.CURRENT_USER, receiver_position)
        else:
            return "False"
        
        #trade_transaction(giver, giver_position, receiver, receiver_position)
    
    else:
    
        try:
            asking_pokemon_id = get_pokemon_id_from_name(pokemon_to_trade)
            if asking_pokemon_id != "Error":
                set_pokemon_trade_status(asking_pokemon_id, asking_level, globals.CURRENT_USER, party_position)
                return "Success"
            else:
                return "spelling error"
        except Exception, error:
            return "FailFish: " + str(error)
            