# -*- encoding: utf-8 -*-

import urllib.parse
import urllib.request
import json
import random
import os
from slackbot.bot import respond_to

# キーワードに反応して、ランチをおすすめします。
@respond_to(u'ランチ')
@respond_to(u'ひるごはん')
@respond_to(u'昼ご飯')
def recommend_lunch(message):
    try:
        message.reply(create_message())
    except Exception as e:
        print(e.message.encode('utf-8'))

# メッセージを構築します。
def create_message():
    lunch = decide_lunch()
    return u'今日のランチはここ！{0}'.format(lunch)

# 今日のランチを決めます。
# TODO 評価によって選択に重みをつけたい
def decide_lunch():
    gnavi_json = call_gnavi_api()
    url_list = to_url_list(gnavi_json)
    return random.choice(url_list)

# ぐるなびAPIにリクエストを送り、レスポンスのjsonを取得します。
# TODO APIトークンをハードコーディングしない
# TODO 緯度経度をハードコーディングしない
# TODO ラーメンなど、食べ物のカテゴリを選べるようにしたい
# TODO 休業日のお店は除外する
def call_gnavi_api():
    params = urllib.parse.urlencode({
        'format': 'json',
        'keyid': os.environ['GNAVI_API_TOKEN'],
        # 緯度経度は日本測地系
        'latitude': '35.65211952',
        'longitude': '139.6958563',
        'range': '2',
        'lunch': '1',
        'hit_per_page': '100',
    })
    try:
        responce = urllib.request.urlopen("http://api.gnavi.co.jp/RestSearchAPI/20150630/?" + params)
        return responce.read().decode('utf-8')
    except:
        raise Exception(u'APIアクセスに失敗しました')

# json形式のデータをパースして、お店のURLの一覧にします。
def to_url_list(data):
    parsed_data = json.loads(data)
    if 'error' in parsed_data:
        if 'message' in parsed_data:
            raise Exception(u'{0}'.format(parsed_data['message']))
        else:
            raise Exception(u'データ取得に失敗しました')
            
    total_hit_count = int(parsed_data.get('total_hit_count', '0'))
    if total_hit_count < 1:
        raise Exception(u'指定した内容ではヒットしませんでした')

    res_list = []
    for (count, rest) in enumerate(parsed_data.get('rest')):
        url = rest.get('url')
        res_list.append(url)
    return res_list

# 動作確認用
if __name__ == "__main__":
    print(create_message())

