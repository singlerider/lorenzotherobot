'''
Developed by Shane Engelman <me@5h4n3.com>
'''

import time

query = []

results = []

def poll(args):
        
        
        
        usage = "!poll <option1/option2/option3>"
        
        options = args[0]
    
        def create_poll():
            
            query.append(options)
            return query[0]
            
        print "before sleep"
        time.sleep(10)
        print "after sleep"
        if args[0] != "0":
            return create_poll() + "Results: " + str(results)
        else:
            return "Usage: " + usage.replace('<','').replace('>','')
    