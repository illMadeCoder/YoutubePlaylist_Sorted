from googleapiclient.discovery import build
import config

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, 
                YOUTUBE_API_VERSION, 
                developerKey=config.DEVELOPER_KEY)  

def playlistIDToPlaylist(playlistID):
    print(playlistID)
    result = youtube.playlists().list(
        part='snippet', 
        id=playlistID,
        maxResults=50).execute()
    return result["items"][0]["snippet"]


def playlistIDToVideos(playlistID):
    playlistVideos = []
    nextPageToken = None
    while True:
        # query youtube for a list of videos for the given playlistID
        playlistItemsRequestResult = youtube.playlistItems().list(
            part='contentDetails', 
            playlistId=playlistID,
            maxResults=50,
            pageToken=nextPageToken).execute()

        # retrieve the list of videos in a simple form from the ds
        playlistItemVideos = playlistItemsRequestResult['items']

        # retrieve the playlist video ids
        playlistVideoIDs = list(map(lambda x : x['contentDetails']['videoId'], 
                                        playlistItemVideos))    
        # query youtube for the list of video statistic details 
        videosRequestResult = youtube.videos().list(
            part='statistics,snippet,status', 
            id=','.join(playlistVideoIDs)).execute()

        # append to the growing list of videos for this playlist only the videos that are available
        playlistVideos = playlistVideos + videosRequestResult["items"]
        
        # prepare for the next playlistItems batch
        nextPageToken = playlistItemsRequestResult.get('nextPageToken', None) 
        # if there is no more nextPageTokens returned by the results we have finished processing the playlist                                                                                                                         
        if not nextPageToken:            
            return playlistVideos         