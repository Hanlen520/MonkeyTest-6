#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/16 17:28
# @Author  : 疏影
# @File    : psutilTest.py
import psutil

if __name__ == '__main__':
    print psutil.cpu_count()
    print psutil.cpu_count(logical=False)  # CPU物理核心

    print psutil.pids()