import json
from mediaDownloaders.util.mediaHandler import *


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

def downloadFacebookVideo(url):
    try:
        pageContent = getPageContent(url)
        videoName = findVideoName(pageContent)
        videoObj, audioObj = maxResVideo(pageContent)

        if not videoObj or not audioObj:
            return None

        videoPath = downloadTempFile(videoObj.get("base_url"), f"{videoName}_video")
        audioPath = downloadTempFile(audioObj.get("base_url"), f"{videoName}_audio")
        if videoPath and audioPath:
            outputPath = combineVideoAudio(videoPath, audioPath, videoName)
            return outputPath
        else:
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
