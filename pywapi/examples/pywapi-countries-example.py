#!/usr/bin/env python

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

countries = pywapi.get_countries_from_google('en')

pp.pprint(countries)
