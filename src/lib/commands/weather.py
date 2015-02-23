#!/usr/bin/env python

"""
Developed by Shane Engelman <me@5h4n3.com> using the weather API found at
https://code.google.com/p/python-weather-api/
"""

import pywapi

def weather(args):
    usage = "!weather [zipcode]"
    
    try:
        result = pywapi.get_weather_from_yahoo(str(args[0]).replace("_", " "), "imperial")
        current_conditions = result["condition"]["title"] + ": "  + result["condition"]["text"] + ", " + result["condition"]["temp"]
        five_day_forecast = result["forecasts"]
        forecast_1 = str(five_day_forecast[0]["day"]) + ": " + str(five_day_forecast[0]["text"]) + ", " + str(five_day_forecast[0]["high"]) + ", " + str(five_day_forecast[0]["low"]) + " | "
        forecast_2 = str(five_day_forecast[1]["day"]) + ": " + str(five_day_forecast[1]["text"]) + ", " + str(five_day_forecast[1]["high"]) + ", " + str(five_day_forecast[1]["low"]) + " | "
        forecast_3 = str(five_day_forecast[2]["day"]) + ": " + str(five_day_forecast[2]["text"]) + ", " + str(five_day_forecast[2]["high"]) + ", " + str(five_day_forecast[2]["low"]) + " | "
        forecast_4 = str(five_day_forecast[3]["day"]) + ": " + str(five_day_forecast[3]["text"]) + ", " + str(five_day_forecast[3]["high"]) + ", " + str(five_day_forecast[3]["low"]) + " | "
        forecast_5 = str(five_day_forecast[4]["day"]) + ": " + str(five_day_forecast[4]["text"]) + ", " + str(five_day_forecast[4]["high"]) + ", " + str(five_day_forecast[4]["low"])
        forecasts = forecast_1 + forecast_2 + forecast_3 + forecast_4 + forecast_5
        
        return current_conditions + " | Forecasts: " + forecasts
    except:
        return "Zip codes only, at the moment, plz."
