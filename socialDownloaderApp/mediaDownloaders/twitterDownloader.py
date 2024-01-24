from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import *


def getMaxQualityVideo(videoID):
    # Fetches Twitter video data for the given video ID, finds the highest quality video stream, and returns the video
    # URL and a formatted name for the video.
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
    # Removes URLs from a text string and formats the remaining text to serve as a meaningful video name.
    urlPattern = r'https?://[^\s]+'
    name = re.sub(urlPattern, '', text).strip()
    return formatVideoName(name) if name else 'TwitterVideo'


def checkTwitterShortUrl(url):
    # Checks a shortened Twitter URL and extracts the redirect destination, typically the full Twitter status URL.
    streamContent = requests.get(url, headers=TWITTER_HEADERS)
    soup = bs4.BeautifulSoup(streamContent.content, 'html.parser')
    metaTag = soup.find('meta')
    return metaTag['content'].split('URL=')[1]


def downloadTwitterVideo(url):
    # Processes a Twitter video URL to identify the video ID, fetches the highest quality video stream, and initiates
    # the download of the video file.
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
