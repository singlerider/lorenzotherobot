# from src.lib.queries.quotes_queries import *
# from src.lib.twitch import *
#
#
# def addquote(args, **kwargs):
#     q = Quotes()
#     user = kwargs.get("username", "testuser")
#     channel = kwargs.get("channel", "testchannel")
#     quote = unicode(args[0].strip().strip("\"").strip("\'"), 'utf-8')
#     if len(quote) > 200:
#         return "Let's keep it below 200 characters?"
#     game = get_stream_game(channel)
#     q.add_quote(channel, user, quote, game)
#     return "{0} added!".format(quote)
