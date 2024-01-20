
WIN_AGENT = "(Windows NT 10.0; Win64; x64)"

LINUX_AGENT = "(X11; Linux x86_64)"

SERVER_OS = "Windows"

USER_AGENT = f"Mozilla/5.0 {WIN_AGENT} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

TWITTER_ROOT_URL = 'https://twitter.com/i/api/graphql/7DoGe0BiedOgxkJNXr5K0A/TweetDetail'

SNAPCHAT_ROOT_URL = 'https://cf-st.sc-cdn.net/d/'

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
    # 'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7',
    # 'cache-control': 'max-age=0',
    # 'dpr': '1',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.226", "Google Chrome";v="120.0.6099.226"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': f'"{SERVER_OS}"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'user-agent': USER_AGENT,
}

