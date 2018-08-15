#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/15 11:04
# @Author  : 疏影
# @File    : 公信宝授权.py
from CashLoanProject.common import config
import requests
import json,datetime
from CashLoanProject.common.addSign import Sign

host = 'https://bjzapi.51mingyao.com'
def gxb_get_token(headers):
    url = host + '/v1/gxb/token'
    params={
        'auth_type':'sesame_multiple',
        'user_id':'900000008'
    }
    s = Sign()
    new_params = s.signfun(params)
    print new_params
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.get(url=url,headers=headers,params=new_params,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    gxb_token=''
    if 200 == response.status_code:
        dict_content = json.loads(response.content)
        if '10000'==dict_content['status']:
            gxb_token = dict_content['data']['token']
        print response.content.decode("unicode-escape")

    return gxb_token

if __name__ == '__main__':
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0Mjk4ODMwLCJleHAiOjc1MzQyOTg3NzAsIm5iZiI6MTUzNDI5ODgzMCwianRpIjoicEtPclJyUlFtYU5WQXZZSCIsInN1YiI6OTAwMDAwMDA4fQ.Z-zts13X1S6HToryFaznN9oMuKSiPHl4ozjde6dMaUI'
    headers = config.HEADER_ANDROID
    headers.update({'Authorization':'Bearer ' + token})

    gxb_token = gxb_get_token(headers)
    print u'当前gxb_token：',gxb_token

    # 芝麻授权地址
    baseurl= "https://prod.gxb.io/v2/auth/sesame_multiple"
    burl ="https://bjzapi.51mingyao.com/v1/gxb/get_auth_result/900000008/sesame_multiple"
    url = baseurl+"?"+burl+"&token="+gxb_token
    print url
