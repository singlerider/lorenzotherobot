from src.lib.queries.pokemon_queries import *
from src.lib.queries.points_queries import *
import globals
from datetime import *

def me():
    usage = "!me"
    
    now = datetime.utcnow()
    
    start_time = get_last_battle(globals.CURRENT_USER)
    print start_time
    print now
    time_delta = now - get_last_battle(globals.CURRENT_USER)
    print now
    print "time delta", time_delta
    set_battle_timestamp(globals.CURRENT_USER, now)
    return time_delta
    # args = llama_import.user_data_name

    # if llama_import.llama.grab_user in llama_import.llama.user_commands_import.user_command_dict:
    #    return llama_import.user_commands_import.user_command_dict[llama_import.llama.grab_user]["return"] + " | " + llama_import.llama.user_return
    # else:
    #    return llama_import.llama.user_return
    # return llama_import.get_user_command()
    # return set_user_points()
    # return get_user_party_info(globals.CURRENT_USER)
    # return remove_user_pokemon()
    # return get_battle_stats()
    # return get_user_points(globals.CURRENT_USER)
    # return user_pokemon_types_summary()
    # return user_pokemon_types_summary(globals.CURRENT_USER, 1)
    # return "use '!party members' instead"
    

def get_stream_uptime():
    if get_stream_status():
        format = "%Y-%m-%d %H:%M:%S"
        get_stream_uptime_url = 'https://api.twitch.tv/kraken/streams/' + \
            globals.channel
        get_stream_uptime_resp = requests.get(url=get_stream_uptime_url)
        uptime_data = json.loads(get_stream_uptime_resp.content)
        start_time = str(uptime_data['stream']['created_at']).replace(
            "T", " ").replace("Z", "")
        stripped_start_time = datetime.datetime.strptime(start_time, format)
        time_delta = datetime.datetime.utcnow() - stripped_start_time
        return "The stream has been live for EXACTLY " + str(time_delta) + "!"
    else:
        return "She's offline, duh."
    