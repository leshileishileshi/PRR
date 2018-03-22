# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Base
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

import werobot
import yaml

from PPR_WX.Static import conf_path
conf = yaml.load(open(conf_path))
robot = werobot.WeRoBot(token=conf.get('token'))

class App:
    @classmethod
    def Init(cls):
        robot = werobot.WeRoBot(token=conf.get('token'))
        robot.config['HOST'] = conf.get('HOST')
        robot.config['PORT'] = conf.get('PORT')
        robot.config["APP_ID"] = conf.get('APP_ID')
        robot.config["APP_SECRET"] = conf.get('APP_SECRET')

        return robot
