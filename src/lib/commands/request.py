"""
Developed by Shane Engelman <me@5h4n3.com> using the YouTube API
"""

##################################################################################
#The first time the bot is run when the requests command is given                #
#You MUST run the bot in the following manner in order to be able to authenticate#
#./serve --noauth_local_webserver                                                #
#After that, do your one-time authentication as prompted                         #
##################################################################################

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

def request(args):

    videos = []
    channels = []
    playlists = []
    video_id = []
    complete_url = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY)
    
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
      q=args[0].replace("_", " "),
      type="video",
      part="id,snippet",
      #videoDuration="short",
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

    # Retrieves video duration for the purposes of limiting the maximum playtime of a requested song
    video_response = youtube.videos().list(
    id=str(video_id[0]).strip("()"),
    part='snippet, contentDetails'
  ).execute()
    
    video_duration = video_response["items"][0]["contentDetails"]["duration"].replace("PT","")
    
    #print "video_id: " + str(video_id[0]).strip("()")
    #print video_duration
    
    #Time is output as PT2M43S
    
    #print "Videos:\n", "\n".join(videos), "\n"
    #print "Channels:\n", "\n".join(channels), "\n"
    #print "Playlists:\n", "\n".join(playlists), "\n"
    
    # Only return a result if it's valid - if no result, return exception message
    try:
        complete_url.append("https://www.youtube.com/watch?v=" + str(video_id[0]).strip('()'))
        #add_song
    except:
        return "Something happened. 'Couldn't find that video, dude."
    
    def add_to_playlist():
        # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
        # the OAuth 2.0 information for this application, including its client_id and
        # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
        # the Google Developers Console at
        # https://console.developers.google.com/.
        # Please ensure that you have enabled the YouTube Data API for your project.
        # For more information about using OAuth2 to access the YouTube Data API, see:
        #   https://developers.google.com/youtube/v3/guides/authentication
        # For more information about the client_secrets.json file format, see:
        #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
        
        CLIENT_SECRETS_FILE = "client_secret_221588655181-j4rkfkis8h2df80kon2nq6rs2au3aa30.apps.googleusercontent.com.json"
        
        # This variable defines a message to display if the CLIENT_SECRETS_FILE is
        # missing.
        MISSING_CLIENT_SECRETS_MESSAGE = """
        WARNING: Please configure OAuth 2.0
        
        To make this sample run you will need to populate the client_secrets.json file
        found at:
        
           %s
        
        with information from the Developers Console
        https://console.developers.google.com/
        
        For more information about the client_secrets.json file format, please visit:
        https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
        """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           CLIENT_SECRETS_FILE))
        
        # This OAuth 2.0 access scope allows for full read/write access to the
        # authenticated user's account.
        YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
          message=MISSING_CLIENT_SECRETS_MESSAGE,
          scope=YOUTUBE_READ_WRITE_SCOPE)
        
        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()
        
        if credentials is None or credentials.invalid:
            flags = argparser.parse_args()
            credentials = run_flow(flow, storage, flags)
        
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
          http=credentials.authorize(httplib2.Http()))

        add_video_request=youtube.playlistItems().insert(
            part="snippet",
            body={
            'snippet': {
              'playlistId': globals.YOUTUBE_PLAYLIST, 
              'resourceId': {
                      'kind': 'youtube#video',
                  'videoId': video_id[0].strip("()")
                }
            #'position': 0
            }
    }
    ).execute()
    
        #print "Video added: %s" % add_video_request
    try:
        add_song = add_to_playlist()
        return str("Video added: "+ str(videos[0]) + " | " + str(complete_url[0])) + " | Duration: " + video_duration
    except:
        
        #print video_id[0].strip("()")
        return "Something happened. You probably spelled it wrong. Kappa"

if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="metal gear solid 3 longplay")
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()
    
    try:
        request(args)
        #print complete_url[0]
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
