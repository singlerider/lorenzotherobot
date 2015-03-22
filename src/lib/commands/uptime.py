import src.lib.commands.llama as llama_import


def uptime():
    usage = "!uptime"

    return llama_import.get_stream_uptime()
