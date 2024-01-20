import bs4
import requests

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


def checkTwitterShortUrl(url):
    streamContent = requests.get(url, headers=TWITTER_HEADERS)
    soup = bs4.BeautifulSoup(streamContent.content, 'html.parser')
    metaTag = soup.find('meta')
    return metaTag['content'].split('URL=')[1]


def downloadTwitterVideo(url):
    try:
        pattern = r'/status/(\d+)'
        videoID = extractTextPattern(url, pattern)
        if not videoID:
            videoID = extractTextPattern(checkTwitterShortUrl(url), pattern)
        videoObj, videoName = getMaxQualityVideo(videoID)
        return downloadTempFile(videoObj, videoName)
    except Exception as e:
        print(f'Error in twitter download: {e}')
        return None
