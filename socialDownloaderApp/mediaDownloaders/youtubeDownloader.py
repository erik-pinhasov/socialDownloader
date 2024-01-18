from pytube import YouTube


def downloadYoutubeVideo(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        return video_stream.download()

    except Exception as e:
        print(f'Error in youtube download: {e}')
        return None
