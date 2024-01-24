import instaloader
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import downloadTempFile
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import formatVideoName


def downloadInstagramVideo(url):
    # Handles the download of an Instagram video by extracting the media shortcode from the provided URL, fetching the
    # video details using Instaloader, and saving the video file with an appropriately formatted name.
    try:
        insLoader = instaloader.Instaloader()
        media = instaloader.Post.from_shortcode(insLoader.context, url.split("/")[-2])
        videoName = formatVideoName(media.caption) if media.caption else "InstagramVideo"
        return downloadTempFile(media.video_url, videoName)

    except Exception as e:
        print(f"Error in instagram download: {e}")
        return None
