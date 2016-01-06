#!/usr/bin/env python
# encoding: utf-8

__author__ = 'kamal@belajar.github.io'

import sys
import time
import urllib

import requests
import telegram
import html2text

from telegram.forcereply import ForceReply

def get(param):
    offset = 0
    length = None
    params = param.split()
    url = params[0].strip()
    if len(params) == 2:
        length = int(params[1])
    elif len(params) == 3:
        offset = int(params[1])
        length = int(params[2])

    try:
        resp = requests.get(url)
    except Exception as e:
        print e
        return 'Error'

    out = html2text.html2text(resp.text)
    if offset > 0:
        return out[offset:length]
    if length is None:
        return out
    return out[:length]

def main(token):
    bot = telegram.Bot(token)  # Telegram Bot Authorization Token

    global LAST_UPDATE_ID

    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  # Get lastest update
    except IndexError:
        LAST_UPDATE_ID = 0

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id

            if LAST_UPDATE_ID < update_id:  # If newer than the initial
                                            # LAST_UPDATE_ID
                if text:
                    output = get(text)
                    try:
                        bot.sendMessage(chat_id=chat_id, text=output, reply_markup=ForceReply())
                    except Exception as e:
                        print e
                        bot.sendMessage(chat_id=chat_id, text='Error')

                    LAST_UPDATE_ID = update_id

        time.sleep(2)

if __name__ == '__main__':
    main(sys.argv[1])
