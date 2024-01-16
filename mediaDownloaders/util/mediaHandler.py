import tempfile
import os
import bs4
import requests
from moviepy.editor import VideoFileClip, AudioFileClip
from playwright.sync_api import sync_playwright


def getTempPath(fileName):
    tempDir = tempfile.gettempdir()
    return os.path.join(tempDir, f"{fileName}.mp4")


def downloadTempFile(url, videoName):
    try:
        response = requests.get(url)
        tempPath = getTempPath(videoName)

        with open(tempPath, 'wb') as file:
            file.write(response.content)
        return tempPath
    except requests.RequestException as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def combineVideoAudio(videoPath, audioPath, videoName):
    try:
        tempPath = getTempPath(videoName)
        videoClip = VideoFileClip(videoPath)
        audioClip = AudioFileClip(audioPath)

        finalClip = videoClip.set_audio(audioClip)
        finalClip.write_videofile(tempPath)

        os.remove(videoPath)
        os.remove(audioPath)
        return tempPath
    except Exception as e:
        print(f"An error occurred while combining video and audio: {e}")
        return None


def getPageContent(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return bs4.BeautifulSoup(content, 'html.parser')


def formatVideoName(name):
    return "".join(x if x.isalnum() or x in (" ", ".", "-") else "" for x in name)
