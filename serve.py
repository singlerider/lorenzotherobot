#!/usr/bin/env python2.7

from sys import argv
from src.bot import *
from src.config.config import *
import datetime

bot = Roboraj(config).run()
