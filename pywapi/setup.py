#!/usr/bin/env python

#Copyright (c) 2009 Eugene Kaznacheev <qetzal@gmail.com>
#Copyright (c) 2013 Joshua Tasker <jtasker@gmail.com>

#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

from distutils.core import setup

__author__ = 'qetzal@gmail.com, jtasker@gmail.com'
from pywapi import __version__


setup(name='pywapi',
    version=__version__,
    description='Python wrapper around different weather APIs',
    author='Eugene Kaznacheev, Joshua Tasker',
    author_email='qetzal@gmail.com, jtasker@gmail.com',
    url='http://code.google.com/p/python-weather-api/',
    py_modules=['pywapi'],
    license='MIT',
    keywords = 'weather api yahoo noaa google',
    platforms = 'any',
    long_description = """
This module provides a Python wrapper around the Yahoo! Weather, Weather.com,
and National Oceanic and Atmospheric Administration (NOAA) APIs. Fetch
weather reports using zip code, location id, city name, state, country, etc.
    """
)
