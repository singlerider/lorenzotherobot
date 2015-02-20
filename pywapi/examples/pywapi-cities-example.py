#!/usr/bin/env python

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

cities = pywapi.get_cities_from_google('fr', 'de') # or (country = 'fr', hl = 'de')

pp.pprint(cities)
