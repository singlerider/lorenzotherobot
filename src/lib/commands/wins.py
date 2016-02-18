"""
Developed Shane Engelman <me@5h4n3.com>
"""


def readWins():
    try:
        with open("wins.txt", "r+") as f:  # read changes.json
            try:
                count = int(f.read())
            except Exception as error:
                print error
                count = 0
            return count
    except Exception as error:
        print error
        with open("wins.txt", "w") as f:
            f.write(str(0))
            return 0


def writeWins(count):
    previous_count = readWins()
    with open("wins.txt", "w") as f:  # save words json file
        f.write(count)


def wins(args):
    action = args[0]
    wins_count = readWins()
    try:
        delta = int(args[1])
    except:
        return "I need a number for the amount. idiot."

    if action == "add":
        writeWins(str(wins_count + delta))
    elif action == "remove":
        writeWins(str(wins_count - delta))
    elif action == "set":
        writeWins(str(delta))

    return "{} total wins now!".format(readWins())
