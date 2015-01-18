import random
import time

def pokemon():
    
    usage = '!pokemon'
    
    pokemonlist = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', \
                   'Squirtle', 'Wortortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', \
                   'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', \
                   'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', \
                   'Sandslash', 'Nidoran Male', 'Nidorina', 'Nidoqueen', 'Nidoran Female', 'Nidorino', 'Nidoking', \
                   'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', \
                   'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', \
                   'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', \
                   'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', \
                   'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebell', \
                   'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', \
                   'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', \
                   'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', \
                   'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', \
                   'Exeggcute', 'Exeggcutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', \
                   'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskan', 'Horsea', \
                   'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', \
                   'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyrados', 'Lapras', 'Ditto', \
                   'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Polygon', 'Omanyte', 'Lord Helix (Omastar)', \
                   'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', \
                   'Dragonair', 'Dragonite', 'Mewtwo', 'Mew', 'Missingno'          
                   ]
    
    def battle():
        pokemon1 = random.choice(pokemonlist)
        pokemon2 = random.choice(pokemonlist)
        
        versus = "It's: " + pokemon1 + " versus " + pokemon2 + ", dude! "
        
        versuslist = [pokemon1, pokemon2]
        
        winner = random.choice(versuslist) + " Wins!"
        
        random.shuffle(pokemonlist)
        random.shuffle(versuslist)
        
        #time.sleep( 5 )
        #return ",".join(versus, winner)
        return " ".join([versus, winner])
        #return battle(versus, winner)
        
    return battle()
        