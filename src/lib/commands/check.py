from src.lib.queries.pokemon_queries import *
import globals

def check(args):
    
    if args[0] == 'trades':
        all_tradable_pokemon = show_all_tradable_pokemon()
        all_tradable_pokemon_comprehension = ["{}".format(user) for user, giverpoke, pos, askingpoke, askinglevel in all_tradable_pokemon]
        all_tradable_pokemon_set = set([x for x in all_tradable_pokemon_comprehension])
        return " | ".join(all_tradable_pokemon_comprehension)
        #('singlerider', 'Vaporeon', 1, 'Psyduck', 14L)
    elif args[0] == 'market':
        return show_all_pokemon_for_sale()
    elif args[0] == 'items':
        for_sale = check_items()
        for_sale_comprehension = ["({}) {}, {}".format( int(x),y.replace(' ', ''), int(z)) for x,y,z in for_sale]
        return " | ".join(for_sale_comprehension)
    elif args[0] == 'inventory':
        return "Coming soon"
    else:
        username = args[0].lower()
        user_tradable_pokemon = show_user_tradable_pokemon(username)
        user_tradable_pokemon_comprehension = ["({}) {}, {}, lvl {})".format(int(pos), str(giverpoke), str(askingpoke), int(askinglevel)) for user,giverpoke, pos, askingpoke, askinglevel in user_tradable_pokemon]
        return username + "'s listings ordered by position, listed Pokemon, asking Pokemon, asking level: " + str(" | ".join(user_tradable_pokemon_comprehension))