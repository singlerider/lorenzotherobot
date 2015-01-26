'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import random
import time
import re

def streetfighter():
    
    usage = '!streetfighter'
    

    
    # Pokemon name,their type(s), and a grouping for their evolution order, in the form of a list
    street_fighters = [[ 
              'Akuma'],
            ['Ryu'], ['Chun-Li'], ['Ken'], ['M. Bison'], ['Oni'],
            ['Poison'], ['Evil Ryu'], ['Juri'], ['Cammy'], ['Gouken'],
            ['Sagat'], ['Sakura'], ['Guile'], ['Vega'], ['Dan'], ['Decapre'],
            ['Balrog'], ['Blanka'], ['Charlie'], ['Zangief'], ['Seth'], ['Ibuki'],
            ['Rose'], ['Abel'], ['Elena'], ['Dhalsim'], ['C. Viper'], ['Gen'],
            ['Gill'], ['Makoto'], ['Fei Long'], ['Hugo'], ['Guy'], ['Hakan'],
            ['Dudley'], ['Goutetsu'], ['Adon'], ['Oro'], ['Rolento'], ['Alex'],
            ['Dee Jay'], ['Yun'], ['E. Honda'], ['T. Hawk'], ['Karin'],
            ['Yang'], ['Skullomania'], ['Urien'], ['Rufus'], ['Sean'],
            ['Q'], ['El Fuerte'], ['Necro'], ['Twelve']
            ]

    # One-line for loop that runs through pokemon_list, searching only the first column    
    street_fighter = [x[0] for x in street_fighters]
    #One-line for loop that runs through pokemon_list, searching only the third column
    
    # Grabs multiplier of pokemon based on name[type]


    # Script that handles battle    
    def battle():
        # Establishes two randomly selected pokemon as independent variables

        fighter_1 = random.choice (street_fighter)
        fighter_2 = random.choice (street_fighter)
        
        # Establishes the two selected pokemon as a concatenation 
        versus = "It's " + fighter_1 + " versus " + fighter_2 + ", dude!"
        
        # Establishes the two selected pokemon to battle
        versus_list = [fighter_1, fighter_2]
        
        # Sets variable for winner between pokemon1 and pokemon2
        winner = random.choice(versus_list) + " Wins!"
        
        # Allows for random selection from each list
        random.shuffle(street_fighters)
        random.shuffle(versus_list)

        # Concatenates results of versus and winner, separated by a space
        return " ".join([versus, winner])

    #Return corresponding evolutionary set
   
    return battle()
