def randomnumber():
    usage = '!randomnumber'
    # module = importlib.import_module('src.lib.commands.%s' % command)
    # carry out validation
    try:
        num = range(10, 50)
        return num[random.randint(0, len(num) - 1)]
    except ValueError:
        return '!randomnumber'
    except:
        return usage
