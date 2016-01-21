import globals
from src.lib.queries.points_queries import *
from src.lib.queries.pokemon_queries import *

usage = "!tallgrass [treatsamount]"


def tallgrass_release(generated_pokemon):
    globals.channel_info[globals.global_channel]['caught'] = False
    globals.channel_info[globals.global_channel]['pokemon'] = generated_pokemon
    return "A wild " + generated_pokemon + " appeared!"


def tallgrass(args):
    points_to_sacrifice = abs(int(args[0])) * -1
    username = globals.CURRENT_USER
    weighted_choices = [(0, 1), (1, 20), (2, 50), (3, 100)]
    donation_points = get_user_points(username)
    time_points = get_user_time_points(username)
    actual_points = donation_points + time_points
    treats_removed = " " + str(points_to_sacrifice) + \
        " treats from " + str(username) + "!"

    if globals.global_channel == "shedeviil_09":
        return "This only works in Curvyllama's chat. Excuse my dust as I upgrade my systems!"

    if isinstance(actual_points, long):
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
                    return tallgrass_release(
                        generated_pokemon) + treats_removed
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
                    return tallgrass_release(
                        generated_pokemon) + treats_removed
                else:
                    return "Sorry, but you need more treats to do that."
            elif abs(points_to_sacrifice) > 4:
                "abs(points_to_sacrifice) > 4:", abs(points_to_sacrifice)
                if actual_points >= abs(points_to_sacrifice):
                    generated_pokemon = spawn_tallgrass(3)
                    modify_user_points(username, points_to_sacrifice)
                    return tallgrass_release(
                        generated_pokemon) + treats_removed
                else:
                    return "Sorry, but you need more treats to do that."
            else:
                return "Dude, don't be cheap. Spare 5 treats."
        else:
            return "Treats to sacrifice must be a number higher than 5."
    print type(actual_points)
    return "Sorry. That won't work. You need more treats! Stay tuned!"
