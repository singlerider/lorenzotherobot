'''
Developed by Shane Engelman <me@5h4n3.com>
'''

def songrequest(args):
    
    usage = '!songrequest <artist_name> - <song_title>'
    
    artist = args[0]
    dash = args[1]
    title = args[2]
    
    def song():
        if args[1] == '-':
            return "Sending request, " + " ".join([artist, title]).replace('_'," ") + " to Spotify!"
        else:
            return "Usage: " + usage.replace('<','').replace('>','')
        
        
    return song()