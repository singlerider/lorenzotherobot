#!/usr/bin/env python2.7

from sys import argv
from src.bot import *
from src.config.config import *
import datetime

#Logger is run. Roboraj is contained within
bot = Logger(config, "log/" + str(datetime.date.today()) + "-lorenzo.html").run()
