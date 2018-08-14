#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/4 19:52
# @Author  : 疏影
# @File    : testMD5.py
import base64,json
import hashlib
import time


if __name__ == '__main__':
    str ="action=register&code=8205&phone=18192496382&pictureToken=1530704707000438800&key=HDBSBDJNJDNBCHFGDHXKOFDGHFCVBNCf"
    str1='action=register&code=4077&phone=18192496382&pictureToken=1530706764000401049&key=HDBSBDJNJDNBCHFGDHXKOFDGHFCVBNCf'
    hl = hashlib.md5()
    hl.update(str1.encode(encoding='utf-8'))

    print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + hl.hexdigest().upper())