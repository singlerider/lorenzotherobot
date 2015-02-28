'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import socket, re, time, sys
from src.lib.functions_general import *
import time
import thread
import src.lib.cron as cron
import globals
import src.lib.irc as irc

query = []

results = []

voters = []

print "global"

def __init__(self, config):
    self.config = config
    print "init"
    
def poll(args):
    print "def poll"
    usage = "!poll <option1/option2/option3>"
    
    options_raw = args[0]
    query.append(options)

    def create_poll(self):
        print "create poll"
        thread.start_new_thread(cron.cron(self, globals.channel).run, (60))
        print "End Thread"
        
        poll_results = "Vote for option 1, 2, or 3 by typing '!vote [option_number (1/2/3)]'"
        
        options_separated = options_raw.split('/')
        
        irc.irc.send_message(self, globals.channel, poll_results)
        irc.irc.send_message(self, globals.channel, poll_results)
        irc.irc.send_message(self, globals.channel, poll_results)
    
        return query[0]
    
    return str(query) + "Results: " + str(results)
