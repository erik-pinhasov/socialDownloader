import instaloader
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import downloadTempFile
from socialDownloaderApp.mediaDownloaders.util.mediaHandler import formatVideoName
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import USER_AGENT


def downloadInstagramVideo(url):
    try:
        insLoader = instaloader.Instaloader()
        insLoader.context.get_anonymous_session()
        insLoader.login('erikpinhasov', 'Erer1515')
        insLoader.context.user_agent = USER_AGENT
        media = instaloader.Post.from_shortcode(insLoader.context, url.split("/")[-2])
        videoName = formatVideoName(media.caption) if media.caption else "InstagramVideo"
        return downloadTempFile(media.video_url, videoName)

    except Exception as e:
        print(f"Error in instagram download: {e}")
        return None
downloadInstagramVideo('https://www.instagram.com/p/C0wlbk6o1DI/')