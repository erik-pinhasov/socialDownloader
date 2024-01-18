import instaloader
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import downloadTempFile
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import formatVideoName


def downloadInstagramVideo(url):
    insLoader = instaloader.Instaloader()

    try:
        media = instaloader.Post.from_shortcode(insLoader.context, url.split("/")[-2])
        videoName = formatVideoName(media.caption) if media.caption else "InstagramVideo"
        videoPath = downloadTempFile(media.video_url, videoName)
        return videoPath

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

downloadInstagramVideo('https://www.instagram.com/p/C0wlbk6o1DI/')