#!/usr/bin/env python3

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

kalamata = pywapi.get_weather_from_weather_com('GRXX0036')

pp.pprint(kalamata)
