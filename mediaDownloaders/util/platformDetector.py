from mediaDownloaders.youtubeDownloader import downloadYoutubeVideo
from mediaDownloaders.facebookDownloader import downloadFacebookVideo
from mediaDownloaders.instagramDownloader import downloadInstagramVideo
from mediaDownloaders.twitterDownloader import downloadTwitterVideo
from mediaDownloaders.linkedinDownloader import downloadLinkedinVideo

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
}


def detectPlatform(url):
    url = url.lower()
    for platform, patterns in PLATFORMS.items():
        if any(pattern in url for pattern in patterns):
            return PLATFORM_DOWNLOADERS.get(platform)
    return None
