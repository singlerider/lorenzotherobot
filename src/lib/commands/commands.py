import src.lib.command_headers as headers
import urllib2
import ast

def commands():
    usage = '!commands'
    
    response = urllib2.urlopen('https://tmi.twitch.tv/group/user/curvyllama/chatters') #change username to your channel
    user_dict = ast.literal_eval(response.read())
    
    key_list = []
    
    if mod_name in user_dict["chatters"]["moderators"]:
        return str(", ".join(sorted(headers.commands))).replace("!","")
    else:
        for key, value in headers.commands.iteritems():
            for subkey in value.iteritems():
                if 'ul' and 'mod' not in subkey:
                    key_list.append(key)
        return str(sorted(set(key_list))).strip("[]").replace("!", "").replace("'", "")