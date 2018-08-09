#!/user/bin/env python
# -*- coding:utf-8 -*-
import locale,json

if __name__ == '__main__':
    a= 1.0
    b=a
    print id(a)
    print id(b)

    a= 1
    b=2.1
    print a+b


    data = {
        "phone":"13572489850",
        "password":"qwe123",
        "openudid":"7d2d43e69fb2c70b31e2f606ba425a517c54e4f0",
        "deviceName":'祝材的 iPhone',
        "deviceToken":"2d2deb394acbe9ffc6601dc3a9d294ef683c239585508a82679432b6b58ddf0d",
        "memorySize":"16",
        "systemVersion":"10.3.3",
        "deviceModel":"iPhone 6 Plus"
    }

    result = json.dumps(data, encoding='UTF-8', ensure_ascii=False)
    print "data = ", result

