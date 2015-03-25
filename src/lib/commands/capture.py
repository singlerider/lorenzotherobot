import src.lib.commands.llama as llama_import
import globals
import os
import sqlite3
from src.lib.commands.pokedex import pokedex

def capture():
    usage = "!capture"

    if globals.CAUGHT is False:
        globals.CAUGHT = True
        pokedex.setPokemon(globals.CURRENT_USER, globals.POKEMON)
        return globals.CURRENT_USER + " caught it!"
    else:
        return "Somebody else beat you to it!"
