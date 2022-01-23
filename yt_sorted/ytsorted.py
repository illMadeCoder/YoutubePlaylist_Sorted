from datetime import datetime
from sys import argv
import youtubeservice
import logservice
import sortservice
import argsservice 

logservice.log(timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
logservice.log(playlistsIDs = argsservice.playlistIDs, mixin=argsservice.mixin, sortby=argsservice.sortby, c=argsservice.c, n=argsservice.n)
playlists = list(map(lambda playlistID : youtubeservice.playlistIDToVideos(playlistID), argsservice.playlistIDs))   
logservice.log(playlists = playlists)

# sort playlists before flatten
for playlist in playlists:
    sortservice.sortVideos(playlist, argsservice.sortby)

# pare down playlists by cByN rules 
playlists = list(map(lambda ls: ls[:int(argsservice.c*(len(ls)/argsservice.n if argsservice.n != None else 1))], playlists))

# if there are more videos than 50 (youtube's untitled playlist limit)   
if len(sum(playlists, [])) > 50:
    # cut from each playlist evenly
    d = int(50/len(playlists))
    playlists = list(map(lambda ls : ls[:d], playlists))        

videos = sum(playlists, [])
if argsservice.mixin == "mixin":    
    sortservice.sortVideos(videos, argsservice.sortby)
videosIDs = list(map(lambda video : video["id"], videos))

videosIDsCSV = ','.join(videosIDs)
print("http://www.youtube.com/watch_videos?video_ids=" + videosIDsCSV)
logservice.commit_log()