'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import src.lib.commands.poll as options

def vote(args):
    
    usage = "!vote <option>"
    
    vote_choice = args[0]
    
    def return_vote():
        
        options.results.append(vote_choice)
        return "Vote counted: " + vote_choice + "!"
    
    return return_vote()