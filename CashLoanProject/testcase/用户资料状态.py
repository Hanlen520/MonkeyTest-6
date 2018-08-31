#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/15 10:11
# @Author  : 疏影
# @File    : 用户资料状态.py
from CashLoanProject.common import config
import requests
import time,datetime
from CashLoanProject.common.addSign import Sign

host = 'https://bjzapi.51mingyao.com'
def status_fun(headers):
    url = host + '/v1/user/info/status'
    s = Sign()
    params = s.signfun({})
    print params
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.get(url=url,headers=headers,params=params,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if 200 == response.status_code:
        print response.content.decode("unicode-escape")

if __name__ == '__main__':
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0MTM4Nzk3LCJleHAiOjc1MzQxMzg3MzcsIm5iZiI6MTUzNDEzODc5NywianRpIjoiM3dsMWt6R214SFBoeHhQVSIsInN1YiI6OTAwMDAwMDA1fQ.G_HY_jLUatekqvMJKpZRjgkiAQwnl2ifr6V3gMg6PMU'
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3FteWFhcGkuNTFsaWFuZHUuY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0NDczOTMwLCJleHAiOjc1MzQ0NzM4NzAsIm5iZiI6MTUzNDQ3MzkzMCwianRpIjoiTmRrZUhLdlg3Q0RNbzFxWSIsInN1YiI6ODMwMTA1Mjg2fQ.O_aot6sShFJgb2wcrxo_D9YZySl2EPIG_Ez7m5wwheo'
    headers = config.HEADER_ANDROID
    headers.update({'Authorization':'Bearer ' + token})

    status_fun(headers)