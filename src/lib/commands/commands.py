import src.lib.command_headers as headers

def commands():
    usage = '!commands'
    

    return str(", ".join(sorted(headers.commands))).replace("!","")