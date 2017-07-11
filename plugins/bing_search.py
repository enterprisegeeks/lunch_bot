# -*- encoding: utf-8 -*-

from slackbot.bot import respond_to
import sys
import requests
import json
import re
import os
import urllib.parse

@respond_to('.*', re.IGNORECASE)
def res(message):
    input_text = message.body['text']
    res = call_bing_search_api(input_text)
    message.reply(u'これが知りたいのかな？{0}'.format(res))

# AzureのBING APIを使用して、URLを1つ検索します
# TODO 0件のときの挙動をちゃんとする
def call_bing_search_api(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    headers = {
        'Ocp-Apim-Subscription-Key': os.environ['BING_API_TOKEN'],
    }
    params = {
        'q': query,
        'mkt': 'ja-JP',
        'count': 1,
        'offset': 0,
    }
    response = requests.get(url ,headers = headers, params = params)
    bing_res_url = response.json().get('webPages').get('value')[0]['url']
    encoded_url = re.search("http.*&r=(http.*)&p=.*", bing_res_url).group(1)
    return urllib.parse.unquote(encoded_url)

# 動作確認
if __name__ == '__main__':
    print(call_bing_search_api(u'渋谷でラーメンが食べたいなあ'))
