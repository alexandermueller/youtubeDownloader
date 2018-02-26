#!/usr/bin/python

import os
import sys
from os import makedirs
from os.path import *
from pytube import YouTube
from Constants import VIDEOS_PATH, VIDEOS_PATH_WIN
from GetLinks import getLinks

def passesPlaylistCheck(argc, argv):
    return argc >= 1 and not argv[0].isdigit() and argc == 4 and argv[2].isdigit() and argv[3].isdigit() and 'list=' in argv[0]

def main(argc, argv):
    urls     = []
    location = VIDEOS_PATH_WIN if os.name == 'posix' else expanduser(VIDEOS_PATH)
    name     = argv[1] if argc >= 2 else ''

    if argc == 1:
        urls = [argv[0]]
    elif argc == 2 and 'list=' in argv[0]:
        urls = ['https://www.youtube.com%s' % (link) for link in getLinks(argv[0])]
    elif passesPlaylistCheck(argc, argv):
        links = ['https://www.youtube.com%s' % (link) for link in getLinks(argv[0])]
        start = int(argv[2]) - 1 if int(argv[2]) > 0 else 0
        end   = int(argv[3]) if int(argv[3]) > start else start
        urls  = links[start:end]
    else:
        print 'Expected: <video/playlist_url> [<video/playlist_name>, <video/playlist_name> <playlist_start> <playlist_end>]'
        print '    Note: If you want to print 1 video in a playlist, use the number twice'
        print '          - "video_playlist_url marioGame 12 12"'
        return
    
    filepath = '%s/%s' % (location, name) if len(urls) > 0 and name != '' else location 
    
    if not isdir(filepath):
            makedirs(filepath)
    
    for video_url in urls:
        video = YouTube(video_url) 

        print 'Downloading: ' + video.title

        video.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download(filepath)

    print 'Finished!'

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
