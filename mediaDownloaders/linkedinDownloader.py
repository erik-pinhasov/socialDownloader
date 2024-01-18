import json
from mediaDownloaders.util.mediaHandler import *


def extractVideoName(text):
    return formatVideoName(text) if text else 'LinkedinVideo'


def getMaxQualityVideo(url):
    try:
        streamContent = getStreamRequest(url)
        soup = getBeautifulSoup(streamContent)
        scriptTag = soup.find('script', type='application/ld+json')
        jsonData = json.loads(scriptTag.text.strip())
        videoObj = jsonData['video']['contentUrl']
        videoName = extractVideoName(jsonData['video']['description'])
        return videoObj, videoName

    except Exception as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def downloadLinkedinVideo(url):
    videoObj, videoName = getMaxQualityVideo(url)
    return downloadTempFile(videoObj, videoName)
