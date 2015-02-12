from oauth2client import gce
import httplib2
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser, run_flow
import globals
import os
import sys
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = globals.YOUTUBE_DEVELOPER_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

videos = []
channels = []
playlists = []
video_id = []
complete_url = []

def request(args):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY)
    
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
      q=args[0].replace("_", " "),
      part="id,snippet",
      #Returning only one result, as only the top result will be used
      maxResults = "1"
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
            video_id.append("(%s)" % (search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

    #print "Videos:\n", "\n".join(videos), "\n"
    #print "Channels:\n", "\n".join(channels), "\n"
    #print "Playlists:\n", "\n".join(playlists), "\n"
    try:
        # Only return a result if it's valid - if no result, return exception message
        complete_url.append("https://www.youtube.com/watch?v=" + str(video_id[0]).strip('()'))
        return str(videos[0]) + " | " + str(complete_url[0])
    except:
        return "Something happened. You probably spelled it wrong. Kappa"

if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="metal gear solid 3 longplay")
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()
    
    try:
        request(args)
        print complete_url[0]
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)



