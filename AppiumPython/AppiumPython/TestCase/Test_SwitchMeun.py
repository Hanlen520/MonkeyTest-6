# -*- coding: utf-8 -*-
__author__ = 'ceshiyun'
import unittest,sys,os
# 获取当前文件夹的上层文件夹相对路径
dirpath= os.path.split(os.path.dirname(sys.argv[0]))
# 拼接page、public文件目录路径
page = dirpath[0]+'/Page'
Public = dirpath[0]+'/Public'
sys.path.append(page)
sys.path.append(Public)
from Page import Base, homePage, internetPage, workPlacePage, lifeServicePage
from Page.Base import Base
import time
from appium import webdriver

class SwitchMeun(unittest.TestCase):
    def setUp(self):
        #self.driver = Base.driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Base.capabilities)
        self.homePage = homePage.homePage(self.driver)
        self.internetPage = internetPage.internetPage(self.driver)
        self.workPlacePage = workPlacePage.workPlacePage(self.driver)
        self.lifeServicePage = lifeServicePage.lifeService(self.driver)
        time.sleep(5)

    def test08_Workplace(self):
        self.homePage.workplace().click()
        time.sleep(2)
        workPlacetitle = self.workPlacePage.pagetitle().text
        self.assertEqual(workPlacetitle, "职场发展")
        self.workPlacePage.back().click()
        time.sleep(1)
    '''
    def test09_internet(self):
        self.homePage.internet().click()
        time.sleep(2)
        internettitle = self.internetPage.pagetitle().text
        self.assertEqual(internettitle, "互联网+")
        self.internetPage.back().click()
        time.sleep(1)

    def test10_lifeService(self):
        self.homePage.lifeService().click()
        time.sleep(2)
        lifeServicetitle = self.lifeServicePage.pagetitle().text
        self.assertEqual(lifeServicetitle, "生活服务")
        self.lifeServicePage.back().click()
    '''

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()