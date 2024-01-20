from socialDownloaderApp.mediaDownloaders.youtubeDownloader import downloadYoutubeVideo
from socialDownloaderApp.mediaDownloaders.facebookDownloader import downloadFacebookVideo
from socialDownloaderApp.mediaDownloaders.instagramDownloader import downloadInstagramVideo
from socialDownloaderApp.mediaDownloaders.twitterDownloader import downloadTwitterVideo
from socialDownloaderApp.mediaDownloaders.linkedinDownloader import downloadLinkedinVideo
from socialDownloaderApp.mediaDownloaders.snapchatDownloader import downloadSnapchatVideo


PLATFORM_INFO = {
    "youtube": {
        "patterns": ["youtube.com", "youtu.be"],
        "downloader": downloadYoutubeVideo,
    },
    "facebook": {
        "patterns": ["facebook.com", "fb.watch"],
        "downloader": downloadFacebookVideo,
    },
    "instagram": {
        "patterns": ["instagram.com"],
        "downloader": downloadInstagramVideo,
    },
    "linkedin": {
        "patterns": ["linkedin.com"],
        "downloader": downloadLinkedinVideo,
    },
    "twitter": {
        "patterns": ["twitter.com"],
        "downloader": downloadTwitterVideo,
    },
    "snapchat": {
        "patterns": ["snapchat.com"],
        "downloader": downloadSnapchatVideo,
    },
}


def detectPlatform(url):
    url = url.lower()
    for platform, info in PLATFORM_INFO.items():
        try:
            if any(pattern in url for pattern in info["patterns"]):
                return info["downloader"]
        except Exception as e:
            print(f"Error detect platform: {e}")
            continue
    return None
