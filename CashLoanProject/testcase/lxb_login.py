#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/10 10:39
# @Author  : 疏影
# @File    : lxb_login.py
from CashLoanProject.common import config
import requests
import json
from CashLoanProject.common.addSign import Sign

host = 'https://lxbapi.51luocheng.com'

def login_fun():
    url = host + '/v1/authorizations'
    data = {
        "phone":"13572489850",
        "password":"qwe123",
        "openudid":"7d2d43e69fb2c70b31e2f606ba425a517c54e4f0",
        "deviceName":'祝材的 iPhone',
        "deviceToken":"2d2deb394acbe9ffc6601dc3a9d294ef683c239585508a82679432b6b58ddf0d",
        "memorySize":"16",
        "systemVersion":"10.3.3",
        "deviceModel":"iPhone 6 Plus"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.post(url=url, headers=config.HEADER_IOS, data=data,verify=False)
    print response
    token = ''
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        token = dict_content['data']['info']['token']
        print 'response:',str_content.decode("unicode-escape")
        print 'token:',token
    return token
# token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2x4YmFwaS41MWx1b2NoZW5nLmNvbS92MS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTUzMzg2ODg0MCwiZXhwIjo3NTMzODY4NzgwLCJuYmYiOjE1MzM4Njg4NDAsImp0aSI6Ilh1UzBQdzM3dGFpVjA5b2kiLCJzdWIiOjcwMDAwMTA4MX0.zRXiBURihsrn9OeZrCEYRX_TEprFokVJypkS_3erhSA

if __name__ == '__main__':
    login_fun()