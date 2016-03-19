import random
from datetime import timedelta, datetime

from src.lib.queries.pokemon_queries import *
from src.lib.twitch import get_dict_for_users


def battle(args, **kwargs):
    position = int(args[0])
    opponent = args[1].lower().lstrip("@")
    all_users = []
    username = kwargs.get("username", "testuser")
    channel = kwargs.get("channel", "testchannel")
    user_dict, all_users = get_dict_for_users(channel)
    now = datetime.now()
    cooldown_time = 3
    last_battle_time = get_last_battle(username)
    WHISPER = kwargs.get("WHISPER", False)
    if last_battle_time < now - timedelta(minutes=cooldown_time):
        if opponent in all_users or WHISPER is True:
            if opponent != username:
                available_positions, occupied_positions = find_open_party_positions(
                    opponent)
                if len(occupied_positions) > 0:
                    eligible_positions = []
                    attacker_stats = get_battle_stats(
                        username, position)
                    for spot in occupied_positions:
                        all_defender_stats = get_battle_stats(
                            opponent, int(spot[0]))
                        if attacker_stats[0] - all_defender_stats[0] < 5:
                            if attacker_stats[0] - \
                                    all_defender_stats[0] > -5:
                                eligible_positions.append(spot[0])
                    if len(eligible_positions) > 0:
                        random_opponent_position = random.choice(
                            eligible_positions)
                    else:
                        recommended_fighters = []
                        them = get_user_battle_info(opponent)
                        you = get_user_battle_info(username)
                        for __, defender in them:
                            for pos, attacker in you:
                                if attacker - defender < 5:
                                    if attacker - defender > - 5:
                                        recommended_fighters.append(pos)
                        if len(recommended_fighters) > 0:
                            return "You can only battle an opponent with a Pokemon within 5 levels of your attacker! Try using your position {}!".format(
                                random.choice(recommended_fighters))
                        else:
                            return "Either you are too high of a level or not high enough to battle anything {} has! Try someone else?".format(
                                opponent)
                    nickname_1, pokemon_type1_id_1, pokemon_type2_id_1, pokemon_name_1, pokemon_type1_1, pokemon_type2_1 = user_pokemon_types_summary(
                        username, position)
                    nickname_2, pokemon_type1_id_2, pokemon_type2_id_2, pokemon_name_2, pokemon_type1_2, pokemon_type2_2 = user_pokemon_types_summary(
                        opponent, random_opponent_position)
                    defender_stats = get_battle_stats(
                        opponent, random_opponent_position)
                    attacker_modifier = pokemon_type1_id_1
                    defender_modifier = pokemon_type1_id_2
                    attacker_multiplier = get_attacker_multiplier(
                        attacker_modifier, defender_modifier)
                    defender_multiplier = get_defender_multiplier(
                        attacker_modifier, defender_modifier)
                    total_attacker = sum(
                        attacker_stats[2:7]) * attacker_multiplier
                    total_defender = sum(
                        defender_stats[2:7]) * defender_multiplier
                    set_battle_timestamp(username)
                    if total_attacker == total_defender:
                        return username + "'s " + nickname_1 + \
                            " and " + opponent + "'s " + nickname_2 + " had a draw."
                    elif total_attacker > total_defender:
                        if attacker_stats[0] < 100:  # attacker's level
                            level_up_user_pokemon(
                                username, position)
                        add_win(username)
                        return username + "'s " + nickname_1 + \
                            " defeated " + opponent + "'s " + nickname_2 + "."
                    elif total_attacker < total_defender:
                        add_loss(username)
                        return username + "'s " + nickname_1 + \
                            " was defeated by " + opponent + "'s " + nickname_2 + "."
                else:
                    return opponent + " has nothing to battle with. Tell them to use !catch"
            else:
                return "You can't battle yourself."
        else:
            return "Your opponent must be in this channel."
    else:
        return "It takes " + str(cooldown_time) + \
            " minutes for your Pokemon to heal!"
