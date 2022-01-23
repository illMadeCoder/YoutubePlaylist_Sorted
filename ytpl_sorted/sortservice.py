sortByFunctions = {
    'views': lambda x : int(x['statistics']['viewCount']),
    'likes': lambda x : int(x['statistics']['likeCount']),    
    'ratio': lambda x : int(x['statistics']['likeCount'])/int(x['statistics']['viewCount']),
    'scatter' : lambda x : x,
    'random' : lambda x : x 
}    

def sortVideos(videos, sortBy):
    return videos.sort(key=sortByFunctions["ratio" if sortBy == None else sortBy], reverse=True)