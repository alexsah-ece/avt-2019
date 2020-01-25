import subprocess
import youtube_dl
import sys

links = []

with open('links.txt', 'r') as f:
    for line in f:
        links.append(line.rstrip('\n'))

class SimpleLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        sys.exit()


def hook_handler(d):
    if d['status'] == 'finished':
        print(f"{d['filename']} Done downloading, now converting ...")
    elif d['status'] ==  'downloading':
        print(d['filename'], d['eta'], 'sec')


# For options check https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
ydl_opts = {
    'format': 'best[width<=720]', # We want 720p videos if they are available
    'logger': SimpleLogger(),
    'progress_hooks': [hook_handler],
    'format': 'mp4',
    'restrictfilenames': 'true',
    'merge-output-format': 'mp4',
    'writesubtitles': False, 
    'outtmpl': "videos/%(title)s.%(ext)s",
    'subtitleslangs': ['el'] # Download greek subtitles
}


downloader = youtube_dl.YoutubeDL(ydl_opts)

downloader.download(links)
