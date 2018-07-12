#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/11 17:50
# @Author  : 疏影
# @File    : jsonTest.py
import json

def fun1():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json1 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    print json1

if __name__ == '__main__':
    fun1()