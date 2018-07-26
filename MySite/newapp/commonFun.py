#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/20 15:55
# @Author  : 疏影
# @File    : commonFun.py
import models
import os
import io
import time
import yaml
from django.core.exceptions import ObjectDoesNotExist

def run_by_single(index, base_url, path):
    """
    加载单个case用例信息
    :param index: int or str：用例索引
    :param base_url: str：环境地址
    :return: dict
    """
    config = {
        'config': {
            'name': 'base_url config',
            'request': {
                'base_url': base_url
            }
        }
    }
    testcase_list = []
    testcase_list.append(config)

    try:
        obj = models.TestInfo.objects.get(id=index)
    except ObjectDoesNotExist:
        return testcase_list

    # include = eval(obj.include)
    request = eval(obj.request)
    name = obj.test_name

    project = obj.belong_project
    testcase_dir_path = os.path.join(path, project)

    testcase_list.append(request)

    file_path=os.path.join(path, name +".yml")
    with io.open(file_path, 'w', encoding='utf-8') as stream:
        yaml.dump(testcase_list, stream, indent=4, default_flow_style=False, encoding='utf-8')

def case_info_logic(**kwargs):
    test = kwargs.get('test')

    if 'request' in test.keys():
        if test.get('name').get('case_name') is '':
            return u'测试用例名称不能为空'
        if test.get('request').get('url') is '':
            return u'接口地址不能为空'

        name = test.pop('name')
        test.setdefault('name',name.pop('case_name'))
        test.setdefault('case_info', name)

        request_data = test.get('request').pop('request_data')
        data_type = test.get('request').pop('type')
        if request_data and data_type:
            if data_type == 'json':
                test.get('request').setdefault(data_type, request_data)
            else:
                data_dict = key_value_dict('data', **request_data)
                if not isinstance(data_dict, dict):
                    return data_dict
                test.get('request').setdefault(data_type, data_dict)
        headers = test.get('request').pop('headers')
        if headers:
            test.get('request').setdefault('headers', key_value_dict('headers', **headers))

        kwargs.setdefault('test', test)

def key_value_dict(keyword, **kwargs):
    """
    字典二次处理
    :param keyword: str: 关键字标识
    :param kwargs: dict: 原字典值
    :return: ok or tips
    """
    if not isinstance(kwargs, dict) or not kwargs:
        return None
    else:
        dicts = {}
        test = kwargs.pop('test')
        for value in test:
            key = value.pop('key')
            val = value.pop('value')
            if 'type' in value.keys():
                type = value.pop('type')
            else:
                type = 'str'

            if key != '' and val != '':
                if keyword == 'headers':
                    value[key] = val
                elif keyword == 'data':
                    msg = type_change(type, val)
                    if msg == 'exception':
                        return '{keyword}: {val}格式错误,不是{type}类型'.format(keyword=keyword, val=val, type=type)
                    value[key] = msg
                dicts.update(value)
        return dicts

def type_change(type, value):
    """
    数据类型转换
    :param type: str: 类型
    :param value: object: 待转换的值
    :return: ok or error
    """
    try:
        if type == 'float':
            value = float(value)
        elif type == 'int':
            value = int(value)
    except ValueError:
        return 'exception'
    if type == 'boolean':
        if value == 'False':
            value = False
        elif value == 'True':
            value = True
        else:
            return 'exception'
    return value
