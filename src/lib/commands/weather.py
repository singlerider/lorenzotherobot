"""
{
  "coord": {
    "lon": 19.4,
    "lat": 51.71
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "Sky is Clear",
      "icon": "01n"
    }
  ],
  "base": "cmc stations",
  "main": {
    "temp": 273.15,
    "pressure": 1029,
    "humidity": 89,
    "temp_min": 273.15,
    "temp_max": 273.15
  },
  "wind": {
    "speed": 1.5,
    "deg": 200
  },
  "clouds": {
    "all": 0
  },
  "dt": 1449797400,
  "sys": {
    "type": 1,
    "id": 5358,
    "message": 0.0094,
    "country": "PL",
    "sunrise": 1449815911,
    "sunset": 1449844340
  },
  "id": 3101720,
  "name": "Chocianowice",
  "cod": 200
}
"""
from globals import weather_key
import requests
import json
import random


def weather(args):
    remarks = ["That's pretty neat!", "How neat is that?"]
    units = args[0].lower()
    query = " ".join(args[1:]).lower()
    try:
        query = "{0},us".format(int(query))
    except:
        pass
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}".format(
        query, weather_key, units)
    resp = requests.get(url)
    data = json.loads(resp.content)
    current_temp = data["main"]["temp"]
    high_temp = data["main"]["temp_max"]
    low_temp = data["main"]["temp_min"]
    condition = (data["weather"][0]["description"]).lower()
    place = data["name"]
    statement = "Dude, it's {0} in {1} right now and the conditions are {2}. {3}".format(
        current_temp, place, condition, random.choice(remarks))
    return statement
