from datetime import datetime
from sys import argv
import youtubeservice
import logservice
import sortservice

def ytplsorted(playlistIDs, sortby, mixin, c, n):
    logservice.log(timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    logservice.log(playlistsIDs = playlistIDs, mixin=mixin, sortby=sortby, c=c, n=n)
    playlists = list(map(lambda playlistID : youtubeservice.playlistIDToVideos(playlistID), playlistIDs))   
    logservice.log(playlists = playlists)

    # sort playlists before flatten
    for playlist in playlists:
        sortservice.sortVideos(playlist, sortby)

    # pare down playlists by cByN rules 
    playlists = list(map(lambda ls: ls[:int(c*(len(ls)/n if n != None else 1))], playlists))

    # if there are more videos than 50 (youtube's untitled playlist limit)   
    if len(sum(playlists, [])) > 50:
        # cut from each playlist evenly
        d = int(50/len(playlists))
        playlists = list(map(lambda ls : ls[:d], playlists))        

    videos = sum(playlists, [])
    if mixin == "mixin":    
        sortservice.sortVideos(videos, sortby)
    videosIDs = list(map(lambda video : video["id"], videos))

    videosIDsCSV = ','.join(videosIDs)
    print("http://www.youtube.com/watch_videos?video_ids=" + videosIDsCSV)
    logservice.commit_log()
