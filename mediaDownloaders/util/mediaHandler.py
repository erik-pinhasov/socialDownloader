import json
import re
import subprocess
import tempfile
import os
import bs4
import requests
from playwright.sync_api import sync_playwright

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def getStreamRequest(url, params=None, cookies=None, headers=None):
    try:
        response = requests.get(url, params=params, cookies=cookies, headers=headers, stream=True)
        return response.text
    except Exception as e:
        print(f"An error occurred while getting stream request: {e}")
        return None


def getTempPath(name):
    tempDir = tempfile.gettempdir()
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
        command = [
            'ffmpeg', '-i', videoPath, '-i', audioPath,
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', '-q:v', '1', '-q:a', '1', tempPath
        ]
        subprocess.run(command, check=True)
        os.remove(videoPath)
        os.remove(audioPath)
        return tempPath

    except Exception as e:
        print(f"An error occurred while combining video and audio: {e}")
        return None


def getPageContent(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context(user_agent=USER_AGENT).new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return getBeautifulSoup(content)


def getBeautifulSoup(content):
    return bs4.BeautifulSoup(content, 'html.parser')


def getMaxResolution(objects, tag):
    return max(objects, key=lambda x: int(x.get(tag, 0)), default=None)


def extractTextPattern(url, pattern):
    match = re.search(pattern, url)
    return match.group(1) if match else None


def formatVideoName(name):
    first_line = name.splitlines()[0]
    return "".join(x if x.isalnum() or x in (" ", ".", "-") else "" for x in first_line)


def findVideoName(content, platform):
    meta_tag = content.find('meta', attrs={'name': 'description'})
    return formatVideoName(meta_tag.get('content')) if meta_tag else platform + 'Video'


def getScriptJson(url, scriptType):
    streamContent = getStreamRequest(url)
    soup = getBeautifulSoup(streamContent)
    scriptTag = soup.find('script', type=scriptType)
    return json.loads(scriptTag.text.strip())
