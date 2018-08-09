#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/30 17:27
# @Author  : 疏影
# @File    : testcase01.py
from SeleniumPrj.public.login import Mylogin
from SeleniumPrj.page.navbarPage import navbarPage
from SeleniumPrj.page.afterSaleOfAllOrderPage import afterSaleOfAllOrderPage
from SeleniumPrj.common.base import BaseCommon
from selenium import webdriver
from SeleniumPrj.common.util import Util
import time
import unittest
import os

# 售后管理-全部订单
class TestAfterSaleOfAllOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.basecommon = BaseCommon(self.driver)

        self.data = Util().operateYaml("../data/pageData/pageData.yaml")
        url = self.data['testAllOrder']['url']
        self.driver.get(url)

    def tearDown(self):
        result_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'result')
        filedir = os.path.join(result_path, "screenshot")
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        screen_name = os.path.join(filedir,time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png")
        print screen_name
        self.basecommon.screenshot(screen_name)
        self.driver.quit()

    def common_fun(self):
        '''进入 售后管理->全部订单页面'''
        log = Mylogin(self.driver)
        navbar = navbarPage(self.driver)
        allorder = afterSaleOfAllOrderPage(self.driver)
        title =''
        if log.login():
            if navbar.get_li_shouhou():
                navbar.get_li_shouhou().click()
                time.sleep(2)
                navbar.get_li_allorder().click()
                time.sleep(2)
                title = allorder.get_h1_title().text
                print title
        self.assertEqual(u"全部订单", title)

    # def testAllOrder_01(self):
    #     '''搜索订单号：DEVELOP-1-1806111337575745'''
    #     self.common_fun()
    #     print "testAllOrder_01:start--->"
    #     allorder = afterSaleOfAllOrderPage(self.driver)
    #     order_no=allorder.get_input_order_no()
    #     count =0
    #     if order_no:
    #         order_no.send_keys(self.data['testAllOrder']['testAllOrder_01']['find_order'])
    #         allorder.get_button_chaxun().click()
    #
    #         table = allorder.get_table_tableData()
    #         table_rows = table.find_elements_by_tag_name('tr')
    #         count = len(table_rows)
    #         print u"总行数(包含标题):", count
    #     self.assertEqual(1, count-1)
    #     print "testAllOrder_01:end--->"

    def testAllOrder_02(self):
        '''重置'''
        self.common_fun()
        print "testAllOrder_02:start--->"
        allorder = afterSaleOfAllOrderPage(self.driver)
        allorder.get_input_name().send_keys(self.data['testAllOrder']['testAllOrder_02']['name'])
        allorder.get_input_user_id().send_keys(self.data['testAllOrder']['testAllOrder_02']['user_id'])
        allorder.get_input_reset().click()

        text1 = allorder.get_input_name().text
        text2 = allorder.get_input_user_id().text

        self.assertEqual("", text1)
        self.assertEqual("", text2)
        print "testAllOrder_02:end--->"

    def testAllOrder_03(self):
        '''搜索渠道'''
        self.common_fun()
        print "testAllOrder_03:start--->"
        allorder = afterSaleOfAllOrderPage(self.driver)

        print "testAllOrder_03:end--->"
