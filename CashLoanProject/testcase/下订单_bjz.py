#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/20 17:57
# @Author  : 疏影
# @File    : 下订单_bjz.py

from CashLoanProject.common import config
import requests
import json,datetime
from CashLoanProject.common.addSign import Sign

host = 'https://bjzapi.51mingyao.com'
# host = 'https://qmyaapi.51liandu.com'
def loan_fun(headers):
    url = host + '/v1/loan'
    data = {
        "money":"2500",
        "blackBox":"eyJ0b2tlbklkIjoiOStHOTEzNStxNHhJNmpEWWFjc0FWdFFPQUNKRThhQnZMMGFvTW1QV2FnaDI3WmJRMXpRbzIrYUM3SitNTVpLZjRncmxvWUoxdktISk0zNENmT0hkeFE9PSIsIm9zIjoiaU9TIiwicHJvZmlsZVRpbWUiOjIwNywidmVyc2lvbiI6IjMuMS4wIn0=",
        "device_id":"572774"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.post(url=url, headers=headers, data=new_data,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print response

    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        print 'response:', str_content.decode("unicode-escape")

if __name__ == '__main__':
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0NzU5MDE4LCJleHAiOjc1MzQ3NTg5NTgsIm5iZiI6MTUzNDc1OTAxOCwianRpIjoicWc1SzIwRTJ1RFo2UlIybCIsInN1YiI6OTAwMDAwMDEwfQ.QqEd4PMO51fvJVTfiyUqD0xl_ZovSKCvx81yByy5g7Q'
    headers = config.HEADER_ANDROID
    headers.update({'Authorization':'Bearer ' + token})

    for i in range(2):
        loan_fun(headers)