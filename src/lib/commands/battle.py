from src.lib.queries.pokemon_queries import *
from src.lib.twitch import *
import random

def battle(args):
    
    position = args[0]
    opponent = args[1].lower()
    
    user_dict, user_list = get_dict_for_users()
    
    if opponent in user_list:
        if opponent != globals.CURRENT_USER:
            open_position, occupied_positions = find_open_party_positions(opponent)
            if len(open_position) > 0:
                random_opponent_position = random.choice(occupied_positions)
                nickname_1, pokemon_type1_id_1, pokemon_type2_id_1, pokemon_name_1, pokemon_type1_1, pokemon_type2_1 = user_pokemon_types_summary(globals.CURRENT_USER, position)
                nickname_2, pokemon_type1_id_2, pokemon_type2_id_2, pokemon_name_2, pokemon_type1_2, pokemon_type2_2 = user_pokemon_types_summary(opponent, random_opponent_position)
                attacker_stats = get_battle_stats(globals.CURRENT_USER, position)
                defender_stats = get_battle_stats(opponent, random_opponent_position)
                attacker_modifier = pokemon_type1_id_1
                defender_modifier = pokemon_type1_id_2
                attacker_multiplier = get_attacker_multiplier(attacker_modifier, defender_modifier)
                defender_multiplier = get_defender_multiplier(attacker_modifier, defender_modifier)
                total_attacker = sum(attacker_stats[2:7])*attacker_multiplier
                total_defender = sum(defender_stats[2:7])*defender_multiplier
                # print "opponent ", opponent, ", random opponent position ", random_opponent_position, ", attacker types ", user_pokemon_types_summary(globals.CURRENT_USER, position), ", defender types ", user_pokemon_types_summary(opponent, random_opponent_position), ", attacker_stats ", attacker_stats, ", defender_stats ", defender_stats 
                # print "attacker_modifier ", attacker_modifier, ", defender_modifier ", defender_modifier, ", attacker_multiplier ", attacker_multiplier, ", defender_multiplier ", defender_multiplier
                if total_attacker == total_defender:
                    return globals.CURRENT_USER + "'s " + nickname_1 + " and " + opponent + "'s " + nickname_2 + " had a draw."
                elif total_attacker > total_defender:
                    #level_up_user_pokemon(globals.CURRENT_USER, position)
                    return globals.CURRENT_USER + "'s " + nickname_1 + " defeated " + opponent + "'s " + nickname_2 + "."
                elif total_attacker < total_defender:
                    return globals.CURRENT_USER + "'s " + nickname_1 + " was defeated by " + opponent + "'s " + nickname_2 + "."
            else:
                return opponent + "has nothing to battle with. Tell them to use !catch"
        else:
            return "You can't battle yourself."
        return "total attacker ", total_attacker, "total defender ", total_defender
    else:
        return "Your opponent must be in this channel."
    