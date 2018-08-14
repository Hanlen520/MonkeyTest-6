#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/9 17:18
# @Author  : 疏影
# @File    : md.py
import hashlib

if __name__ == '__main__':
    tel = '13572489850'

    print hashlib.md5(tel).hexdigest()

    with open('tel.txt',"r") as f:
        print hashlib.md5(f.read()).hexdigest()
