from playwright.sync_api import sync_playwright
import bs4
import json
import requests
import os


def downloadFB(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
        return os.path.abspath(name)  # Return the absolute path of the file
    else:
        print("Failed to download the file. Status code:", response.status_code)
        return None


def findMaxResolution(representations):
    maxBandwidth = -1
    maxResoObj = None

    for obj in representations:
        bandwidth = int(obj.get("bandwidth", 0))  # Convert bandwidth to int, default to 0 if not found
        if bandwidth > maxBandwidth:
            maxBandwidth = bandwidth
            maxResoObj = obj

    return maxResoObj


def findUrl(jsonData):
    firstLevel = jsonData.get('require')[0][3][0]['__bbox']['require']
    for obj1 in firstLevel:
        if obj1[1] == 'next':
            secondLevel = obj1[3][1]['__bbox']['result']['extensions']['all_video_dash_prefetch_representations'][0][
                'representations']
            maxResoObj = findMaxResolution(secondLevel)
    return maxResoObj if maxResoObj else None


def findVideoName(soup):
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    if meta_tag and meta_tag.get('content'):
        return meta_tag['content']


def downloadFacebookVideo(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        soup = bs4.BeautifulSoup(page.content(), 'html.parser')
        browser.close()

        videoName = findVideoName(soup)
        tags = soup.find_all('script')
        urlObjs = []
        for tag in tags:
            try:
                urlObjs.append(findUrl(json.loads(tag.get_text(strip=True))))
            except Exception as e:
                continue
        maxResoObj = findMaxResolution(urlObjs)
        return downloadFB(maxResoObj.get("base_url"), f"{videoName}.mp4")
