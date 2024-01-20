from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import SNAPCHAT_ROOT_URL


def readFile(path):
    with open(path, 'r') as file:
        content = file.read()
    os.remove(path)
    return content


def getMediaUrl(url, mediaType):
    m3u8Path = downloadTempFile(url, mediaType + 'Playlist')
    mediaUrl = SNAPCHAT_ROOT_URL + extractTextPattern(readFile(m3u8Path), r'#EXT-X-MAP:URI="([^"]+)"')
    return mediaUrl


def processPlaylistFile(m3u8Path):
    m3u8Content = readFile(m3u8Path)
    lines = m3u8Content.splitlines()
    maxResVideo = {"url": "", "resolution": 0}

    for i, line in enumerate(lines):
        if line.startswith('#EXT-X-STREAM-INF'):
            width, height = map(int, re.search(r'RESOLUTION=(\d+)x(\d+)', line).groups())
            resolution = width * height
            if resolution > maxResVideo["resolution"]:
                maxResVideo = {"url": SNAPCHAT_ROOT_URL + lines[i + 1], "resolution": resolution}
        elif 'TYPE=AUDIO' in line:
            audioUrl = getMediaUrl(SNAPCHAT_ROOT_URL + extractTextPattern(line, r'URI="([^"]+)"'), 'audio')

    videoUrl = getMediaUrl(maxResVideo["url"], 'video')
    return videoUrl, audioUrl


def getMaxQualityVideo(videoObj, videoName):
    m3u8Path = downloadTempFile(videoObj['videoTrackUrl']['value'], 'playlist')
    videoUrl, audioUrl = processPlaylistFile(m3u8Path)

    videoPath = downloadTempFile(videoUrl, f"{videoName}_video")
    audioPath = downloadTempFile(audioUrl, f"{videoName}_audio")
    return videoPath, audioPath


def downloadSnapchatVideo(url):
    jsonData = getScriptJson(url, 'application/json')
    videoObj = jsonData['props']['pageProps']['preselectedStory']['premiumStory']['playerStory']
    videoName = videoObj['storyTitle']['value']
    videoPath, audioPath = getMaxQualityVideo(videoObj, videoName)
    return combineVideoAudio(videoPath, audioPath, videoName)
