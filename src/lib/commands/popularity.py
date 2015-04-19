from src.lib.twitch import *

def popularity(args):
    
    game = args[0]
    
    if "fresh" in game.lower():
        return "Who is freshnica, culo?"
    elif "singlerider" or "shane" in game.lower():
        return "10 out of 10 B)"
    elif "newyork" or "triforce" in game.lower():
        return "1 out of ResidentSleeper"
    elif "curvy" in game.lower() or game.lower() == "amanda":
        return "Amanda sits just outside of the crazy zone (hovering at a 7.9), but far into the hot zone (10 out of 10), making her an actual unicorn. Catch her now!"
    
    else:
        return get_game_popularity(game)