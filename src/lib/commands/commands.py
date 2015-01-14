import src.lib.command_headers as headers

def commands():
    usage = '!commands'
    

    return ", ".join(sorted(headers.commands))
