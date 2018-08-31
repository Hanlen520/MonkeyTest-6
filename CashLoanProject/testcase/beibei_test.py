#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 13:52
# @Author  : 疏影
# @File    : beibei_test.py

from CashLoanProject.common import config
import requests
import json,datetime
from CashLoanProject.common.addSign import Sign

host = "https://lxbapi.51luocheng.com"

def login_fun():
    url = host + '/v1/authorizations'
    data = {
        "brushed":"1",
        "deviceModel":"oppor7sm",
        "deviceName":"OPPO",
        "deviceToken":"86787602332210513572489850",
        "memorySize":"32",
        "openudid":"867876023322105",
        "password":"qwe123",
        "phone":"13572489850",
        "systemVersion":"5.1.1"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.post(url=url, headers=config.HEADER_ANDROID, data=new_data,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print response
    token = ''
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        print 'response:', str_content.decode("unicode-escape")
        if '10000' == dict_content['status']:
            token = dict_content['data']['info']['token']
            print u'当前token:', token
        else:
            print u'获取token失败'
    return token

def init_fun(headers):
    url = host + '/v1/loan/init'
    s = Sign()
    params = s.signfun({"openudid":"867876023322105"})
    print params
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.get(url=url,headers=headers,params=params,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if 200 == response.status_code:
        # print response.content.decode("unicode-escape")
        print json.dumps(json.loads(response.content), ensure_ascii=False, indent=2)

if __name__ == '__main__':
    token = login_fun()
    headers = config.HEADER_ANDROID
    headers.update({'Authorization':'Bearer ' + token})
    init_fun(headers)