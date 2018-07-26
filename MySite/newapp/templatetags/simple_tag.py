#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/26 13:37
# @Author  : 疏影
# @File    : simple_tag.py

import json
from django import template

register = template.Library()

@register.filter(name='json_dumps')
def json_dumps(value):
    return json.dumps(value, indent=4, separators=(',', ': '), ensure_ascii=False)