import random
import time

def pokemon():
    
    usage = '!pokemon'

    types = [ 'Normal', 'Fire', 'Fighting', 'Water', 'Flying', 'Grass', 'Poison', 'Electric', 'Ground', \
             'Psychic', 'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']
    
    
    #Nested dictionary with different pokemon types with defensive damage modifiers (higher number means 'more vulnerable to')
    multipliers = { 'Normal': {
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
                             'Fightin': 0.0,
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
    
    
    #Pokemon and their type(s), in the form of a list
    pokemondetaillist = [[ 'Bulbasaur ', ('Grass' , 'Poison') , '' ],
            [ 'Ivysaur ', ('Grass' , 'Poison') , '' ],
            [ 'Venusaur ', ('Grass' , 'Poison') , '' ],
            [ 'Charmander ', ('Fire', ) , '' ],
            [ 'Charmeleon ', ('Fire', ) , '' ],
            [ 'Charizard ', ('Fire' , 'Flying') , '' ],
            [ 'Squirtle ', ('Water', ) , '' ],
            [ 'Wartortle ', ('Water', ) , '' ],
            [ 'Blastoise ', ('Water', ) , '' ],
            [ 'Caterpie ', ('Bug', ) , '' ],
            [ 'Metapod ', ('Bug', ) , '' ],
            [ 'Butterfree ', ('Bug' , 'Flying') , '' ],
            [ 'Weedle ', ('Bug' , 'Poison') , '' ],
            [ 'Kakuna ', ('Bug' , 'Poison') , '' ],
            [ 'Beedrill ', ('Bug' , 'Poison') , '' ],
            [ 'Pidgey ', ('Normal' , 'Flying') , '' ],
            [ 'Pidgeotto ', ('Normal' , 'Flying') , '' ],
            [ 'Pidgeot ', ('Normal' , 'Flying') , '' ],
            [ 'Rattata ', ('Normal', ) , '' ],
            [ 'Raticate ', ('Normal', ) , '' ],
            [ 'Spearow ', ('Normal' , 'Flying') , '' ],
            [ 'Fearow ', ('Normal' , 'Flying') , '' ],
            [ 'Ekans ', ('Poison', ) , '' ],
            [ 'Arbok ', ('Poison', ) , '' ],
            [ 'Pikachu ', ('Electric', ) , '' ],
            [ 'Raichu ', ('Electric', ) , '' ],
            [ 'Sandshrew ', ('Ground', ) , '' ],
            [ 'Sandslash ', ('Ground', ) , '' ],
            [ 'Nidoran Female ', ('Poison', ) , '' ],
            [ 'Nidorina ', ('Poison', ) , '' ],
            [ 'Nidoqueen ', ('Poison' , 'Ground') , '' ],
            [ 'Nidoran Male ', ('Poison', ) , '' ],
            [ 'Nidorino ', ('Poison', ) , '' ],
            [ 'Nidoking ', ('Poison' , 'Ground') , '' ],
            [ 'Clefairy ', ('Fairy', ) , '' ],
            [ 'Clefable ', ('Fairy', ) , '' ],
            [ 'Vulpix ', ('Fire', ) , '' ],
            [ 'Ninetales ', ('Fire', ) , '' ],
            [ 'Jigglypuff ', ('Normal' , 'Fairy') , '' ],
            [ 'Wigglytuff ', ('Normal' , 'Fairy') , '' ],
            [ 'Zubat ', ('Poison' , 'Flying') , '' ],
            [ 'Golbat ', ('Poison' , 'Flying') , '' ],
            [ 'Oddish ', ('Grass' , 'Poison') , '' ],
            [ 'Gloom ', ('Grass' , 'Poison') , '' ],
            [ 'Vileplume ', ('Grass' , 'Poison') , '' ],
            [ 'Paras ', ('Bug' , 'Grass') , '' ],
            [ 'Parasect ', ('Bug' , 'Grass') , '' ],
            [ 'Venonat ', ('Bug' , 'Poison') , '' ],
            [ 'Venomoth ', ('Bug' , 'Poison') , '' ],
            [ 'Diglett ', ('Ground', ) , '' ],
            [ 'Dugtrio ', ('Ground', ) , '' ],
            [ 'Meowth ', ('Normal', ) , '' ],
            [ 'Persian ', ('Normal', ) , '' ],
            [ 'Psyduck ', ('Water', ) , '' ],
            [ 'Golduck ', ('Water', ) , '' ],
            [ 'Mankey ', ('Fighting', ) , '' ],
            [ 'Primeape ', ('Fighting', ) , '' ],
            [ 'Growlithe ', ('Fire', ) , '' ],
            [ 'Arcanine ', ('Fire', ) , '' ],
            [ 'Poliwag ', ('Water', ) , '' ],
            [ 'Poliwhirl ', ('Water', ) , '' ],
            [ 'Poliwrath ', ('Water' , 'Fighting') , '' ],
            [ 'Abra ', ('Psychic', ) , '' ],
            [ 'Kadabra ', ('Psychic', ) , '' ],
            [ 'Alakazam ', ('Psychic', ) , '' ],
            [ 'Machop ', ('Fighting', ) , '' ],
            [ 'Machoke ', ('Fighting', ) , '' ],
            [ 'Machamp ', ('Fighting', ) , '' ],
            [ 'Bellsprout ', ('Grass' , 'Poison') , '' ],
            [ 'Weepinbell ', ('Grass' , 'Poison') , '' ],
            [ 'Victreebel ', ('Grass' , 'Poison') , '' ],
            [ 'Tentacool ', ('Water' , 'Poison') , '' ],
            [ 'Tentacruel ', ('Water' , 'Poison') , '' ],
            [ 'Geodude ', ('Rock' , 'Ground') , '' ],
            [ 'Graveler ', ('Rock' , 'Ground') , '' ],
            [ 'Golem ', ('Rock' , 'Ground') , '' ],
            [ 'Ponyta ', ('Fire', ) , '' ],
            [ 'Rapidash ', ('Fire', ) , '' ],
            [ 'Slowpoke ', ('Water' , 'Psychic') , '' ],
            [ 'Slowbro ', ('Water' , 'Psychic') , '' ],
            [ 'Magnemite ', ('Electric' , 'Steel') , '' ],
            [ 'Magneton ', ('Electric' , 'Steel') , '' ],
            [ "Farfetch'd ", ('Normal' , 'Flying') , '' ],
            [ 'Doduo ', ('Normal' , 'Flying') , '' ],
            [ 'Dodrio ', ('Normal' , 'Flying') , '' ],
            [ 'Seel ', ('Water', ) , '' ],
            [ 'Dewgong ', ('Water' , 'Ice') , '' ],
            [ 'Grimer ', ('Poison', ) , '' ],
            [ 'Muk ', ('Poison', ) , '' ],
            [ 'Shellder ', ('Water', ) , '' ],
            [ 'Cloyster ', ('Water' , 'Ice') , '' ],
            [ 'Gastly ', ('Ghost' , 'Poison') , '' ],
            [ 'Haunter ', ('Ghost' , 'Poison') , '' ],
            [ 'Gengar ', ('Ghost' , 'Poison') , '' ],
            [ 'Onix ', ('Rock' , 'Ground') , '' ],
            [ 'Drowzee ', ('Psychic', ) , '' ],
            [ 'Hypno ', ('Psychic', ) , '' ],
            [ 'Krabby ', ('Water', ) , '' ],
            [ 'Kingler ', ('Water', ) , '' ],
            [ 'Voltorb ', ('Electric', ) , '' ],
            [ 'Electrode ', ('Electric', ) , '' ],
            [ 'Exeggcute ', ('Grass' , 'Psychic') , '' ],
            [ 'Exeggutor ', ('Grass' , 'Psychic') , '' ],
            [ 'Cubone ', ('Ground', ) , '' ],
            [ 'Marowak ', ('Ground', ) , '' ],
            [ 'Hitmonlee ', ('Fighting', ) , '' ],
            [ 'Hitmonchan ', ('Fighting', ) , '' ],
            [ 'Lickitung ', ('Normal', ) , '' ],
            [ 'Koffing ', ('Poison', ) , '' ],
            [ 'Weezing ', ('Poison', ) , '' ],
            [ 'Rhyhorn ', ('Ground' , 'Rock') , '' ],
            [ 'Rhydon ', ('Ground' , 'Rock') , '' ],
            [ 'Chansey ', ('Normal', ) , '' ],
            [ 'Tangela ', ('Grass', ) , '' ],
            [ 'Kangaskhan ', ('Normal', ) , '' ],
            [ 'Horsea ', ('Water', ) , '' ],
            [ 'Seadra ', ('Water', ) , '' ],
            [ 'Goldeen ', ('Water', ) , '' ],
            [ 'Seaking ', ('Water', ) , '' ],
            [ 'Staryu ', ('Water', ) , '' ],
            [ 'Starmie ', ('Water' , 'Psychic') , '' ],
            [ 'Mime ', ('Mr.' , 'Mime') , '' ],
            [ 'Scyther ', ('Bug' , 'Flying') , '' ],
            [ 'Jynx ', ('Ice' , 'Psychic') , '' ],
            [ 'Electabuzz ', ('Electric', ) , '' ],
            [ 'Magmar ', ('Fire', ) , '' ],
            [ 'Pinsir ', ('Bug', ) , '' ],
            [ 'Tauros ', ('Normal', ) , '' ],
            [ 'Magikarp ', ('Water', ) , '' ],
            [ 'Gyarados ', ('Water' , 'Flying') , '' ],
            [ 'Lapras ', ('Water' , 'Ice') , '' ],
            [ 'Ditto ', ('Normal', ) , '' ],
            [ 'Eevee ', ('Normal', ) , '' ],
            [ 'Vaporeon ', ('Water', ) , '' ],
            [ 'Jolteon ', ('Electric', ) , '' ],
            [ 'Flareon ', ('Fire', ) , '' ],
            [ 'Porygon ', ('Normal', ) , '' ],
            [ 'Omanyte ', ('Rock' , 'Water') , '' ],
            [ 'Omastar ', ('Rock' , 'Water') , '' ],
            [ 'Kabuto ', ('Rock' , 'Water') , '' ],
            [ 'Kabutops ', ('Rock' , 'Water') , '' ],
            [ 'Aerodactyl ', ('Rock' , 'Flying') , '' ],
            [ 'Snorlax ', ('Normal', ) , '' ],
            [ 'Articuno ', ('Ice' , 'Flying') , '' ],
            [ 'Zapdos ', ('Electric' , 'Flying') , '' ],
            [ 'Moltres ', ('Fire' , 'Flying') , '' ],
            [ 'Dratini ', ('Dragon', ) , '' ],
            [ 'Dragonair ', ('Dragon', ) , '' ],
            [ 'Dragonite ', ('Dragon' , 'Flying') , '' ],
            [ 'Mewtwo ', ('Psychic', ) , '' ],
            [ 'Mew ', ('Psychic', ) , '' ],
            [ 'Missingno', ('Normal', 'Flying') , '' ]
            ]
    
    #One-line for loop that runs through pokemondetaillist, searching only the first column    
    pocketmonster = [x[0] for x in pokemondetaillist]
    
    #Grabs multiplier of pokemon based on name[type]
    def getmultiplier(pokemon1type, pokemon2type):
        p1 = 1.0
        try:
            print "dict['Name']: ", multipliers['Name'];
            print "dict['Age']: ", multipliers['Age'];
        except:
            print "Whoops"            
                        
        
    
    #Script that handles battle    
    def battle():
        #Establishes two randomly selected pokemon as independent variables
        pokemon1 = random.choice (pocketmonster)
        pokemon2 = random.choice (pocketmonster)
        
        #Establishes the two selected pokemon as a concatenation 
        versus = "It's: " + pokemon1 + " versus " + pokemon2 + ", dude!"
        
        #Establishes the two selected pokemon to battle
        versuslist = [pokemon1, pokemon2]
        
        #Sets variable for winner between pokemon1 and pokemon2
        winner = random.choice(versuslist) + " Wins!"
        
        #Allows for random selection from each list
        random.shuffle(pokemondetaillist)
        random.shuffle(versuslist)
        
        #Concatenates results of versus and winner, separated by a space
        return " ".join([versus, winner])

    
    #return getmultiplier()    
    return battle()
        