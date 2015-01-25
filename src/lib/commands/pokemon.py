'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import random
import time

def pokemon(args):
    
    usage = '!pokemon <action (battle/print/evolution)> <name>'
    
    action = args[0]
    #name = args[1]
    
    print_dict = {}
    
    evolution_index = []
    type_index = []
    
    pokemon_1_cat = []
    pokemon_2_cat = []
    
    multipliers = {'Normal': {
                           'Fighting': 2.0,
                           'Ghost': 0.0,
                           },
                   'Fighting': {
                            'Flying': 2.0,
                            'Rock': 0.5,
                            'Bug': 0.5,
                            'Psychic': 2.0,
                            'Dark': 0.5,
                            'Fairy': 2.0
                            },
                   'Flying': {
                            'Fighting': 0.5,
                            'Ground': 0.0,
                            'Rock': 2.0,
                            'Bug': 0.5,
                            'Grass': 0.5,
                            'Electric': 2.0,
                            'Ice': 2.0 
                            },
                   'Poison': {
                            'Fighting': 0.5,
                            'Poison': 0.5,
                            'Ground': 2.0,
                            'Bug': 0.5,
                            'Grass': 0.5,
                            'Psychic': 2.0,
                            'Fairy': 0.5
                            },
                   'Ground': {
                            'Poison': 0.5,
                            'Rock': 0.5,
                            'Water': 2.0,
                            'Grass': 2.0,
                            'Electric': 0.0,
                            'Ice': 2.0  
                            },
                   'Rock': {
                            'Normal': 0.5,
                            'Fighting': 2.0,
                            'Flying': 0.5,
                            'Poison': 0.5,
                            'Ground': 2.0,
                            'Steel': 2.0,
                            'Fire': 0.5,
                            'Water': 2.0,
                            'Grass': 2.0
                            },
                   'Bug': {
                           'Fighting': 0.5,
                           'Flying': 2.0,
                           'Ground': 0.5,
                           'Rock': 2.0,
                           'Fire': 2.0,
                           'Grass': 2.0
                           },
                   'Ghost': {
                             'Normal': 0.0,
                             'Fighting': 0.0,
                             'Poison': 0.5,
                             'Bug': 0.5,
                             'Ghost': 2.0,
                             'Dark': 2.0
                             },
                   'Steel': {
                             'Normal': 0.5,
                             'Fighting': 2.0,
                             'Flying': 0.5,
                             'Poison': 0.0,
                             'Ground': 2.0,
                             'Rock': 0.5,
                             'Bug': 0.5,
                             'Steel': 0.5,
                             'Fire': 2.0,
                             'Grass': 0.5,
                             'Psychic': 0.5,
                             'Ice': 0.5,
                             'Dragon': 0.5,
                             'Fairy': 0.5
                             },
                   'Fire': {
                            'Ground': 2.0,
                            'Rock': 2.0,
                            'Bug': 0.5,
                            'Steel': 0.5,
                            'Fire': 0.5,
                            'Water': 2.0,
                            'Grass': 0.5,
                            'Ice': 0.5,
                            'Fairy': 0.5
                            },
                   'Water': {
                             'Steel': 0.5,
                             'Fire': 0.5,
                             'Water': 0.5,
                             'Grass': 2.0,
                             'Electric': 2.0,
                             'Ice': 0.5
                             },
                   'Grass': {
                             'Flying': 2.0,
                             'Poison': 2.0,
                             'Ground': 0.5,
                             'Bug': 2.0,
                             'Fire': 2.0,
                             'Water': 0.5,
                             'Grass': 0.5,
                             'Electric': 0.5,
                             'Ice': 2.0
                             },
                   'Electric': {
                                'Flying': 0.5,
                                'Ground': 2.0,
                                'Steel': 0.5,
                                'Electric': 0.5
                                },
                   'Psychic': {
                               'Fighting': 0.5,
                               'Bug': 2.0,
                               'Ghost': 2.0,
                               'Psychic': 0.5,
                               'Dark': 2.0
                               },
                   'Ice': {
                           'Fighting': 2.0,
                           'Rock': 2.0,
                           'Steel': 2.0,
                           'Fire': 2.0,
                           'Ice': 0.5
                           },
                   'Dragon': {
                              'Fire': 0.5,
                              'Water': 0.5,
                              'Grass': 0.5,
                              'Electric': 0.5,
                              'Ice': 2.0,
                              'Dragon': 2.0,
                              'Fairy': 2.0
                              },
                   'Dark': {
                            'Fighting': 2.0,
                            'Bug': 2.0,
                            'Ghost': 0.5,
                            'Psychic': 0.0,
                            'Dark': 0.5,
                            'Fairy': 2.0
                            },
                   'Fairy': {
                             'Fighting': 0.5,
                             'Poison': 2.0,
                             'Bug': 0.5,
                             'Steel': 2.0,
                             'Dragon': 0.0,
                             'Dark': 0.5
                             }   
                    }

    # Pokemon name,their type(s), and a grouping for their evolution order, in the form of a list
    pokemon_list = [[ 
			  'Bulbasaur', ('Grass' , 'Poison') , '0' ],
            [ 'Ivysaur', ('Grass' , 'Poison') , '0' ],
            [ 'Venusaur', ('Grass' , 'Poison') , '0' ],
            [ 'Charmander', ('Fire',) , '1' ],
            [ 'Charmeleon', ('Fire',) , '1' ],
            [ 'Charizard', ('Fire' , 'Flying') , '1' ],
            [ 'Squirtle', ('Water',) , '2' ],
            [ 'Wartortle', ('Water',) , '2' ],
            [ 'Blastoise', ('Water',) , '2' ],
            [ 'Caterpie', ('Bug',) , '3' ],
            [ 'Metapod', ('Bug',) , '3' ],
            [ 'Butterfree', ('Bug' , 'Flying') , '3' ],
            [ 'Weedle', ('Bug' , 'Poison') , '4' ],
            [ 'Kakuna', ('Bug' , 'Poison') , '4' ],
            [ 'Beedrill', ('Bug' , 'Poison') , '4' ],
            [ 'Pidgey', ('Normal' , 'Flying') , '5' ],
            [ 'Pidgeotto', ('Normal' , 'Flying') , '5' ],
            [ 'Pidgeot', ('Normal' , 'Flying') , '5' ],
            [ 'Rattata', ('Normal',) , '6' ],
            [ 'Raticate', ('Normal',) , '6' ],
            [ 'Spearow', ('Normal' , 'Flying') , '7' ],
            [ 'Fearow', ('Normal' , 'Flying') , '7' ],
            [ 'Ekans', ('Poison',) , '8' ],
            [ 'Arbok', ('Poison',) , '8' ],
            [ 'Pikachu', ('Electric',) , '9' ],
            [ 'Raichu', ('Electric',) , '9' ],
            [ 'Sandshrew', ('Ground',) , '10' ],
            [ 'Sandslash', ('Ground',) , '10' ],
            [ 'Nidoran Female', ('Poison',) , '11' ],
            [ 'Nidorina', ('Poison',) , '11' ],
            [ 'Nidoqueen', ('Poison' , 'Ground') , '11' ],
            [ 'Nidoran Male', ('Poison',) , '12' ],
            [ 'Nidorino', ('Poison',) , '12' ],
            [ 'Nidoking', ('Poison' , 'Ground') , '12' ],
            [ 'Clefairy', ('Fairy',) , '13' ],
            [ 'Clefable', ('Fairy',) , '13' ],
            [ 'Vulpix', ('Fire',) , '14' ],
            [ 'Ninetales', ('Fire',) , '14' ],
            [ 'Jigglypuff', ('Normal' , 'Fairy') , '15' ],
            [ 'Wigglytuff', ('Normal' , 'Fairy') , '15' ],
            [ 'Zubat', ('Poison' , 'Flying') , '16' ],
            [ 'Golbat', ('Poison' , 'Flying') , '16' ],
            [ 'Oddish', ('Grass' , 'Poison') , '17' ],
            [ 'Gloom', ('Grass' , 'Poison') , '17' ],
            [ 'Vileplume', ('Grass' , 'Poison') , '17' ],
            [ 'Paras', ('Bug' , 'Grass') , '18' ],
            [ 'Parasect', ('Bug' , 'Grass') , '18' ],
            [ 'Venonat', ('Bug' , 'Poison') , '19' ],
            [ 'Venomoth', ('Bug' , 'Poison') , '19' ],
            [ 'Diglett', ('Ground',) , '20' ],
            [ 'Dugtrio', ('Ground',) , '20' ],
            [ 'Meowth', ('Normal',) , '21' ],
            [ 'Persian', ('Normal',) , '21' ],
            [ 'Psyduck', ('Water',) , '22' ],
            [ 'Golduck', ('Water',) , '22' ],
            [ 'Mankey', ('Fighting',) , '23' ],
            [ 'Primeape', ('Fighting',) , '23' ],
            [ 'Growlithe', ('Fire',) , '24' ],
            [ 'Arcanine', ('Fire',) , '24' ],
            [ 'Poliwag', ('Water',) , '25' ],
            [ 'Poliwhirl', ('Water',) , '25' ],
            [ 'Poliwrath', ('Water' , 'Fighting') , '25' ],
            [ 'Abra', ('Psychic',) , '26' ],
            [ 'Kadabra', ('Psychic',) , '26' ],
            [ 'Alakazam', ('Psychic',) , '26' ],
            [ 'Machop', ('Fighting',) , '27' ],
            [ 'Machoke', ('Fighting',) , '27' ],
            [ 'Machamp', ('Fighting',) , '27' ],
            [ 'Bellsprout', ('Grass' , 'Poison') , '28' ],
            [ 'Weepinbell', ('Grass' , 'Poison') , '28' ],
            [ 'Victreebel', ('Grass' , 'Poison') , '28' ],
            [ 'Tentacool', ('Water' , 'Poison') , '29' ],
            [ 'Tentacruel', ('Water' , 'Poison') , '29' ],
            [ 'Geodude', ('Rock' , 'Ground') , '30' ],
            [ 'Graveler', ('Rock' , 'Ground') , '30' ],
            [ 'Golem', ('Rock' , 'Ground') , '30' ],
            [ 'Ponyta', ('Fire',) , '31' ],
            [ 'Rapidash', ('Fire',) , '31' ],
            [ 'Slowpoke', ('Water' , 'Psychic') , '32' ],
            [ 'Slowbro', ('Water' , 'Psychic') , '32' ],
            [ 'Magnemite', ('Electric' , 'Steel') , '33' ],
            [ 'Magneton', ('Electric' , 'Steel') , '33' ],
            [ "Farfetch'd ", ('Normal' , 'Flying') , '34' ],
            [ 'Doduo', ('Normal' , 'Flying') , '35' ],
            [ 'Dodrio', ('Normal' , 'Flying') , '35' ],
            [ 'Seel', ('Water',) , '36' ],
            [ 'Dewgong', ('Water' , 'Ice') , '36' ],
            [ 'Grimer', ('Poison',) , '37' ],
            [ 'Muk', ('Poison',) , '37' ],
            [ 'Shellder', ('Water',) , '38' ],
            [ 'Cloyster', ('Water' , 'Ice') , '38' ],
            [ 'Gastly', ('Ghost' , 'Poison') , '39' ],
            [ 'Haunter', ('Ghost' , 'Poison') , '39' ],
            [ 'Gengar', ('Ghost' , 'Poison') , '39' ],
            [ 'Onix', ('Rock' , 'Ground') , '40' ],
            [ 'Drowzee', ('Psychic',) , '41' ],
            [ 'Hypno', ('Psychic',) , '41' ],
            [ 'Krabby', ('Water',) , '42' ],
            [ 'Kingler', ('Water',) , '42' ],
            [ 'Voltorb', ('Electric',) , '43' ],
            [ 'Electrode', ('Electric',) , '43' ],
            [ 'Exeggcute', ('Grass' , 'Psychic') , '44' ],
            [ 'Exeggutor', ('Grass' , 'Psychic') , '44' ],
            [ 'Cubone', ('Ground',) , '45' ],
            [ 'Marowak', ('Ground',) , '45' ],
            [ 'Hitmonlee', ('Fighting',) , '46' ],
            [ 'Hitmonchan', ('Fighting',) , '47' ],
            [ 'Lickitung', ('Normal',) , '48' ],
            [ 'Koffing', ('Poison',) , '49' ],
            [ 'Weezing', ('Poison',) , '50' ],
            [ 'Rhyhorn', ('Ground' , 'Rock') , '51' ],
            [ 'Rhydon', ('Ground' , 'Rock') , '51' ],
            [ 'Chansey', ('Normal',) , '52' ],
            [ 'Tangela', ('Grass',) , '53' ],
            [ 'Kangaskhan', ('Normal',) , '54' ],
            [ 'Horsea', ('Water',) , '55' ],
            [ 'Seadra', ('Water',) , '55' ],
            [ 'Goldeen', ('Water',) , '56' ],
            [ 'Seaking', ('Water',) , '56' ],
            [ 'Staryu', ('Water',) , '57' ],
            [ 'Starmie', ('Water' , 'Psychic') , '57' ],
            [ 'Mime', ('Mr.' , 'Mime') , '58' ],
            [ 'Scyther', ('Bug' , 'Flying') , '59' ],
            [ 'Jynx', ('Ice' , 'Psychic') , '60' ],
            [ 'Electabuzz', ('Electric',) , '61' ],
            [ 'Magmar', ('Fire',) , '62' ],
            [ 'Pinsir', ('Bug',) , '63' ],
            [ 'Tauros', ('Normal',) , '64' ],
            [ 'Magikarp', ('Water',) , '65' ],
            [ 'Gyarados', ('Water' , 'Flying') , '65' ],
            [ 'Lapras', ('Water' , 'Ice') , '66' ],
            [ 'Ditto', ('Normal',) , '67' ],
            [ 'Eevee', ('Normal',) , ('68',) ],
            [ 'Vaporeon', ('Water',) , ('68','0') ],
            [ 'Jolteon', ('Electric',) , ('68','1') ],
            [ 'Flareon', ('Fire',) , ('68','2') ],
            [ 'Porygon', ('Normal',) , '69' ],
            [ 'Omanyte', ('Rock' , 'Water') , '70' ],
            [ 'Omastar', ('Rock' , 'Water') , '70' ],
            [ 'Kabuto', ('Rock' , 'Water') , '71' ],
            [ 'Kabutops', ('Rock' , 'Water') , '71' ],
            [ 'Aerodactyl', ('Rock' , 'Flying') , '72' ],
            [ 'Snorlax', ('Normal',) , '73' ],
            [ 'Articuno', ('Ice' , 'Flying') , '74' ],
            [ 'Zapdos', ('Electric' , 'Flying') , '75' ],
            [ 'Moltres', ('Fire' , 'Flying') , '76' ],
            [ 'Dratini', ('Dragon',) , '77' ],
            [ 'Dragonair', ('Dragon',) , '77' ],
            [ 'Dragonite', ('Dragon' , 'Flying') , '77' ],
            [ 'Mewtwo', ('Psychic',) , '78' ],
            [ 'Mew', ('Psychic',) , '79' ],
            [ 'Missingno', ('Normal', 'Flying') , '80' ]
            ]

    # One-line for loop that runs through pokemon_list, searching only the first column    
    pocket_monster = [x[0] for x in pokemon_list]
    #One-line for loop that runs through pokemon_list, searching only the third column
    #evolution_set = [k[2] for k in pokemon_list]
    
    # Grabs multiplier of pokemon based on name[type]
    '''
    def get_multiplier(pokemon_1_type, pokemon_2_type):
        default = 1.0
        for i in multiplier:
            for j in multiplier:
                try:
                    print "dict['Name']: ", multipliers[0];
                    print "dict['Age']: ", multipliers[1];
                except:
                    print "Whoops"            
    '''
     
    # Script that handles battle    
    def battle():
        # Establishes two randomly selected pokemon as independent variables
        
        
            

        
        pokemon_1 = random.choice (pocket_monster)
        pokemon_2 = random.choice (pocket_monster)
        
        # Establishes the two selected pokemon as a concatenation 
        versus = "It's " + pokemon_1 + " versus " + pokemon_2 + ", dude!"
        
        # Establishes the two selected pokemon to battle
        versus_list = [pokemon_1, pokemon_2]
        
        # Sets variable for winner between pokemon1 and pokemon2
        winner = random.choice(versus_list) + " Wins!"
        
        # Allows for random selection from each list
        random.shuffle(pokemon_list)
        random.shuffle(versus_list)

        for name, type, group in pokemon_list:
            
            if pokemon_1.lower() in name.lower():
                
                type_index.append(type)
                for index in type_index:
                    pass
                    #print "Type for 1 " + str(index)
                
                    if type == index:
                        print name + " is Pokemon 1 " + "with type 1 " + str(type)
                        
        for name, type, group in pokemon_list:
            
            if pokemon_2.lower() in name.lower():
                
                type_index.append(type)
                for index in type_index:
                    pass
                    #print "Type for 2 " + str(index)
                
                    if type == index:
                        print " ".join([name, " is Pokemon 2 " , "with type(s)" , str(type)])                       
        
        
        # Concatenates results of versus and winner, separated by a space
        return " ".join([versus, winner])

    #Return corresponding evolutionary set
    def evolution():
        #Iterate through nested list, returning Pokemon name, type, and set
        #and adding it to empty evolution_set
        for name,__,set in pokemon_list:
            name_list.append(str(name) + " , " + str(set))
            print (name , set)
        print name_list
        #evolved_pokemon = random.choice (evolution_set)

        #random.shuffle(pokemon_list)
        return (args[1] + str(name_list))
    
    def print_pokemon():
        
        print_dict[0] = args[1]

        #for item in pokemon_list:
        #    pass
        
        for name, type, group in pokemon_list:
            
            if group == "3":
                print str(name)
            
            if args[1].lower() in name.lower():
                
                evolution_index.append(group)
                for index in evolution_index:
                    pass
                    print str(index)
                
                    if group == index:
                        print name + " HOLY CRAP"
                print "Match: " + str(name) + " is a " + str(type) + str(group)
                return " ".join([str(name) + " is type: ",str(type).replace("(", "").replace(")","").replace(",", " ")])

        

                
                
    #print ("Name List: " + str(name_list))
    #print ("Evolution Set: " + str(evolution_set))
    #print ("Pocket Monster " + str(pocket_monster))
        
    #return getmultiplier()
    if action == "battle":
        return battle()
    if action == "evolution":
        return evolution()
    if action == "print":
        return print_pokemon()
    else:
        return "Usage: " + usage.replace('<','').replace('>','')
    print "At least this works"
    #else:
        # return a thing