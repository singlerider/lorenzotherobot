'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import src.lib.commands.poll as options
import globals

voter = globals.CURRENT_USER

usage = "!vote [option]"

def vote(args):

    

    vote_choice = args[0]

    def return_vote():

        if voter in options.voters:
            return "You can't vote twice!"
        else:
            if vote_choice in options.poll().create_poll().options_separated:
                options.voters.append(voter)
                options.results.append(vote_choice)
                return "Vote counted: " + vote_choice + "!"
            else:
                return "It doesn't look like your choice is valid. Try entering a number."

    return return_vote()
