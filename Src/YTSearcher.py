'''
Created by Ryan Stewart
September 18, 2016
More at http://www.github.com/ryanstewartalex

Summary: Searches for youtube playlists and returns the videos in them. I made this as a test for using APIs in Python =)
'''

#imports
import time as t
import urllib
import json
import requests

#variables
YT_key = "AIzaSyAaHig61lLWWh17cNrlKXra4O1MpItBjiE"

#return playlist for the searched term
def get_playlist(query):
        response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={}&type=playlist&order={}&key={}".format(query, "relevance",  YT_key))
        data = response.json()
        if len(data["items"]) == 0:
                return -1
        else:
                return data["items"][0]["id"]["playlistId"]



#return videos in playlist
def get_videos(id):
        response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&key={}".format(id, YT_key))
        data = response.json()
        return data

#go to video
def get_direct_video(vid_id):
        return "https://www.youtube.com/watch?v={}".format(vid_id)

#prompt user
def main():
        i = raw_input("\nEnter a search term here: ")
        pid = get_playlist(i)

        if pid == -1:
                print("No results found")
        else:
                print("Videos for \"{q}\": ".format(q=i))
                for video in get_videos(pid)["items"]:
                        vid_id = video["snippet"]["resourceId"]["videoId"]
                        print("\t" + video["snippet"]["title"] + ": " + get_direct_video(vid_id))
        main()

#init
main()
