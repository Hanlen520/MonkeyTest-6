#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/14 14:09
# @Author  : 疏影
# @File    : temp.py
from CashLoanProject.common import config
import requests
import json
from CashLoanProject.common.addSign import Sign

if __name__ == '__main__':
    data = {
        'version':'1.0.1'
    }
    s = Sign()
    new_data = s.signfun(data)
    print new_data