#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/2 15:55
# @Author  : 疏影
# @File    : runAll.py
import time
import unittest
import os
import SeleniumPrj.report.HTMLTestRunnerCN as HTMLTestRunnerCN
from testcase01 import TestAfterSaleOfAllOrder

if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestAfterSaleOfAllOrder("testAllOrder_01"))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # html报告文件路径
    result_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'result')
    filePath = os.path.join(result_path, "result_" + now + ".html")
    print 'filePath:',filePath
    fp = file(filePath, 'wb')

    # 生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='Test Report', description='This is Report')
    runner.run(suiteTest)
    fp.close()
