#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import platform

import requests
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 替换成自己机器人的 token
bot_token = '123456:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


def start(bot, update):
    startResponse = '你可以向我发送以下命令:\n\n' \
                    '/anime - 动画\n' \
                    '/comic - 漫画\n' \
                    '/game - 游戏\n' \
                    '/novel - 小说\n' \
                    '/myself - 原创\n' \
                    '/internet - 来自网络\n' \
                    '/other - 其他\n' \
                    '/random - 随机'
    update.message.reply_text(startResponse)


def anime(bot, update):
    yiyan(bot, update, 'a')


def comic(bot, update):
    yiyan(bot, update, 'b')


def game(bot, update):
    yiyan(bot, update, 'c')


def novel(bot, update):
    yiyan(bot, update, 'd')


def myself(bot, update):
    yiyan(bot, update, 'e')


def internet(bot, update):
    yiyan(bot, update, 'f')


def other(bot, update):
    yiyan(bot, update, 'g')


def random(bot, update):
    yiyan(bot, update, 'random')


def yiyan(bot, update, type):
    url = 'https://sslapi.hitokoto.cn/?encode=text&c=' + type
    response = requests.get(url)
    text = response.text
    logger.info("url:%s user:%s text:%s", url, update.message.chat.first_name, text)
    update.message.reply_text(text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
    update.message.reply_text('哎呀, 出错了~~~')


def main():
    if platform.system() == 'Windows':
        request_kwargs = {'proxy_url': 'http://127.0.0.1:1080'}
        updater = Updater(token=bot_token, request_kwargs=request_kwargs)
    else:
        updater = Updater(token=bot_token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', start))

    dp.add_handler(CommandHandler('anime', anime))
    dp.add_handler(CommandHandler('comic', comic))
    dp.add_handler(CommandHandler('game', game))
    dp.add_handler(CommandHandler('novel', novel))
    dp.add_handler(CommandHandler('myself', myself))
    dp.add_handler(CommandHandler('internet', internet))
    dp.add_handler(CommandHandler('other', other))
    dp.add_handler(CommandHandler('random', random))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
