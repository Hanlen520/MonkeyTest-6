#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/7 13:54
# @Author  : 疏影
# @File    : pre.py
from config import *
import hashlib

host = 'http://api.xjd.51lianqian.net:7035'

def pre_fun():
    url = host + '/v1/user/login/pre'
    data = {
        "phone": "13572489850"
    }

    t = Tool()
    new_data = t.signfun(data)
    print new_data

    # 以json形式发送post请求
    s = json.dumps(new_data)
    logging.info(u'发送请求：'+ url)
    logging.info(u'发送请求-data：' + s)
    response = requests.post(url=url,headers=HEADER_IOS, data=s)

    logging.info(u'响应：' + response.content)
    if response.status_code == 200:
        print response.content.decode("unicode-escape")

def create_fun():
    url = host + '/v1/captcha/create'
    data = {
        "pictureToken": "1533621653000472632"
    }

    t = Tool()
    new_data = t.signfun(data)
    print new_data

    response = requests.get(url=url, headers=HEADER_IOS, params=new_data)
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

    t = Tool()
    new_data = t.signfun(data)
    print new_data

    response = requests.get(url=url, headers=HEADER_IOS, params=new_data)
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
        "pay_type":"3",
        "md5_phone":hashlib.md5("18192496382".encode('utf8')).hexdigest()
        }
    t = Tool()
    new_data = t.signfun(data)
    print new_data

    # 以json形式发送post请求
    s = json.dumps(new_data)
    response = requests.post(url=url,headers=HEADER_IOS, data=s)
    print response
    if response.status_code == 200:
        print response.content.decode("unicode-escape")


if __name__ == '__main__':
    # create_fun()

    # sendcode_fun()

    # register_fun()

    print hashlib.md5("13572489850".encode('utf8')).hexdigest()