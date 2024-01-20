from socialDownloaderApp.mediaDownloaders.util.mediaHandler import *
from socialDownloaderApp.mediaDownloaders.util.requestHeaders import TWITTER_ROOT_URL, TWITTER_COOKIES, TWITTER_HEADERS

def generateReqParams(videoID):
    return {
        'variables': '{"focalTweetId":' + videoID + ',"with_rux_injections":false,"includePromotedContent":true,"withBirdwatchNotes":true,"withVoice":true}',
        'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'
    }


def getMaxQualityVideo(videoID):
    try:
        streamContent = getStreamRequest(TWITTER_ROOT_URL, generateReqParams(videoID), TWITTER_COOKIES, TWITTER_HEADERS)
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
    urlPattern = r'https?://[^\s]+'
    name = re.sub(urlPattern, '', text).strip()
    return formatVideoName(name) if name else 'TwitterVideo'


def downloadTwitterVideo(url):
    videoID = extractTextPattern(url, r'/status/(\d+)')
    videoObj, videoName = getMaxQualityVideo(videoID)
    return downloadTempFile(videoObj, videoName)
