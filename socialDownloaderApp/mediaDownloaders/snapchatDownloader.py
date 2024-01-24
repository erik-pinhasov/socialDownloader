from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import SNAPCHAT_URL


def readFile(path):
    # Reads and returns the content of a file from the given path, then deletes the file.
    with open(path, 'r') as file:
        content = file.read()
    os.remove(path)
    return content


def getMediaUrl(url, mediaType):
    # Downloads a media playlist file from a URL, finds the media URL inside it, and returns the full media URL.
    m3u8Path = downloadTempFile(url, mediaType + 'Playlist')
    mediaUrl = SNAPCHAT_URL + extractTextPattern(readFile(m3u8Path), r'#EXT-X-MAP:URI="([^"]+)"')
    return mediaUrl


def processPlaylistFile(m3u8Path):
    # Reads a playlist file, finds the best quality video stream and the associated audio stream, and returns their URLs.
    m3u8Content = readFile(m3u8Path)
    lines = m3u8Content.splitlines()
    maxResVideo = {"url": "", "resolution": 0}

    for i, line in enumerate(lines):
        if line.startswith('#EXT-X-STREAM-INF'):
            width, height = map(int, re.search(r'RESOLUTION=(\d+)x(\d+)', line).groups())
            resolution = width * height
            if resolution > maxResVideo["resolution"]:
                maxResVideo = {"url": SNAPCHAT_URL + lines[i + 1], "resolution": resolution}
        elif 'TYPE=AUDIO' in line:
            audioUrl = getMediaUrl(SNAPCHAT_URL + extractTextPattern(line, r'URI="([^"]+)"'), 'audio')

    videoUrl = getMediaUrl(maxResVideo["url"], 'video')
    return videoUrl, audioUrl


def getMaxQualityVideo(videoObj, videoName):
    # Downloads the playlist for a video, processes it to get the highest quality video and audio URLs, downloads these
    # files, and returns their paths.
    m3u8Path = downloadTempFile(videoObj['videoTrackUrl']['value'], 'playlist')
    videoUrl, audioUrl = processPlaylistFile(m3u8Path)

    videoPath = downloadTempFile(videoUrl, f"{videoName}_video")
    audioPath = downloadTempFile(audioUrl, f"{videoName}_audio")
    return videoPath, audioPath


def downloadSnapchatVideo(url):
    # Fetches video metadata from a Snapchat URL, extracts video details, downloads the highest quality video and its
    # audio, combines them, and returns the final video path.
    try:
        jsonData = getScriptJson(url, 'application/json')
        videoObj = jsonData['props']['pageProps']['preselectedStory']['premiumStory']['playerStory']
        videoName = videoObj['storyTitle']['value']
        videoPath, audioPath = getMaxQualityVideo(videoObj, videoName)
        return combineVideoAudio(videoPath, audioPath, videoName)

    except Exception as e:
        print(f'Error in snapchat download: {e}')
        return None
