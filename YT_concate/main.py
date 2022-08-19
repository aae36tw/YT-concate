#API : AIzaSyC8F7aeo6gH-LkvuVJ4rRzo3Lg2C6y9iiE

import urllib.request
import json
from settings import API_KEY
print(API_KEY)


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):

    # api_key = os.getenv('API_KEY') 將api_key存至環境變數(搜尋Edit the system...點選enviornment variable)

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + \
        'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
            API_KEY, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


#video_list = get_all_video_in_channel(CHANNEL_ID)

# print(len(video_list))
