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
