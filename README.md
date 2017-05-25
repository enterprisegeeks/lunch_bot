# lunch_bot
ランチのレコメンデーションを主な目的としたSlack Botです。

## Requirement
- python3
- slackbotライブラリ
- SLACKのAPI TOKEN
- 使用するプラグインに応じた各種API TOKEN

## Usage
### インストール
このリポジトリをクローンしてください。
Python3をインストールしてください。
Pythonのslackbotライブラリをインストールしてください。

### API TOKENの設定
各種API TOKENは、環境変数から読み込みます。
env_set.shというファイルを作成し、以下のように記述してください。
```
#!/bin/bash

export SLACK_API_TOKEN='xxx'
export GNAVI_API_TOKEN='xxx'
export BING_API_TOKEN='xxx'
```
SLACK_API_TOKENはこのボットを使用するのに必須です。
他のAPI TOKENは、使用するプラグインに応じて設定してください。

### プラグインの設定
slackbot_setting.pyを編集することで、使用するプラグインを変更することができます。
```
# -*- coding: utf-8 -*-

import os

API_TOKEN = os.environ['SLACK_API_TOKEN']

default_reply = "ごめん。わからない。"

PLUGINS = [
    'plugins.bing_search',
]
```

### 起動
以下のコマンドを実行してください。
```
./start_lunch_bot.sh
```

### 停止
以下のコマンドを実行してください。
```
./stop_lunch_bot.sh
```
