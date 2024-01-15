from playwright.sync_api import sync_playwright
import bs4
import json
import requests
import os
from moviepy.editor import VideoFileClip, AudioFileClip


def downloadVideo(url, name):
    try:
        response = requests.get(url)
        with open(name, 'wb') as file:
            file.write(response.content)
        print(f"File {name} downloaded successfully.")
        return os.path.abspath(name)
    except requests.RequestException as e:
        print(f"Failed to download the file. Error: {e}")
        return None


def findMaxResolution(representations):
    maxResoObj = max(representations, key=lambda x: int(x.get("bandwidth", 0)), default=None)
    audioObj = next((obj for obj in representations if 'audio/mp4' in str(obj.get("mime_type", ''))), None)
    return maxResoObj, audioObj


def findVideoUrl(jsonData):
    try:
        firstLevel = jsonData.get('require')[0][3][0]['__bbox']['require']
        for obj1 in firstLevel:
            if obj1[1] == 'next':
                secondLevel = \
                    obj1[3][1]['__bbox']['result']['extensions']['all_video_dash_prefetch_representations'][0][
                        'representations']
                return findMaxResolution(secondLevel)
    except Exception as e:
        print(f"Error in findVideoUrl: {e}")
    return None, None


def findVideoName(content):
    meta_tag = content.find('meta', attrs={'name': 'description'})
    return meta_tag.get('content') if meta_tag else 'FacebookVideo'


def getPageContent(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return bs4.BeautifulSoup(content, 'html.parser')


def maxResVideo(content):
    tags = content.find_all('script')
    for tag in tags:
        try:
            videoObj, audioObj = findVideoUrl(json.loads(tag.get_text(strip=True)))
            if videoObj and audioObj:
                return videoObj, audioObj
        except Exception as e:
            continue
    return None, None


def combineVideoAudio(videoPath, audioPath, outputPath):
    try:
        videoClip = VideoFileClip(videoPath)
        audioClip = AudioFileClip(audioPath)

        finalClip = videoClip.set_audio(audioClip)
        finalClip.write_videofile(outputPath, codec='libx264', audio_codec='aac')


        print(f"Combined video and audio into {outputPath}")
    except Exception as e:
        print(f"An error occurred while combining video and audio: {e}")
    finally:
        os.remove(videoPath)
        os.remove(audioPath)


def downloadFacebookVideo(url):
    try:
        pageContent = getPageContent(url)
        videoName = findVideoName(pageContent)
        videoObj, audioObj = maxResVideo(pageContent)

        if not videoName or not videoObj or not audioObj:
            print("Video name or URL not found.")
            return None

        videoPath = downloadVideo(videoObj.get("base_url"), f"{videoName}_video.mp4")
        audioPath = downloadVideo(audioObj.get("base_url"), f"{videoName}_audio.mp4")

        if videoPath and audioPath:
            outputPath = f"{videoName}.mp4"
            combineVideoAudio(videoPath, audioPath, outputPath)
            return outputPath
        else:
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
