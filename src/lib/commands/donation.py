import src.lib.twitch as twitch
from src.lib.queries.points_queries import *


def donation(args, **kwargs):
    user = args[0].lower().lstrip("@")
    amount = args[1]
    try:
        amount = int(float(amount.lstrip("$")))

    except Exception as error:
        print error
        return "amount has to be a number, ya dingus!"
    treats_to_add = int(amount / 10) * 750
    modify_user_points(user, treats_to_add)
    thanks_message = "Let's get some curvyFireball in the chat for {0}'s ${1} donation!".format(
        user, amount)
    return "{} treats for {}! {}".format(treats_to_add, user, thanks_message)


def cron(a=None):
    import requests
    import json
    import time
    from src.lib.commands.donation import donation
    from src.lib.queries.points_queries import modify_user_points
    import globals

    def cron_donation(args):
        user = args[0].lower()
        amount = args[1]
        try:
            amount = int(float(amount.lstrip("$")))
        except Exception as error:
            print error
        treats_to_add = int(amount / 10) * 750
        modify_user_points(user, treats_to_add)

    def get_donations():
        {
            "data": [
                {
                    "donation_id": "80179029",
                    "created_at": "1438576556",
                    "currency": "USD",
                    "amount": "50",
                    "name": "Thomas",
                    "message": "nice!"
                },
                {
                    "donation_id": "80179019",
                    "created_at": "1438576521",
                    "currency": "USD",
                    "amount": "15.50",
                    "name": "JoeGamer",
                    "message": None
                }
            ]
        }
        token = globals.twitchalerts_token
        # only get donations from the past 20 seconds
        after = int(time.time()) - 20
        url = "https://twitchalerts.com/api/v1.0/donations"
        params = "?access_token={0}&after={1}".format(
            token, after)
        resp = requests.get(url + params)
        data = resp.content
        donations = data["data"]
        return donations

    def apply_donation():
        all_donations = get_donations()
        if len(donations) > 0:
            for single_donation in all_donations:
                user = single_donation["name"]
                amount = single_donation["amount"]
                args = [user.lower(), amount]
                cron_donation(args)

            return "curvyFireball curvyFireball curvyFireball curvyFireball"

    return apply_donation()
