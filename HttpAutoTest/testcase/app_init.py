#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from config import *

def init_testcase01():
    url = URL + '/v1/init/version'
    params= {
        'timestamp': '1526539963',
        'sign':'C2942540A8E2A2C8C9E49B00CB582764'
    }
    response = requests.get(url=url,headers=HEADER_IOS,params=params)

    if 200 == response.status_code:
        print response.content.encode('utf-8')

def init_testcase02():
    url = URL + '/v1/data/notice'
    params= {
        'timestamp': '1526623553',
        'sign':'54B969F367DCD77336B2FF9A83B7ADA0'
    }
    response = requests.get(url=url,headers=HEADER_IOS,params=params)

    if 200 == response.status_code:
        print response.content.decode("unicode-escape")

if __name__ == '__main__':
    init_testcase01()
    init_testcase02()