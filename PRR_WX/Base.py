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

# 包管理
from sanic import Sanic
from sanic.response import text
import xml.etree.ElementTree as Element
from PRR_WX.Utils.Validate import Validate
from PRR_WX.Utils.CustomReply import (
    Reply_text,
    Reply
)

class APP:
    @classmethod
    def Init(cls):
        app = Sanic(__name__)

        @app.route("/", methods=["GET", "POST"])
        async def root_path(request):
            # 获取请求方式
            method = request.method
            print("Request method: %s " % method)
            if method == "GET":
                return text(Validate(request=request))
            else:
                """
                收到POST请求就是有信息在公众号里面
                需要解析很多东西
                目前只解析: 文字信息
                """
                # 这里用的request.body
                # xml数据都在body里面
                xml_res = Element.fromstring(request.body.decode("UTF-8"))

                # 解析xml里面的数据. 具体有哪些数据还是要看微信公众号里面的开发文档
                to_user = xml_res.find('ToUserName').text
                from_user = xml_res.find('FromUserName').text
                msg_type = xml_res.find("MsgType").text
                create_time = xml_res.find("CreateTime")

                # 文字信息
                if msg_type == "text":
                    content = xml_res.find('Content').text
                    return text(
                        Reply_text.Reply_text(
                            from_user,
                            to_user,
                            Reply.Reply(
                                from_user,
                                content)))
        return app
