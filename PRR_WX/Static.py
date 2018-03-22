# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Static
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from pathlib import Path
import os
from yaml import load
# 配置文件地址
conf_path = open(Path(os.getcwd()).parent.parent / 'conf.yaml')
conf = load(conf_path)