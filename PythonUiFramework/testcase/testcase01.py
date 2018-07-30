#coding=utf-8
from common.base import BaseCommon
from public.login import Mylogin
from selenium import webdriver
import unittest
import os
import time
from report import HTMLTestRunner

class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

        self.basecommon = BaseCommon(self.driver)

        
    def tearDown(self):
        print time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        filedir="D:/webtest/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','webtest','screenshot'))
        screen_name = filedir+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+".png"
        self.basecommon.screenshot(screen_name)
        self.driver.quit()
    
    
    def testBaidu01_01(self):

        self.driver.find_element_by_link_text(u'新闻').click()
        time.sleep(2)
        self.basecommon.back()
        time.sleep(2)
        self.basecommon.forward()
        time.sleep(2)
        print "111111"
        self.assertEqual("https://www.baidu.com",self.driver.current_url)
        
        
    def testBaidu01_02(self):

        time.sleep(2)
        self.basecommon.fresh()
        ele = self.basecommon.untilTime("ID",'kw')
        ele.send_keys("123")
        print "test结束"
        
        
if __name__=="__main__":
        #suite = unittest.TestLoader().loadTestsFromTestCase(Testlogin)
        #unittest.TextTestRunner(verbosity=2).run(suite)
        suiteTest = unittest.TestSuite()
        suiteTest.addTest(Testlogin("testBaidu01_01"))
        suiteTest.addTest(Testlogin("testBaidu01_02"))
        filePath = "../report/Result.html"
        fp = file(filePath,'wb')
        #生成报告的Title,描述
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='This is Report')
        runner.run(suiteTest)


