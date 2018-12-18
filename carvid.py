#!/usr/bin/env python3

from __future__ import unicode_literals
import youtube_dl
from pprint import pprint
from slugify import slugify

#   Project : YT video download & converter for ///ALPINE IVE-W530BT.
#             6.1 inch wide VGA display (first gen touch screen 2din)
#             compatible formats : MP3, WMA, AAC, DivX
#             pixel limits : 640x360 nHD it seems!

HEIGHT = 640
WIDTH = 360

flags = f"\"scale=(iw*sar)*min({HEIGHT}/(iw*sar)\,{WIDTH}/ih):ih*min({HEIGHT}/(iw*sar)\,{WIDTH}/ih), pad={HEIGHT}:{WIDTH}:({HEIGHT}-iw*min({HEIGHT}/iw\,{WIDTH}/ih))/2:({WIDTH}-ih*min({HEIGHT}/iw\,{WIDTH}/ih))/2\""
scale_and_rename = "ffmpeg -i {} -c:v mpeg4  -q:v 0 -tag:v DIVX -acodec libmp3lame -q:a 0 -ac 2 -ar 48000 -vf " + flags + " $(./renamer.py {}).avi; rm -f {}"
rename = "mv {} $(./renamer.py {}).avi"

# set options for the downloaded videos
configuration = {
    'outtmpl': '%(title)s',
#    'postprocessors': [{
#        'key': 'FFmpegExtractAudio',
#        'preferredcodec': 'mp3',
#        'preferredquality': '320'
#    }],
    'postprocessors': [{
        'key': 'ExecAfterDownload',
        'exec_cmd': scale_and_rename
    }],
}

# read textfile containing youtube links into python list for later.
URLS = []
with open('list.txt', 'r') as file:
    for line in file: 
        link = line.strip() # strip each line at end
        print('link retrieved from file: ', link)
        URLS.append(link) # append to list of URLs

# download the actual content using the configurations set above
with youtube_dl.YoutubeDL(configuration) as ydl:
    ydl.download(URLS) 
