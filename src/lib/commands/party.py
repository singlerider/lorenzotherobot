from src.lib.queries.pokemon_queries import *


def cron(a=None):
    return "New to the channel? Use '!catch', then '!battle' one of my party members: " + \
        str(get_user_party_info("lorenzotherobot"))


def party(args, **kwargs):
    username = kwargs.get("username", "testuser")
    if len(args) < 1:
        party_members = get_user_party_info(username)
        return party_members
    position = args[0].lstrip("@")
    party_size = 6
    if position in [str(n + 1) for n in range(party_size)]:
        nickname, pokemon_type1_id, pokemon_type2_id, pokemon_name, pokemon_type1, pokemon_type2 = user_pokemon_types_summary(
            username, position)
        level, nickname, hp, speed, attack, defense, special_attack, special_defense = get_battle_stats(
            username, position)
        return "lvl " + str(level) + " " + pokemon_name.decode("utf8") + ": HP " + str(hp) + ", Att " + str(attack) + ", Spd " + str(speed) + \
            ", Def " + str(defense) + ", SpAtt " + str(special_attack) + ", SpDef " + \
            str(special_defense) + ", " + pokemon_type1 + ", " + pokemon_type2
    elif args[0] == 'members':
        party_members = get_user_party_info(username)
        return party_members
    else:
        try:
            party = get_user_party_info(position)
            if len(party) > 0:
                return party
            else:
                return "User not found. Check your spelling"
        except Exception as err:
            print Exception, err
            return "Usage: " + usage
