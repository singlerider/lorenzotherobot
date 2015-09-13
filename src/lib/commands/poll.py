'''
Developed by theepicsnail
'''

import socket
import re
import time
import sys
from src.lib.functions_general import *
import time
import thread
import src.lib.cron as cron
import globals
import src.lib.irc as irc


voteline = ""  # message to send periodically about the poll
voted = set()  # users who've voted
options = {}  # choiceid to option string
votes = {}  # choiceid to count
activePoll = False
instructions = " (Type '!vote' plus the number you would like to vote for) "


def computeWinner():
    global activePoll
    activePoll = False

    count = -1
    winners = []
    for k, v in votes.items():
        if v > count:
            winners = [options[k]]
            count = v
        elif v == count:
            winners.append(options[k])
    if len(winners) == 1:
        return "Winner! " + winners[0]
    return "Tie! " + " and " .join(winners)


def poll(args):
    if globals.global_channel == 'shedeviil_09':
        return None
    global voteline, voted, options, votes, activePoll
    arg = args[0]

    if arg == "end":
        if activePoll:
            return computeWinner()
        return "No poll active"

    if "/" not in arg:
        return "need multiple options separated by /'s"

    voted = set()
    options = {}
    votes = {}
    activePoll = True

    options_lines = arg.split("/")
    voteline = ""
    for idx, opt in enumerate(options_lines):
        idx = str(idx + 1)  # 1 index
        opt = opt.strip()
        voteline += " %s(%s)" % (idx, opt)
        options[idx] = opt
        votes[idx] = 0

    out = "A wild poll has emerged! " + instructions + voteline
    return out


def cron(a=None):
    if activePoll is True:
        return instructions + voteline


def onVote(arg):
    if activePoll is False:
        return "There's no active poll, ya dope."
    if globals.CURRENT_USER in voted:
        return "You've already voted!"
    if arg not in votes:
        return "That's not a valid option"

    voted.add(globals.CURRENT_USER)
    votes[arg] += 1
    # return "Vote counted"
