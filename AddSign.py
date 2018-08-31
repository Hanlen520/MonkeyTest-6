#!/usr/bin/env python
# encoding: utf-8
"""
@author:lichengyan
@file: AddSign.py
@time: 2018/8/13 23:09
"""
from Crypto.Cipher import AES
import base64,json
import hashlib
import time

PADDING = '\0'
# pkcs5padding
pad_it = lambda s: s+(16 - len(s)%16)*chr(16 - len(s) % 16)

class AddSign():
    def __init__(self):
        pass
    def encrypt(self,pswStr):
        generator = AES.new('kaledaimall98765', AES.MODE_CBC, 'kaledaimall98765')
        crypt = generator.encrypt(pad_it(pswStr))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr

    def md5(self,str):
        md5_pwd = hashlib.md5()
        # 158 9544b351297a40b18cb5252eb7cdedd60 0876019
        md5_pwd.update(str)
        # print u"sign加密后：",md5_pwd.hexdigest()
        return md5_pwd.hexdigest()

    # 接口sign加密
    def sign(self,data,app_key):
        # 当前时间戳
        now = int(time.time())
        data['timestamp'] = str(now)
        # 键排序
        arrays=[]
        for key in data.keys():
            if key not in['sign','key','token']:
                arrays.append(key)
        # print arrays
        new_arrays = sorted(arrays)
        # print new_arrays

        new_str = ""
        for key in new_arrays:
            new_str += key +"="+data[key]+"&"
        new_str = new_str + 'key='+ app_key
        md5_str = self.md5(new_str)

        # 转换大写
        upper_str = str(md5_str).upper()
        # print upper_str

        data['sign'] = upper_str

        return data

if __name__ == '__main__':
    t = AddSign()
    data={}
    app_key = 'frapkkxookfjisksiakd26oo'
    new_data = t.sign(data,app_key)
    print new_data