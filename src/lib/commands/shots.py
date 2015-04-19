"""
Developed Shane Engelman <me@5h4n3.com>
"""
# IN ORDER FOR THIS TO RUN CORRECTLY
# run '!shots init 0' the first time
import globals
import pickle

def writeShots():
    pickle.dump(shot_count, open("shots.pkl", "wb"))
def readShots():
    try:
        return pickle.load(open("shots.pkl", "rb"))
    except:
        return 0

shot_count = readShots()
usage = "!shots (add/remove/set [amount])"
def shots(args):
    global shot_count

    action = args[0]

    try:
      delta = int(args[1])
    except:
      return "I need a number for the amount. idiot."

    if action == "add":
      shot_count += delta
    elif action == "remove":
      shot_count -= delta
    elif action == "set":
      shot_count = delta

    writeShots()

    return "Alright! Now there's {} left".format(shot_count)

