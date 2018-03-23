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


class Reply_image(metaclass=BaseReply):
    @classmethod
    def Reply_image(cls, to_user, from_user, content):
        """
        以图片类型的方式回复请求
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
            <MsgType><![CDATA[image]]></MsgType>
            <Image><MediaId><![CDATA[{}]]></MediaId></Image>
        </xml>

        """.format(to_user, from_user,
                   int(time.time() * 1000), content)

class Reply_event(metaclass=BaseReply):
    @classmethod
    def Reply_event(cls, to_user, from_user, content):
        """
        以图片类型的方式回复请求
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
            <MsgType><![CDATA[image]]></MsgType>
            <Image><MediaId><![CDATA[{}]]></MediaId></Image>
        </xml>

        """.format(to_user, from_user,
                   int(time.time() * 1000), content)
class TReply(metaclass=BaseReply):
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
        elif "subscribe" == msg:
            return "欢迎又回来了"
        elif "unsubscribe" == msg:
            return "你忍心吗？"
        else:
            return "原谅代码狗团队的唯一一只正在加班\n."


class IReply(metaclass=BaseReply):
    @classmethod
    def Reply(cls, openid, msg):
        """
        回复逻辑
        :param openid:
        :param msg:
        :return:
        """
        if "社招群" == msg:
            return "iGuMlRP5N9V-FLgB0y6LbJz5kKNK-N9VnKXkVvK6YwR0Z8sd1BXEToc7qsIfVkas"
        elif "校招群" == msg:
            return "sVxyYaSiBHbbNLuHlJujvx5g1WC2K34BHTRidDZc9TPqIeFn3l_CEhWOtWkz1cWP"
        else:
            # 什么都不做，回复对方发送的图片
            return msg

class EReply(metaclass=BaseReply):
    @classmethod
    def Reply(cls, openid, msg):
        """
        回复逻辑
        :param openid:
        :param msg:
        :return:
        """
        if "社招群" == msg:
            return "iGuMlRP5N9V-FLgB0y6LbJz5kKNK-N9VnKXkVvK6YwR0Z8sd1BXEToc7qsIfVkas"
        elif "校招群" == msg:
            return "sVxyYaSiBHbbNLuHlJujvx5g1WC2K34BHTRidDZc9TPqIeFn3l_CEhWOtWkz1cWP"
        else:
            # 什么都不做，回复对方发送的图片
            return msg