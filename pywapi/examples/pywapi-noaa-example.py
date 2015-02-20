#!/usr/bin/env python

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.get_weather_from_noaa('KJFK')
pp.pprint(result)
