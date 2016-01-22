'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import random


def streetfighter():
    street_fighters = [
        'Akuma', 'Ryu', 'Chun-Li', 'Ken', 'M. Bison', 'Oni',
        'Poison', 'Evil Ryu', 'Juri', 'Cammy', 'Gouken',
        'Sagat', 'Sakura', 'Guile', 'Vega', 'Dan', 'Decapre',
        'Balrog', 'Blanka', 'Charlie', 'Zangief', 'Seth', 'Ibuki',
        'Rose', 'Abel', 'Elena', 'Dhalsim', 'C. Viper', 'Gen',
        'Gill', 'Makoto', 'Fei Long', 'Hugo', 'Guy', 'Hakan',
        'Dudley', 'Goutetsu', 'Adon', 'Oro', 'Rolento', 'Alex',
        'Dee Jay', 'Yun', 'E. Honda', 'T. Hawk', 'Karin',
        'Yang', 'Skullomania', 'Urien', 'Rufus', 'Sean',
        'Q', 'El Fuerte', 'Necro', 'Twelve'
    ]

    def battle():
        fighter_1 = random.choice(street_fighters)
        fighter_2 = random.choice(street_fighters)
        versus = "It's " + fighter_1 + " versus " + fighter_2 + ", dude!"
        versus_list = [fighter_1, fighter_2]
        winner = random.choice(versus_list) + " Wins!"
        random.shuffle(street_fighters)
        random.shuffle(versus_list)
        return " ".join([versus, winner])
    return battle()
