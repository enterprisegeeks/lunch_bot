#!/bin/bash

TARGET='lunch_bot.py'

pids=$(ps aux | grep $TARGET | grep -v grep | awk '{ print $2; }')

for pid in $pids
do
    kill $pid
done
