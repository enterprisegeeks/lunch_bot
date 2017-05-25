#!/bin/bash

# env_set.shは、以下のコマンドを実行します。
# export SLACK_API_TOKEN='xxx'
# export GNAVI_API_TOKEN='xxx'
# export BING_API_TOKEN='xxx'
source env_set.sh

nohup python3 ./lunch_bot.py > lunch_bot.log 2>&1 &
