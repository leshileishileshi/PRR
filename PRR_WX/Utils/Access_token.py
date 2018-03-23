# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     reply_center
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

import aiohttp
from PRR_WX.Static import conf


async def get_token():
    appid = conf.get("APP_ID")
    secret = conf.get("APP_SECRET")
    async with aiohttp.ClientSession() as sess:
        async with sess.get(f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}") as r:
            token = await r.json()
            return token.get('access_token')
