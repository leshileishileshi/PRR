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

import time
import datetime


class BaseReply(type):
    def __new__(cls, name, bases, attrs):
        return type.__new__(cls, name, bases, attrs)


class Reply_text(metaclass=BaseReply):
    @classmethod
    def Reply_text(cls, to_user, from_user, content):
        """
        以文本类型的方式回复请求
        :param to_user:
        :param from_user:
        :param content:
        :return:
        """
        return """
        <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{}]]></Content>
        </xml>
        """.format(to_user, from_user,
                   int(time.time() * 1000), content)


class Reply(metaclass=BaseReply):
    @classmethod
    def Reply(cls, openid, msg):
        """
        回复逻辑
        :param openid:
        :param msg:
        :return:
        """
        if "日期" == msg:
            return "今天是%s" % datetime.datetime.now().strftime('%Y年%m月%d日 %H时%M分%S秒')
        else:
            return "其他的...\n等等吧...我的功能还很一般."
