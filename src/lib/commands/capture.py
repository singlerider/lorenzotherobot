import src.lib.commands.llama as llama_import
import src.lib.commands.pokemon as pokemon_import
import globals

def capture():
    usage = "!capture"
    
    poke_master = globals.CURRENT_USER
    
    pokemon = pokemon_import.master_pokemon[15][0]
    
    llama_import.UserData.add_pokemon(poke_master, pokemon)