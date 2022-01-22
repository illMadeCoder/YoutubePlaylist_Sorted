from googleapiclient.discovery import build
import sys

DEVELOPER_KEY = "AIzaSyD5PSElg_tlHee9WlQMTxFcYx3GJZdxQ8c"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, 
                YOUTUBE_API_VERSION, 
                developerKey=DEVELOPER_KEY)

nextPageToken = None                
results = None
videos = []
videoNames_views = []
while True:
    results = youtube.playlistItems().list(part='contentDetails', 
                                            playlistId=sys.argv[1],
                                            maxResults=50,
                                            pageToken=nextPageToken).execute()   
# get video ids
    video_ids = list(map(lambda x : x['contentDetails']['videoId'], 
                                    results['items']))    
    
    videos = youtube.videos().list(part='statistics,snippet', 
                                    id=','.join(video_ids)).execute()

    videoNames_views = videoNames_views + list(map(lambda x: (x['snippet']['title'], x['statistics']['viewCount']), videos['items']))

    nextPageToken = results.get('nextPageToken')                                                                                                                          
    if not nextPageToken:
        break                                            

           
videoNames_views.sort(key=lambda x : int(x[1]), reverse=True)
print(videoNames_views[:15])