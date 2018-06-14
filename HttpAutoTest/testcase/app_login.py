#!/user/bin/env python
# -*- coding:utf-8 -*-
from config import *

def login_testcase01():
    url = URL + '/v1/authorizations'

    data = {
        "phone":"13572489850",
        "password":"qwe123",
        "openudid":"7d2d43e69fb2c70b31e2f606ba425a517c54e4f0",
        "deviceName":'祝材的 iPhone',
        "deviceToken":"2d2deb394acbe9ffc6601dc3a9d294ef683c239585508a82679432b6b58ddf0d",
        "memorySize":"16",
        "systemVersion":"10.3.3",
        # "sign":"444DAC1826A4A28CC7003D9B28EDBFC4",
        # "timestamp":"1524731734",
        "deviceModel":"iPhone 6 Plus"
    }
    print data
    data_android={
        "brushed":"1",
        "deviceModel":"oppor7sm",
        "deviceName":"OPPO",
        "deviceToken":"86787602332210513572489850",
        "memorySize":"32",
        "openudid":"867876023322105",
        "password":"qwe123",
        "phone":"13572489850",
        "systemVersion":"5.1.1",
        # "timestamp":"1527040590",
        # "sign":"2187F243F41C5DD42D4106192A4F162C"
    }

    t = Tool()
    new_data = t.signfun(data)

    # 以json形式发送post请求
    s = json.dumps(new_data)
    logging.info(u'发送请求：'+ url)
    logging.info(u'发送请求-data：' + s)
    response = requests.post(url=url,headers=HEADER_IOS, data=s)
    token = ""
    logging.info(u'响应：' + response.content)
    if response.status_code == 200:
        print response.content.decode("unicode-escape")
        token = response.json()['data']['info']['token']
    logging.info(u'当前token：' + token)
    return token

if __name__ == '__main__':
    login_testcase01()