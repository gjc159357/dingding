#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time    : 2018-04-08 13:12
# @Author  : Gujc
# @File    : demon1.py
import json

import requests

# url = 'https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# '''
# curl Webhook -H 'Content-Type: application/json' \
#    -d '{"msgtype": "text",
#     "text": {
#         "content": {
#             "username": "test",
#             "password": "test123",
#                     }
#             }
#         }'
# '''
class Dingding(object):

    def __init__(self, token):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % token
        self.headers = {'Content-Type': 'application/json'}

    def send_text(self, text, at_mobiles=[], at_all=False):
        """
        text类型
        {
            "msgtype": "text",
            "text": {
                "content": "我就是我, @156xxxx8827 是不一样的烟火"
            },
            "at": {
                "atMobiles": [
                    "156xxxx8827",
                    "189xxxx8325"
                ],
                "isAtAll": false
            }
        }
        例子: send_text('天气不错', ['13333333333'])
        :param text: 消息类型，此时固定为:text
        :param at_mobiles: 被@人的手机号 ['13333333333', ]
        :param at_all: @所有人时:true,否则为:false
        :return:
        """
        self._send_text(text, at_mobiles, at_all)

    def _send_text(self, text, at_mobiles, at_all):
        data = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": at_mobiles,
                "isAtAll": at_all
            }
        }
        return self._post(data)

    def _post(self, data):
        data = json.dumps(data)
        # s = requests.session()
        r = requests.post(self.url, data=data, headers=self.headers)
        if r.status_code == 200:
            print("success!")

a = Dingding(token)
#a.send_text(text='username:yxdown\npasswd:test', at_mobiles=[], at_all=False)
