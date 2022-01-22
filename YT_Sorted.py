from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
import sys

# flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json",
#    scopes=['https://www.googleapis.com/auth/youtube'])

# flow.run_local_server(port=8080, prompt="consent")   

# credentials = flow.credentials

DEVELOPER_KEY = "AIzaSyD5PSElg_tlHee9WlQMTxFcYx3GJZdxQ8c"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, 
                YOUTUBE_API_VERSION, 
                developerKey=DEVELOPER_KEY)  

playlistIDs = sys.argv[1].split(',')
sortby = sys.argv[2]

SortByFunctions = {
    'views': lambda x : int(x['statistics']['viewCount']),
    'likes': lambda x : int(x['statistics']['likeCount']),    
    'ratio': lambda x : int(x['statistics']['likeCount'])/int(x['statistics']['viewCount']),
    'scatter' : lambda x : x,
    'random' : lambda x : x 
}    

sortByFunction = SortByFunctions[sortby]

cPerN = sys.argv[3].split(',')
c = int(cPerN[0])
n = None
if len(cPerN) == 2:
    n = int(cPerN[1])

mixin = "mixin"
if len(sys.argv) >= 4:
    mixin = sys.argv[4]

def log(_str):
    original_stdout = sys.stdout 
    with open("log", "a") as f:
        sys.stdout = f
        print(_str)
        sys.stdout = original_stdout

log(playlistIDs)
# youtube = build(YOUTUBE_API_SERVICE_NAME, 
#                 YOUTUBE_API_VERSION, 
#                 credentials=credentials)
#http://www.youtube.com/watch_videos?video_ids=ID1,ID2,ID3,ID4
# print(credentials.to_json())
# youtube.playlistItems().insert(part='snippet', 
#     body = 
#     { 'snippet':{
#         'playlistId': 'PLeYa4Iq4vdY8qeOXuFYRfqB8d1WM9WQve',
#         'resourceId': {
#             'kind': 'youtube#video',
#             'videoId': 'kegNKA3lm9A'
#         }
# }}).execute()
nextPageToken = None                
results = None
playlists = []
for playlistID in playlistIDs:
    video_id_val = []
    while True:
        videos = []        
        results = youtube.playlistItems().list(part='contentDetails', 
                                                playlistId=playlistID,
                                                maxResults=50,
                                                pageToken=nextPageToken).execute()   
        # get video ids
        video_ids = list(map(lambda x : x['contentDetails']['videoId'], 
                                        results['items']))    
        
        videos = youtube.videos().list(part='statistics,snippet', 
                                        id=','.join(video_ids)).execute()

        video_id_val = video_id_val + list(map(lambda x: (x['id'], sortByFunction(x)), videos['items']))

        nextPageToken = results.get('nextPageToken')                                                                                                                          
        if not nextPageToken:            
            playlists.append(video_id_val)
            break                                            

for playlist in playlists:
    playlist.sort(key=lambda x : x[1], reverse=True)
print(sum(playlists, []))
playlists = list(map(lambda ls: ls[:int(c*(len(ls)/n if n != None else 1))], playlists))
    
l = len(sum(playlists, []))
print(l)
if l > 50:
    d = int(50/len(playlists))
    print(d)
    playlists = list(map(lambda ls : ls[:d], playlists))        

all_video_id_val = sum(playlists, [])     
if mixin == "mixin":    
    all_video_id_val.sort(key=lambda x : x[1], reverse=True)

print(all_video_id_val)                      

print(all_video_id_val[:3])
print("http://www.youtube.com/watch_videos?video_ids=" + ','.join(list(map(lambda x : x[0] , all_video_id_val))))
