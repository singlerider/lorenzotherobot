from src.lib.queries.pokemon_queries import *
import globals

def check(args):
    
    if args[0] == 'trades':
        return show_all_tradeable_pokemon()
    elif args[0] == 'market':
        return show_all_pokemon_for_sale()
    elif args[0] == 'items':
        
        for_sale = check_items()
        for_sale_comprehension = ["({},{})".format(x.replace(' ', ''), int(y)) for x,y in for_sale]
        return " ".join(for_sale_comprehension)
    else:
        username = args[0].lower()
        return show_user_tradeable_pokemon(username)