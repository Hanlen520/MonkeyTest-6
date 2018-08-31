#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/27 17:54
# @Author  : 疏影
# @File    : preSendcode.py

from CashLoanProject.common import config
import requests
import json,datetime
from CashLoanProject.common.addSign import Sign
from login_bjz import login_fun

host = 'https://bjzapi.51mingyao.com'

def pre_fun():
    url = host + '/v1/user/login/pre'
    data = {
        "phone": "13572489850"
    }
    s = Sign()
    new_data = s.signfun(data)
    print new_data

    # 以json形式发送post请求
    s = json.dumps(new_data)
    response = requests.post(url=url,headers=config.HEADER_IOS, data=s)

    if response.status_code == 200:
        print response.content.decode("unicode-escape")

def create_fun():
    url = host + '/v1/captcha/create'
    data = {
        "pictureToken": "1533621653000472632"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.get(url=url, headers=config.HEADER_IOS, params=new_data)
    if 200 == response.status_code:
        print response
        with open('picture.jpg', 'wb') as file:
            file.write(response.content)

def sendcode_fun():
    url = host + '/v1/sendcode'
    data = {
        "phone": "13572489850",
        "action":"register",
        "code":"2445",
        "pictureToken":"1533621653000472632"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.get(url=url, headers=config.HEADER_IOS, params=new_data)
    print response
    if 200 == response.status_code:
        print response.content.decode("unicode-escape")

def register_fun():
    url = host + '/v1/register'

    data = {
        "phone": "18192496382",
        "password": "qwe123",
        "code": "354618",
        # "channel_id": "1",
        "pay_type":"3"
        }
    s = Sign()
    new_data = s.signfun(data)
    print new_data

    # 以json形式发送post请求
    s = json.dumps(new_data)
    response = requests.post(url=url,headers=config.HEADER_IOS, data=s)
    print response
    if response.status_code == 200:
        print response.content.decode("unicode-escape")


if __name__ == '__main__':
    create_fun()

    # sendcode_fun()

    # register_fun()

    pre_fun()
