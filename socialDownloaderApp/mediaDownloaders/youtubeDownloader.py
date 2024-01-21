import requests
from pytube import YouTube
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import downloadTempFile


def downloadYoutubeVideo(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        return downloadTempFile(video_stream.url, yt.title)

    except Exception as e:
        print(f'Error in youtube download: {e}')
        return None
