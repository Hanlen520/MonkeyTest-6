#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/30 9:44
# @Author  : 疏影
# @File    : firefoxTest.py
from selenium import webdriver
import time
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')

    time.sleep(3)
    driver.quit()