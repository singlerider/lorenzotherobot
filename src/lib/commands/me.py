import src.lib.commands.llama as llama_import

def me():
    usage = "!me"
    
    args = llama_import.user_data_name
    
    #if llama_import.llama.grab_user in llama_import.llama.user_commands_import.user_command_dict:
    #    return llama_import.user_commands_import.user_command_dict[llama_import.llama.grab_user]["return"] + " | " + llama_import.llama.user_return
    #else:
    #    return llama_import.llama.user_return
    return llama_import.get_user_command()
