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

def dict_json(dict):
    return json.dumps(dict, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    # fun1()
    dict = {'test': {'name': u'test_i00', u'request': {u'url': u'/v1/init/faceInfo', 'headers': {u'timestamp': u'123456'}, u'data': {u'pay_way': u'3'}, u'method': u'GET'}}}

    dict = {u'test': {u'request': {u'url': u'/v1/init/faceInfo', u'headers': {u'test': [{u'value': u'ios', u'key': u'platform'}, {u'value': u'3', u'key': u'pay_way'}]}, u'request_data': {u'test': [{u'type': u'string', u'value': u'1532312327', u'key': u'timestamp'}, {u'type': u'string', u'value': u'F5402E87A417C25CFDE5E49230657DE6', u'key': u'sign'}]}, u'type': u'params', u'method': u'GET'}, u'name': {u'project': u'sdhh', u'include': [], u'remark': u'\u6d4b\u8bd5', u'author': u'\u4eba\u5458A', u'case_name': u'test05'}, u'parameters': {}}}
    dict = {u'test': {u'request': {u'url': u'/v1/init/faceInfo', 'headers': {u'pay_way': u'3'}, u'data': {u'timestamp': u'1532312327'}, u'method': u'GET'}, 'name': u'test06', u'parameters': {}}}
    print dict_json(dict)