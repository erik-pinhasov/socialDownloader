from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import FACEBOOK_HEADERS


def findMaxResolution(representations):
    # Determines the video with the highest bandwidth and locates the corresponding audio track within a list of media representations.
    maxResoObj = getMaxResolution(representations, "bandwidth")
    audioObj = next((obj for obj in representations if 'audio/mp4' in str(obj.get("mime_type", ''))), None)
    return maxResoObj, audioObj


def findVideoUrl(jsonData):
    # Navigates through a JSON structure to extract URLs for the highest resolution video and its associated audio stream.
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


def maxResVideo(content):
    # Scans the page content for scripts, extracting and returning the highest resolution video and audio objects found.
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
    # Manages the process of downloading the highest resolution video from a Facebook URL, including scraping the page,
    # parsing video data, and combining video and audio tracks.
    try:
        response = getStreamRequest(url, headers=FACEBOOK_HEADERS)
        pageContent = getBeautifulSoup(response)
        videoName = findVideoName(pageContent, 'Facebook')
        videoObj, audioObj = maxResVideo(pageContent)

        videoPath = downloadTempFile(videoObj.get("base_url"), f"{videoName}_video")
        audioPath = downloadTempFile(audioObj.get("base_url"), f"{videoName}_audio")
        outputPath = combineVideoAudio(videoPath, audioPath, videoName)
        return outputPath

    except Exception as e:
        print(f"Error in facebook download: {e}")
        return None
