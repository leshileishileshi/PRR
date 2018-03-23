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
    TReply,
    Reply_image,
    IReply
)
# 蓝图管理
from PRR_WX.Modules.Material.Views import mt


class APP:
    @classmethod
    def Init(cls):
        app = Sanic(__name__)
        # 注册蓝图
        cls.Register_Bp(app)
        # 基础方法
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
                    if content == '校招群':
                        return text(
                            Reply_image.Reply_image(
                                from_user,
                                to_user,
                                IReply.Reply(
                                    from_user,
                                    content)),)
                    elif content == '社招群':
                        return text(
                            Reply_image.Reply_image(
                                from_user,
                                to_user,
                                IReply.Reply(
                                    from_user,
                                    content)))
                    else:
                        return text(
                            Reply_text.Reply_text(
                                from_user,
                                to_user,
                                TReply.Reply(
                                    from_user,
                                    content)))
                # 处理图片信息
                elif msg_type == "image":
                    content = xml_res.find('MediaId').text
                    a =  Reply_image.Reply_image(
                            from_user,
                            to_user,
                            IReply.Reply(
                                from_user,
                                content))
                    return text(a)
                # 处理语言信息
                elif msg_type == "voice":
                    return text(
                        Reply_text.Reply_text(
                            from_user,
                            to_user,
                            "语音处理还未开发"))
                # 处理事件信息
                elif msg_type == "event":
                    content = xml_res.find('Event').text
                    # 处理订阅事件信息
                    if content in ["subscribe","unsubscribe"]:
                        # 回复文字信息
                        return text(
                            Reply_text.Reply_text(
                                from_user,
                                to_user,
                                TReply.Reply(
                                    from_user,
                                    content)))
                    else:
                        return text(
                            Reply_text.Reply_text(
                                from_user,
                                to_user,
                                "事件处理还未开发"))
        return app

    @classmethod
    def Register_Bp(cls,app):
        app.blueprint(mt)