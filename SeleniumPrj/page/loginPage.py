#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/30 10:03
# @Author  : 疏影
# @File    : loginPage.py
from SeleniumPrj.common.base import BaseCommon
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class loginPage():

    def __init__(self,driver):
        self.driver = driver
        self.basecommon = BaseCommon(self.driver)

    def get_input_name(self):
        return self.basecommon.find_element(By.NAME,'name')

    def get_input_password(self):
        return self.basecommon.find_element(By.NAME,'password')

    def get_button_login(self):
        return self.basecommon.find_element(By.CSS_SELECTOR, 'button')

    def get_alert_warning(self):
        return self.basecommon.find_element(By.CLASS_NAME,'alert-danger')

# 测试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://crm.ddhs.51lianqian.net:7035/login')
    page = loginPage(driver)
    time.sleep(1)
    page.get_input_name().send_keys('dddd')
    page.get_input_password().send_keys('dddd')
    page.get_button_login().click()

    if page.get_alert_warning():
        print "OK"