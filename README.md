# Youtube Mixtape
![image](https://user-images.githubusercontent.com/11481438/160301736-989898a0-4e78-41af-87c7-103195bb817d.png)

Welcome to one half of Youtube Mixtape Application (Backend), a Google Chrome Extension that automates the process of sorting and merging mutiple Youtube Playlists into a single 'Mixtape'. A Mixtape in this context is a Youtube Generated Playlist based a set of parameters provided to the mixing algorithm including:
1. The list of Youtube User Playlists to source from,
2. Sort Criteria : by views, likes, likes/views, or random,
3. The amount of videos to pull per playlist or the total amount agnostic to the playlist's (max of 50),
4. Whether to perform the Sort Criteria per playlist or on the mixtape as a whole

This repository represents the web api that the chrome extension utilizes as a service to perform the playlist merge algorithm - to view the chrome extension repo itself look here: https://github.com/illmadecoder/ytpl_sorted_chrome_extension.

## Getting Started
This application can be run as a commandline application (main.py), but is primarily intended as a webapi (webapi.py).

### Without Docker
1. Clone the repository locally
2. pip: -r requirements.txt
3. Create a file ytpl_sorted/config.py with the following global variables defined
```
DEVELOPER_KEY = <A Youtube Developer Key>
PORT = <The Port you'd like to run it on locally>
```
5. python ytpl_sorted/webapi.py

## With Docker
1. Clone the repository locally
2. docker build .
3. docker run -dp \<host port>:\<virtual port> <name of image>
4. ensure the config.py has been setup in ytpl_sorted like so:
```
DEVELOPER_KEY = <A Youtube Developer Key>
PORT = <virtual port>
```

## Using the Youtube Mixtape Endpoint
Once stood up hit the endpoint like so:
1. Find some user made (not youtube generated) playlist on Youtube, 
2. look for the playlist ID at the end of the URL,
3. copy the playlist id and insert it at the end of the following URL http://localhost:8000/ytplsorted?playlistIDs= where the 8000 is replaced by your selected port,
4. continue this process via a comma seperated list for additional playlists.
Example: http://localhost:8000/ytplsorted?playlistIDs=PLvNp0Boas721Oudz2jPmLckTw2Efa1P_8,PL7E5D665B1A8B6898

  
## Fullstack 
### Setup
1. Follow the steps above setup the backend.
2. Follow the steps to setup the frontend located in the frontend repo here https://github.com/illmadecoder/ytpl_sorted_chrome_extension
3. While the Web API is running locally, point the frontend to the Web API's local URL.
