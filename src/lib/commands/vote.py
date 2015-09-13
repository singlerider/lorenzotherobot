'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import src.lib.commands.poll as poll


def vote(args):
    return poll.onVote(args[0])
