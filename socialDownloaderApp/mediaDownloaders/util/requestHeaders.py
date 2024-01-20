WIN_AGENT = "(Windows NT 10.0; Win64; x64)"

LINUX_AGENT = "(X11; Linux x86_64)"

SERVER_OS = "Windows"

USER_AGENT = f"Mozilla/5.0 {WIN_AGENT} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

TWITTER_URL = 'https://twitter.com/i/api/graphql/7DoGe0BiedOgxkJNXr5K0A/TweetDetail'

SNAPCHAT_URL = 'https://cf-st.sc-cdn.net/d/'

TWITTER_COOKIES = {
    'auth_token': 'e57a24faea0c67d3c835629ea27ecb9d2aa29b97',
    'ct0': '2f57bb860cf9bffd880cee840acb7281b83be68f7285534b5464fbe12d50a2ce19a66e54f897e5aafc461c3ee05584789a295df36b4b7afec9828fa118e590d5a273afbb8b8f890700bd9cfbf2bbf6d1',
}

TWITTER_HEADERS = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'user-agent': USER_AGENT,
    'x-csrf-token': '2f57bb860cf9bffd880cee840acb7281b83be68f7285534b5464fbe12d50a2ce19a66e54f897e5aafc461c3ee05584789a295df36b4b7afec9828fa118e590d5a273afbb8b8f890700bd9cfbf2bbf6d1',
}

FACEBOOK_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.226", "Google Chrome";v="120.0.6099.226"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': f'"{SERVER_OS}"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'user-agent': USER_AGENT,
}


def generateTwitterParams(videoID):
    return {
        'variables': '{"focalTweetId":' + videoID + ',"with_rux_injections":false,"includePromotedContent":true,"withBirdwatchNotes":true,"withVoice":true}',
        'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'
    }
