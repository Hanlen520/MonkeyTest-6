#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from common.base import BaseCommon
from common.util import Util
from public.login import Mylogin
from selenium import webdriver
import unittest
import os
import time
from report import HTMLTestRunner

class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.basecommon = BaseCommon(self.driver)
        self.mlogin = Mylogin(self.driver)
        self.data = Util().operateYaml("../data/pageData/pageData.yaml")#取到yaml里边的所有数据
        self.driver.get(self.data['login']['url'])
        
    def tearDown(self):
        
        filedir="D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','test','screenshot'))
        screen_name = filedir+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+".png"
        self.basecommon.screenshot(screen_name)
        self.driver.quit()
    
         
    def testJenkins01_01(self):

        time.sleep(2)
        self.mlogin.login()
        print "success......."
        self.taskdata = Util().operateYaml("../data/pageData/newTaskData.yaml")  # 取到yaml里边的所有数据
        self.driver.find_element_by_link_text(self.taskdata['newtask']['newtask_01']['task']).click()
        txt = self.driver.find_element_by_xpath(self.taskdata['newtask']['newtask_01']['taskHo']).text
        print txt
        self.assertEqual(txt,self.taskdata['newtask']['assert']['username'])
        
        
if __name__=="__main__":
        suiteTest = unittest.TestSuite()
        suiteTest.addTest(Testlogin("testJenkins01_01"))
        filePath = "../report/testResult.html"
        fp = file(filePath,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report for me',description='This is my Report')
        runner.run(suiteTest)


