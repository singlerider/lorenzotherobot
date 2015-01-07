import random
import time

random.seed(time.time())

def randomnumber():
    usage = '!randomnumber'
      # carry out validation
    try:
        num = range(1,101)
        return num[random.randint(0,len(num) - 1)]
    except ValueError:
        return '!randomnumber'
    except:
        return usage