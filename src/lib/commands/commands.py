import src.lib.command_headers as headers
import urllib2
import ast
import globals


def commands():
    usage = '!commands'

    # change username to your channel
    response = urllib2.urlopen(
        'https://tmi.twitch.tv/group/user/curvyllama/chatters')
    user_dict = ast.literal_eval(response.read())

    key_list = []

    mod_name = globals.CURRENT_USER

    if mod_name in user_dict["chatters"]["moderators"]:
        return str(", ".join(sorted(headers.commands))).replace("!", "")
    else:
        return "A full list of commands can be found at http://www.github.com/singlerider/lorenzotherobot"
        # Returns non-mod commands
        # for key, value in headers.commands.iteritems():
        #    for subkey in value.iteritems():
        #        if 'ul' and 'mod' not in subkey:
        #            key_list.append(key)
        # return str(sorted(set(key_list))).strip("[]").replace("!",
        # "").replace("'", "")
