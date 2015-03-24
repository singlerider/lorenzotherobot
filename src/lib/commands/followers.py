import src.lib.commands.llama as llama_import


def followers():
    usage = "!followers"

    stream_followers = llama_import.get_stream_followers()
    follower_list = str(stream_followers["follows"][0]["user"]["display_name"]) + ", " + str(stream_followers["follows"][1]["user"]["display_name"]) + ", " + str(stream_followers[
        "follows"][2]["user"]["display_name"]) + ", " + str(stream_followers["follows"][3]["user"]["display_name"]) + ", " + str(stream_followers["follows"][4]["user"]["display_name"])
    return "In case you missed them, here are the five most recent Llamas: " + follower_list
