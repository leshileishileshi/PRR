# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     validate_wx_get
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

import hashlib
import sys
from pathlib import Path
import os
# from yaml import
# f = open(Path(os.getcwd()) / 'conf.yaml')
# c = yaml.load(f)
# print(c)


def Validate(request):
    """
    校验token
    :param request: 请求
    :return: str
    """
    # 这里改写你在微信公众平台里输入的token
    token = 'linhanqiu1123'

    # 获取输入参数
    data = request.args
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    echostr = data.get('echostr', '')

    # 字典排序
    list_1 = sorted([token, timestamp, nonce])

    s = list_1[0] + list_1[1] + list_1[2]

    # sha1加密算法
    code = hashlib.sha1(s.encode('utf-8')).hexdigest()

    # 如果是来自微信的请求，则回复echostr
    if code == signature:
        return echostr
    else:
        return ""
