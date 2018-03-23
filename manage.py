# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manage
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from PRR_WX.Base import APP
from PRR_WX.Static import conf
import fire
# 启动后台


def startUp():
    app = APP.Init()
    app.run(host=conf.get("HOST"), port=conf.get("PORT"), debug=True)


fire.Fire(startUp)
