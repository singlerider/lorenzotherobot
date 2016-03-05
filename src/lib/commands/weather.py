import json
import random

import requests
from globals import weather_key


def weather(args, **kwargs):
    remarks = ["That's pretty neat!", "How neat is that?"]
    units = args[0].lower()
    query = " ".join(args[1:]).lower()
    try:
        query = "{0},us".format(int(query))
    except:
        pass
    if units == "metric" or units == "imperial":
        url = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}".format(
            query, weather_key, units)
        resp = requests.get(url)
        data = json.loads(resp.content)
        current_temp = data["main"]["temp"]
        condition = (data["weather"][0]["description"]).lower()
        place = data["name"]
        statement = "Dude, it's {0} in {1} right now and the conditions are {2}. {3}".format(
            current_temp, place, condition, random.choice(remarks))
        return statement
    else:
        return "You must specify 'imperial' or 'metric' units (ex: '!weather imperial Moscow)''"
