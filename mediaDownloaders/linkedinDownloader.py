from mediaDownloaders.util.mediaHandler import *


def extractVideoName(text):
    return formatVideoName(text) if text else 'LinkedinVideo'


def getMaxQualityVideo(url):
    try:
        jsonData = getScriptJson(url, 'application/ld+json')
        videoObj = jsonData['video']['contentUrl']
        videoName = extractVideoName(jsonData['video']['description'])
        return videoObj, videoName

    except Exception as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def downloadLinkedinVideo(url):
    videoObj, videoName = getMaxQualityVideo(url)
    return downloadTempFile(videoObj, videoName)
