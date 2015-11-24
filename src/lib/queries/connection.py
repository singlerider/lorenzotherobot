import MySQLdb as mdb
import sys
import globals
from src.lib.twitch import *


def get_connection():
    login = globals.mysql_credentials
    con = mdb.connect(login[0], login[1], login[2], login[3])
    return con
