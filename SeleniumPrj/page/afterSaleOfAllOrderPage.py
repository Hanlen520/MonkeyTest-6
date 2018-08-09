#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/30 17:12
# @Author  : 疏影
# @File    : afterSaleOfAllOrderPage.py
from SeleniumPrj.common.base import BaseCommon
from selenium.webdriver.common.by import By
from selenium import webdriver

class afterSaleOfAllOrderPage():
    def __init__(self,driver):
        self.driver = driver
        self.basecommon = BaseCommon(self.driver)

    def get_h1_title(self):
        return self.basecommon.find_element(By.XPATH, '//*[@class="content-header"]/h1/small')

    def get_input_order_no(self):
        return self.basecommon.find_element(By.ID, 'order_no')

    def get_table_tableData(self):
        return self.basecommon.find_element(By.ID, 'tableData')

    def get_button_chaxun(self):
        return self.basecommon.find_element(By.XPATH,'//*[@id="btn" and @type="submit"]')

    def get_input_user_id(self):
        return self.basecommon.find_element(By.ID, 'user_id')

    def get_input_name(self):
        return self.basecommon.find_element(By.ID, 'name')

    def get_input_reset(self):
        return self.basecommon.find_element(By.XPATH,'//*[@class="btn" and @type="reset"]')
