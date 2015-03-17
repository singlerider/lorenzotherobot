import src.lib.commands.llama as llama_import
import globals

def treats(args):

    usage = "!treats (add/remove [username] [amount])"
    
    approved_list = ['curvyllama', 'peligrosocortez', 'singlerider', 'newyork_triforce']
    
    add_remove = args[0]
    delta_user = args[1].lower()
    delta = args[2]
    
    mod_name = globals.CURRENT_USER
    
    if mod_name in approved_list:
        
        if add_remove == "add" and delta_user == "all":
            return llama_import.enter_into_database_all(delta)
        else:
            return llama_import.delta_treats(add_remove, delta_user, delta)
        
        
    else:
        return "Only " + ", ".join(approved_list) + " are allowed to do that!"