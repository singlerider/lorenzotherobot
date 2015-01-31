'''
Developed by Shane Engelman <me@5h4n3.com>
'''

####Use this to run the songrequest script
import subprocess
import src.config.config as config
import src
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
            p = subprocess.Popen(["/home/shane/builds/libspotify-12.1.51-Linux-x86_64-release/share/doc/libspotify/examples/spshell/spshell"], stdin=subprocess.PIPE,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.STDOUT)
            #Using libspotify 12.1.51.g86c92b43 Release Linux-x86_64 
            print p.stdout.readline()
            print p.stdout.read(len("Username (just press enter to login with stored credentials): "))
            print "sending login info:", login
            p.stdin.write(login+"\n")
            # Read the newline after the login
            print p.stdout.readline()
            print p.stdout.read(len("Password: "))            
            p.stdin.write(password+"\n")
            # Read the newline after the login
            print p.stdout.readline()
            
            # Read the logged in message which is two lines
            for i in range(2):
                print p.stdout.readline()
            
            p.stdin.write("search " + add_to_playlist + "\n")
            p.stdin.close()
            print p.stdout.read()
            
            
            child = pexpect.spawn('/home/shane/builds/libspotify-12.1.51-Linux-x86_64-release/share/doc/libspotify/examples/spshell/spshell')
            child.logfile = sys.stdout
            child.expect('Username (just press enter to login with stored credentials): ')
            child.sendline(login)
            child.expect('Password: ')
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