from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *


def extractVideoName(text):
    # Formats the provided text as a video name, defaulting to 'LinkedinVideo' if the text is not provided.
    return formatVideoName(text) if text else 'LinkedinVideo'


def getMaxQualityVideo(url):
    # Retrieves and parses the LinkedIn video metadata from the page's JSON-LD script, extracting the highest
    # quality video URL and its associated name.
    try:
        jsonData = getScriptJson(url, 'application/ld+json')
        videoObj = jsonData['video']['contentUrl']
        videoName = extractVideoName(jsonData['video']['description'])
        return videoObj, videoName

    except Exception as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def downloadLinkedinVideo(url):
    # Proccess downloading a LinkedIn video by extracting the video URL and name, and saving the video file using these details.
    try:
        videoObj, videoName = getMaxQualityVideo(url)
        return downloadTempFile(videoObj, videoName)
    except Exception as e:
        print(f'Error in linkedin download: {e}')
        return None
