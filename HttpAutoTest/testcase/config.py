#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import logging
import time
from HttpAutoTest.common.tool import Tool

# URL = 'https://sdhhapi.51yukun.com'
# URL = 'http://api.sdhh.51lianqian.net:7035'
URL = 'http://sdhhapi1.51lianqian.net:7041'
URL_7041 = 'http://sdhhapi1.51lianqian.net:7041'
CELLPHONE = '13572489850'

HEADER_IOS = {
    'Content-Type': 'application/json',
    'platform': 'ios'
}

HEADER_ANDROID = {
    'Content-Type': 'application/json',
    'platform': 'ios'
}

now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
logging.basicConfig(level=logging.INFO,
                    filename='./log/log'+ now +'.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')