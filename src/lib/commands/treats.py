import src.lib.commands.llama as llama_import

def treats(args):

    usage = "!treats (add/remove [username] [amount])"
    
    approved_list = ['curvyllama', 'peligrosocortez', 'singlerider']
    
    add_remove = args[0]
    user = args[1]
    delta = args[2]
    
    if mod_name in approved_list:
        llama_import.delta_treats(add_remove, user, delta)
    else:
        return "Only " + ", ".join(approved_list) + "are allowed to do that!"