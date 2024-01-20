from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import *


def getMaxQualityVideo(videoID):
    try:
        streamContent = getStreamRequest(TWITTER_URL, generateTwitterParams(videoID), TWITTER_COOKIES,
                                         TWITTER_HEADERS)
        jsonData = json.loads(streamContent)
        infoObj = (jsonData['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][0]
        ['content']['itemContent']['tweet_results']['result']['legacy'])
        videoObjs = infoObj['entities']['media'][0]['video_info']['variants']
        videoName = extractVideoName(infoObj['full_text'])
        maxVideo = getMaxResolution(videoObjs, 'bitrate')
        return maxVideo['url'], videoName

    except Exception as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def extractVideoName(text):
    urlPattern = r'https?://[^\s]+'
    name = re.sub(urlPattern, '', text).strip()
    return formatVideoName(name) if name else 'TwitterVideo'


def downloadTwitterVideo(url):
    try:
        videoID = extractTextPattern(url, r'/status/(\d+)')
        videoObj, videoName = getMaxQualityVideo(videoID)
        return downloadTempFile(videoObj, videoName)
    except Exception as e:
        print(f'Error in twitter download: {e}')
        return None
