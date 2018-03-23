# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from sanic import Blueprint
from sanic.response import json
import aiohttp
from PRR_WX.Utils.Access_token import get_token
mt = Blueprint('Material',)


@mt.route('/mt', methods=['GET', 'POST'])
async def mt_detail(request):
    token = await get_token()
    async with aiohttp.ClientSession() as sess:
        async with sess.get(f'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={token}') as r:
            print(r.url)
            rr = await r.json()
    return json({'my': rr})
