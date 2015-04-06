import globals

import smtplib



def report(args):
    fromaddr = globals.email_credentials[1]
    toaddrs = globals.email_credentials[0]
    msg = globals.CURRENT_USER + " would like to report a bug: " + args[0]
    
    username = fromaddr
    password = globals.email_credentials[2]

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr , toaddrs, msg)
    server.quit()

    return msg + " sent to " + toaddrs