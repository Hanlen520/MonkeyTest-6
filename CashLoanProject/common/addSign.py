#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/9 17:32
# @Author  : 疏影
# @File    : addSign.py

from Crypto.Cipher import AES
import base64,json
import hashlib
import time

PADDING = '\0'
# pkcs5padding
pad_it = lambda s: s+(16 - len(s)%16)*chr(16 - len(s) % 16)

APP_KEY='frapkkxookfjisksiakd26oo'

class Sign():
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
    def signfun(self,data):
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
        new_str = new_str + 'key=' + APP_KEY
        md5_str = self.md5(new_str)

        # 转换大写
        upper_str = str(md5_str).upper()
        # print upper_str

        data['sign'] = upper_str

        return data

if __name__ == '__main__':
    # cellphone = '15800876020'
    # psw = '456456'
    # print encrypt(psw)
    #
    # md5(cellphone[:3] + "9544b351297a40b18cb5252eb7cdedd6" + cellphone[3:])
    # md5("timestamp=1526623553&key=frapkkxookfjisksiakd26oo")
    s = Sign()
    data = {
        "phone":"13572489850",
        "password":"asd123",
        "openudid":"e73417d85cf6edb42d5471645a30fa55415e55f2",
        "deviceName":"祝材的 iPhone",
        "deviceToken":"30d76a189251375537778c31637a355cbb33531395e1fd033af26dcc1e838fde",
        "memorySize":"16",
        "systemVersion":"10.3.3",
        # "sign":"38ECAE86C42AD3F01F3FCB01C0D5D0D8",
        # "timestamp":"1526635574",
        "deviceModel":"iPhone 6 Plus"
    }
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
        "timestamp":"1527040590",
        "sign":"2187F243F41C5DD42D4106192A4F162C"
    }

    print s.signfun(data)

    print time.localtime()

    print s.signfun({})
