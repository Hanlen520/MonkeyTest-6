#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/10 9:35
# @Author  : 疏影
# @File    : 20180810.py
import json

def json_fun():
    str_json = '{"status":"10000","message":"成功","data":{"info":{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLnhqZC41MWxpYW5xaWFuLm5ldDo3MDM1L3YxL2g1L3VzZXIvbG9naW4iLCJpYXQiOjE1MzM4MDg0OTcsImV4cCI6NzUzMzgwODQzNywibmJmIjoxNTMzODA4NDk3LCJqdGkiOiJ4TVdTckxsVUZ5dHJEWldKIiwic3ViIjo4MzAwMDAwMDN9.csmR3vfg9BJxbcBe-B34yEFDK-Cg3eZLf3O0_MyRlbc","expired_at":"2208-09-27 04:33:57","refresh_expired_at":"2208-09-27 04:33:57"}}}'
    # json字符串转换成字典
    dict_json = json.loads(str_json,encoding='gbk')
    print dict_json

    # 将字典转换成json字符串
    str_json = json.dumps(dict_json)
    print(type(str_json))

    # 字典转换成json 存入本地文件
    with open('result.txt','w') as f:
        # 设置不转换成ascii  json字符串首缩进
        f.write(json.dumps(dict_json, ensure_ascii=True, indent=2))

    print json.dumps(dict_json, sort_keys=True, indent=4, separators=(',', ': '))

def lambda_fun():
    s = "lljisjihdi"
    print reduce(lambda x, y: y + x, s)

def map_fun():
    lst = [1,2,3,4,5]
    print map(lambda x:x**2,lst)
    # 提供了两个列表，对相同位置的列表数据进行相加
    print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

    print reduce(lambda x, y: x*y, [1,2,3,4,5])

if __name__ == '__main__':
    map_fun()