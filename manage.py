# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from PPR_WX.Base import App
robot = App.Init()


# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def echo(message):
    return message.content

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img


robot.run()
