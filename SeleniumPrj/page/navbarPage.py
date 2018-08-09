#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/30 15:30
# @Author  : 疏影
# @File    : navbarPage.py
from SeleniumPrj.common.base import BaseCommon
from selenium.webdriver.common.by import By
from selenium import webdriver

class navbarPage():
    def __init__(self,driver):
        self.driver = driver
        self.basecommon = BaseCommon(self.driver)

    # 导航栏上账号
    def get_span_name(self):
        return self.basecommon.find_element(By.CLASS_NAME, 'hidden-xs')

    # 售后管理
    def get_li_shouhou(self):
        return self.basecommon.find_element(By.XPATH, '//*[@class="sidebar-menu"]/li[5]')

    # 售后管理-全部订单
    def get_li_allorder(self):
        return self.basecommon.find_element(By.XPATH, '//*[@class="sidebar-menu"]/li[5]/ul/li[7]')

if __name__ == '__main__':
    from SeleniumPrj.public.login import Mylogin
    import time

    driver = webdriver.Chrome()
    driver.get('http://crm.ddhs.51lianqian.net:7035/login')

    log = Mylogin(driver)
    navbar = navbarPage(driver)
    if log.login():
        if navbar.get_li_shouhou():
            navbar.get_li_shouhou().click()
            time.sleep(2)
            navbar.get_li_allorder().click()