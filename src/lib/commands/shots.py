"""
Developed Shane Engelman <me@5h4n3.com>
"""


def readShots():
    try:
        with open("shots.txt", "r+") as f:  # read changes.json
            try:
                count = int(f.read())
            except Exception as error:
                print error
                count = 0
            return count
    except Exception as error:
        print error
        with open("shots.txt", "w") as f:
            f.write(str(0))
            return 0


def writeShots(count):
    previous_count = readShots()
    with open("shots.txt", "w") as f:  # save words json file
        f.write(count)


def shots(args, **kwargs):
    action = args[0]
    shots_count = readShots()
    try:
        delta = int(args[1])
    except:
        return "I need a number for the amount. idiot."

    if action == "add":
        writeShots(str(shots_count + delta))
    elif action == "remove":
        writeShots(str(shots_count - delta))
    elif action == "set":
        writeShots(str(delta))

    return "Alright! Now there's {} left".format(readShots())
