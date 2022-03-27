# Youtube Mixtape
![image](https://user-images.githubusercontent.com/11481438/160301736-989898a0-4e78-41af-87c7-103195bb817d.png)

Welcome to one half of Youtube Mixtape Application (Backend), a Google Chrome Extension that automates the process of sorting and merging mutiple Youtube Playlists into a single 'Mixtape'. A Mixtape in this context is a Youtube Generated Playlist based a set of parameters provided to the mixing algorithm including:
1. The list of Youtube User Playlists to source from,
2. Sort Criteria : by views, likes, likes/views, or random,
3. The amount of videos to pull per playlist or the total amount agnostic to the playlist's (max of 50),
4. Whether to perform the Sort Criteria per playlist or on the mixtape as a whole

This repository represents the web api that the chrome extension utilizes as a service to perform the playlist merge algorithm - to view the chrome extension repo itself look here: https://github.com/illmadecoder/ytpl_sorted_chrome_extension.

## Getting Started
This application can be run as a commandline application (main.py) but is primarily intended as a webapi (webapi.py).


