#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/1 14:07
# @Author  : 疏影
# @File    : balcklist.py
from config import *
import base64
import hashlib

def fun():
    url = 'https://fintech.lianqiangroup.com/bms/blacklist/search'
    input={
        "idType": "01",
        "idNo": "342923198705146019",
        "appIds": [
            "yrd",
            "baobao",
            "xzbk",
            "jybk",
            "ddhs"
        ]
    }

    now = int(time.time())
    input_str = json.dumps(input) + base64.b64encode(json.dumps(input)) + 'c71705ff984d6c6ecbf78a5719233a09'
    sign = hashlib.md5(input_str.encode('utf8')).hexdigest()

    params = {
        'transactionType':'search',
        'projectCode':'BLACKLIST',
        'platformId':'xzbk2',
        'signType':'MD5',
        'sign':sign,
        'timestamp':str(now),
        'format':'json',
        'charset': 'UTF-8',
        'version':"1.0.0",
        'input':input
    }

    print base64.b64encode(json.dumps(input))
    s = json.dumps(params)
    response = requests.post(url=url, headers=HEADER_IOS, data=s)
    if response.status_code == 200:
        print response.content

if __name__ == '__main__':
    fun()