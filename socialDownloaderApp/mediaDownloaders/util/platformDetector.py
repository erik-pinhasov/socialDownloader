from socialDownloaderApp.mediaDownloaders.youtubeDownloader import downloadYoutubeVideo
from socialDownloaderApp.mediaDownloaders.facebookDownloader import downloadFacebookVideo
from socialDownloaderApp.mediaDownloaders.instagramDownloader import downloadInstagramVideo
from socialDownloaderApp.mediaDownloaders.twitterDownloader import downloadTwitterVideo
from socialDownloaderApp.mediaDownloaders.linkedinDownloader import downloadLinkedinVideo
from socialDownloaderApp.mediaDownloaders.snapchatDownloader import downloadSnapchatVideo

PLATFORMS = {
    "youtube": ["youtube.com", "youtu.be"],
    "facebook": ["facebook.com"],
    "instagram": ["instagram.com"],
    "linkedin": ["linkedin.com"],
    "twitter": ["twitter.com"],
    "snapchat": ["snapchat.com"]
}

PLATFORM_DOWNLOADERS = {
    "youtube": downloadYoutubeVideo,
    "facebook": downloadFacebookVideo,
    "instagram": downloadInstagramVideo,
    "twitter": downloadTwitterVideo,
    "linkedin": downloadLinkedinVideo,
    "snapchat": downloadSnapchatVideo
}


def detectPlatform(url):
    url = url.lower()
    for platform, patterns in PLATFORMS.items():
        if any(pattern in url for pattern in patterns):
            return PLATFORM_DOWNLOADERS.get(platform)
    return None
