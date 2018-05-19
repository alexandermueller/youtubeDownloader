#!/usr/bin/python

# -*- coding: utf-8 -*-

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
        video = YouTube(video_url, on_progress_callback=on_progress) 

        try:
            print 'Downloading: ' + video.title
            video.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download(filepath)
        except KeyboardInterrupt:
            sys.exit()

    print 'Finished!'

def on_progress(stream, chunk, file_handle, bytes_remaining):
    """On download progress callback function.
    :param object stream:
        An instance of :class:`Stream <Stream>` being downloaded.
    :param file_handle:
        The file handle where the media is being written to.
    :type file_handle:
        :py:class:`io.BufferedWriter`
    :param int bytes_remaining:
        How many bytes have been downloaded.
    """
    filesize       = stream.filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)

def display_progress_bar(bytes_received, filesize, ch='=', scale=0.55):
    """Display a simple, pretty progress bar.
    Example:
    ~~~~~~~~
    PSY - GANGNAM STYLE() MV.mp4
    |----------------| 100.0%
    :param int bytes_received:
        The delta between the total file size (bytes) and bytes already
        written to disk.
    :param int filesize:
        File size of the media stream in bytes.
    :param ch str:
        Character to use for presenting progress segment.
    :param float scale:
        Scale multipler to reduce progress bar size.
    """
    _, columns = get_terminal_size()
    max_width  = int(columns * scale)
    filled     = int(round(max_width * bytes_received / float(filesize)))
    remaining  = max_width - filled
    bar        = ch * filled + ' ' * remaining
    percent    = round(100.0 * bytes_received / float(filesize), 1)
    text       = '-->  [{bar}] {percent}%\r'.format(bar=bar, percent=percent)
    sys.stdout.write(text)
    sys.stdout.flush()

def get_terminal_size():
    """Return the terminal size in rows and columns."""
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
