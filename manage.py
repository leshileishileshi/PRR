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

app = APP.Init()
app.run(host="0.0.0.0", port=80, debug=True)
