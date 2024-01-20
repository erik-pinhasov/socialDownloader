import json
import re
import subprocess
import tempfile
import os
import bs4
import requests
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import USER_AGENT


def getStreamRequest(url, params=None, cookies=None, headers=None):
    try:
        if not headers:
            headers = {'user-agent': USER_AGENT}
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        return response.content
    except Exception as e:
        print(f"An error occurred while getting stream request: {e}")
        return None


def getTempPath(name):
    tempDir = tempfile.gettempdir()
    name = name if name else 'video'
    return os.path.join(tempDir, f"{name}.mp4")


def downloadTempFile(url, name):
    try:
        response = requests.get(url)
        tempPath = getTempPath(name)
        with open(tempPath, 'wb') as file:
            file.write(response.content)
        return tempPath
    except requests.RequestException as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def combineVideoAudio(videoPath, audioPath, videoName):
    try:
        tempPath = getTempPath(videoName)
        ffmpegPath = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
        command = [
            ffmpegPath, '-i', videoPath, '-i', audioPath,
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', '-q:v', '1', '-q:a', '1', tempPath
        ]
        subprocess.run(command, check=True)
        os.remove(videoPath)
        os.remove(audioPath)
        return tempPath

    except Exception as e:
        print(f"An error occurred while combining video and audio: {e}")
        return None


def getBeautifulSoup(content):
    return bs4.BeautifulSoup(content, 'html.parser')


def getMaxResolution(objects, tag):
    return max(objects, key=lambda x: int(x.get(tag, 0)), default=None)


def extractTextPattern(url, pattern):
    match = re.search(pattern, url)
    return match.group(1) if match else None


def formatVideoName(name):
    firstLine = name.splitlines()[0]
    return "".join(x if x.isalnum() or x in (" ", ".", "-") else "" for x in firstLine)


def findVideoName(content, platform):
    metaTag = content.find('meta', attrs={'name': 'description'})
    return formatVideoName(metaTag.get('content')) if metaTag else platform + 'Video'


def getScriptJson(url, scriptType):
    streamContent = getStreamRequest(url)
    soup = getBeautifulSoup(streamContent)
    scriptTag = soup.find('script', type=scriptType)
    return json.loads(scriptTag.text.strip())
