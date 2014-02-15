#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *

bot = Roboraj(config).run()
