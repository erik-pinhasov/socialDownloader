from mediaDownloaders.youtubeDownloader import downloadYoutubeVideo
from mediaDownloaders.facebookDownloader import downloadFacebookVideo

PLATFORMS = {
    "youtube": ["youtube.com", "youtu.be"],
    "facebook": ["facebook.com"],
    "instagram": ["instagram.com"],
    "linkedIn": ["linkedin.com"],
    "twitter": ["twitter.com"],
    "tikTok": ["tiktok.com"],
    "snapchat": ["snapchat.com"]
}

PLATFORM_DOWNLOADERS = {
    "youtube": downloadYoutubeVideo,
    "facebook": downloadFacebookVideo
}


def detectPlatform(url):
    url = url.lower()
    for platform, patterns in PLATFORMS.items():
        if any(pattern in url for pattern in patterns):
            return PLATFORM_DOWNLOADERS.get(platform)
    return None
