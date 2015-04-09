from src.lib.queries.pokemon_queries import *
from src.lib.queries.points_queries import *
import globals
import src.lib.commands.pokemon as pokemon_import

usage = "!tallgrass [treatsamount]"

def tallgrass_release(generated_pokemon):
    globals.CAUGHT = False
    globals.POKEMON = generated_pokemon
    return "A wild " + generated_pokemon + " appeared!"

def tallgrass(args):
    points_to_sacrifice = abs(int(args[0])) * -1
    username = globals.CURRENT_USER
    weighted_choices = [(0,1),(1,20),(2,50),(3,100)]
    actual_points = get_user_points(username)
    treats_removed = " " + str(points_to_sacrifice) + " treats from " + str(username) + "!"
    
    if abs(points_to_sacrifice) >= 1000:
        print "abs(points_to_sacrifice) > 1000:", abs(points_to_sacrifice)
        if actual_points >= abs(points_to_sacrifice):
            generated_pokemon = spawn_tallgrass(0)
            modify_user_points(username, points_to_sacrifice)
            return tallgrass_release(generated_pokemon) + treats_removed
        else:
            return "Sorry, but you need more treats to do that."
    elif abs(points_to_sacrifice) >= 100:
        print "abs(points_to_sacrifice) > 100:", abs(points_to_sacrifice)
        if abs(points_to_sacrifice) <= 500:
            print "abs(points_to_sacrifice) <= 500:", abs(points_to_sacrifice)
            if actual_points >= abs(points_to_sacrifice):
                generated_pokemon = spawn_tallgrass(1)
                modify_user_points(username, points_to_sacrifice)
                return tallgrass_release(generated_pokemon) + treats_removed
            else:
                return "Sorry, but you need more treats to do that."
        else:
            return "You're in an open field. No tall grass between 501 and 999 Treats!"
    elif abs(points_to_sacrifice) < 100:
        print "abs(points_to_sacrifice) < 100:", abs(points_to_sacrifice)
        if abs(points_to_sacrifice) >= 25:
            "abs(points_to_sacrifice) >= 25:", abs(points_to_sacrifice)
            if actual_points >= abs(points_to_sacrifice):
                generated_pokemon = spawn_tallgrass(2)
                modify_user_points(username, points_to_sacrifice)
                return tallgrass_release(generated_pokemon) + treats_removed
            else:
                return "Sorry, but you need more treats to do that."
        elif abs(points_to_sacrifice) > 4:
            "abs(points_to_sacrifice) > 4:", abs(points_to_sacrifice)
            if actual_points >= abs(points_to_sacrifice):
                generated_pokemon = spawn_tallgrass(3)
                modify_user_points(username, points_to_sacrifice)
                return tallgrass_release(generated_pokemon) + treats_removed
            else:
                return "Sorry, but you need more treats to do that."
        else:
            return "Dude, don't be cheap. Spare 5 treats."
    else:
        return "Treats to sacrifice must be a number higher than 5."