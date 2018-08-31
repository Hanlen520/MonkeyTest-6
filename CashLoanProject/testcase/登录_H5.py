#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/9 17:39
# @Author  : 疏影
# @File    : login.py
from CashLoanProject.common import config
import requests
import json
from CashLoanProject.common.addSign import Sign

def login_fun():
    url = config.HOST + '/v1/h5/user/login'
    data = {
        "phone": "18192496382",
        "password":"qwe123"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.post(url=url, headers=config.HEADER_IOS, data=data)
    print response
    token = ''
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        token = dict_content['data']['info']['token']
        print 'response:',str_content.decode("unicode-escape")
        print 'token:',token
    return token

def getOrderInfo():
    pass

def loan():
    url = config.HOST + '/v1/h5/user/login'
    data = {
        "phone": "18192496382",
        "password":"qwe123"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.post(url=url, headers=config.HEADER_IOS, data=data)
    print response
    token = ''
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)

if __name__ == '__main__':
    token = login_fun()