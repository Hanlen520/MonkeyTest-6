#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/15 11:27
# @Author  : 疏影
# @File    : demjsonTest.py
import demjson

if __name__ == '__main__':
    data = {
        "status": "10000",
        "message": "success",
        "data": {
            "token": "0004500598000KaWatb0N5nelZTqqVZt"
        }
    }

    print data
    print demjson.encode(data)