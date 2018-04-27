#!/usr/bin/python3
# coding=utf-8

import requests
import json
import sys
from prettytable import PrettyTable

fmt = '\033[0;3{}m{}\033[0m'.format


class color:
    BLACK = 0  # 黑
    RED = 1  # 红
    GREEN = 2  # 绿
    YELLOW = 3  # 棕
    BLUE = 4  # 蓝
    PURPLE = 5  # 紫
    CYAN = 6  # 青
    GRAY = 7  # 灰


if len(sys.argv) != 3:
    print("参数错误, using: python3 diff.py 你的昵称 对方昵称")
    sys.exit()

response = requests.get('http://netease.wkfg.me/diff?me=' + sys.argv[1] + '&your=' + sys.argv[2])

json_object = json.loads(response.text)

x = PrettyTable(["", "歌曲", "歌手", "专辑", "链接"])

x.align = "l"
x.padding_width = 2

for index, item in enumerate(json_object):
    musicName = fmt(color.GREEN, item['name'].lstrip()[0:20])
    artistNames = fmt(color.PURPLE, item['artistNames'][0:20])
    albumName = fmt(color.CYAN, item['albumName'][0:20])
    musicUrl = item['url']
    x.add_row([index + 1, musicName, artistNames, albumName, musicUrl])

print(x)
