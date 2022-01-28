from ytplsorted import ytplsorted
from youtubeservice import playlistIDToPlaylist
import argsservice 

# print(ytplsorted(argsservice.playlistIDs, 
#         argsservice.sortby, 
#         argsservice.mixin, 
#         argsservice.c, 
#         argsservice.n))

print(playlistIDToPlaylist(argsservice.playlistIDs[0]))     