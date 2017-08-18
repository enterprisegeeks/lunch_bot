# -*- encoding: utf-8 -*-

from slackbot.bot import respond_to
import requests
import json
import re
import os

@respond_to('.*', re.IGNORECASE)
def res(message):
    input_text = message.body['text']
    res_url = call_google_search_api(input_text)
    message.reply(u'これが知りたいのかな？{0}'.format(res_url))

# Google Custom Search APIで検索を行い、1件目のURLを取得します。
# TODO 結果が0件の場合の処理を実装する
def call_google_search_api(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': os.environ['GOOGLE_API_KEY'],
        'cx': os.environ['GOOGLE_CSE_ID'],
        'q': query,
        'num': 1,
        'hl': 'ja',
    }
    response = requests.get(url, params = params)
    json = response.json()
    return json.get('items')[0].get('link')

# 動作確認
if __name__ == '__main__':
    import sys
    args = sys.argv
    q = u'渋谷でラーメンが食べたいなあ' if len(args) == 1 else args[1]
    print(call_google_search_api(q))
