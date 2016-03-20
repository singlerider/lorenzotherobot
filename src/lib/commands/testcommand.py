def testcommand(**kwargs):
    username = kwargs["username"]
    channel = kwargs["channel"]
    return channel + ", " + username
