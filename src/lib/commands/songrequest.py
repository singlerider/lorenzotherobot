'''
Developed by Shane Engelman <me@5h4n3.com>
'''

####Use this to run the songrequest script
import subprocess
import src.config.config as config
import sys
import time
import pexpect



def songrequest(args):
    
    usage = '!songrequest <artist_name> - <song_title>'
    
    artist = args[0]
    dash = args[1]
    title = args[2]
    
    login= config.spotify_username
    password = config.spotify_password
    
    def song():
        if dash == '-':
            
            add_to_playlist = "add " + config.spotify_playlist + " 0 " + " ".join([artist, title]).replace('_'," ")
            
            # execute spshell:

            
            child = pexpect.spawn('/home/shane/builds/libspotify-12.1.51-Linux-x86_64-release/share/doc/libspotify/examples/spshell/spshell')
            child.logfile = sys.stdout
            child.expect('Username')
            child.sendline(login)
            child.expect('Password')
            child.sendline(password)
            child.expect('Logged in to Spotify as user')
            child.sendline("search " + add_to_playlist)


            #spotify:user:jamesypaulmichael:playlist:2HejukmtRzlcan06cXMkGG            
            #call(["echo", "Jamesypaulmichael"])
            #return "Sending request, " + " ".join([artist, title]).replace('_'," ") + " to Spotify! " + add_to_playlist 
            return 
        else:
            return "Usage: " + usage.replace('<','').replace('>','')


    return song()