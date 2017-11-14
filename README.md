# youtubeDownloader
Download Youtube Videos/Playlists

Use this program to download all of your favourite Youtube videos and playlists with minimal hassle!

Installing:

1. Using pip, open the terminal and type: `$ pip install beautifulsoup4`.
   (If you don't have pip, go here to install it: https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)
   You will need beautifulsoup in order to retrieve all the links to videos in a playlist.
   And you'll also need pytube: `$ pip install pytube`.

2. If you're using bash on ubuntu on Win10 like me, you'll need to go into the Constants.py file and edit the
   VIDEOS_PATH_WIN constant to point to the drive and location on that drive that you want. Otherwise, this is
   meant to only be compatible only with ubuntu systems (sorry!)
   
3. That's it! Now you just need to know how to call the program.

Usage:

Download.py is what you'll be running in order to get any of the videos you want. The calling syntax looks like this:
   
          $ ./Download.py <video/playlist_url> <video/playlist_name> <playlist_start> <playlist_end>
                  
Note, any of the following '<>' surrounded by '[]' are optional arguments. I recommend using "''" to surround your
video urls and subfolder names, just so that the characters play nicely with the program (thanks!)

1. You can just straight up download a video/whole playlist if you like [to a specific subfolder]:

         $ ./Download.py <video/playlist_url> [<video_name>]
     eg: `$ ./Download.py 'https://www.youtube.com/watch?v=3ZnCrzgM_fU' 'this is a subfolder'`
     
   Note: the subfolder name needs to be less than a certain amount of characters depending on the OS type, so keep that in mind.
   
2. You can also specify how far into a playlist to download:

         $ ./Download.py <playlist_url> <playlist_name> <playlist_start> <playlist_end>
     eg: `$ '/Download.py https://www.youtube.com/watch?v=0GoPRCjEhTc&list=PLYu7z3I8tdEn2m_lLL3Vn7BDwkvMLo_hl' 's' 1 3`
     
   This will download everything on that playlist from video 1 to 3 (inclusive) and they will end up inside the 's' subfolder.
   
   Note: playlists are automatically detected by scanning the url string, which contains '&list=' inside the current Youtube url name structure.
   
Else:

Note that the videos are all downloaded in mp4 format and implicitly in 720p. If you want higher resolutions, go to pytube's website to find out how to increase the deffault res. 
That's it! Happy downloading!
   
