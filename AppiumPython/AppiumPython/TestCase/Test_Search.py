# -*- coding: utf-8 -*-
__author__ = 'ceshiyun'
import unittest,sys,os
# 获取当前文件夹的上层文件夹相对路径
dirpath= os.path.split(os.path.dirname(sys.argv[0]))
# 拼接page文件路径
page = dirpath[0]+'/Page'
Public = dirpath[0]+'/Public'
#print(Public)
sys.path.append(page)
sys.path.append(Public)
from appium import webdriver
#print(sys.path)
from Page import  homePage, cityPage, searchPage
from Page.Base import Base
import time

class Search(unittest.TestCase):
    def setUp(self):
        #self.driver = Base.driver

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Base.capabilities)
        self.homePage = homePage.homePage(self.driver)
        self.cityPage = cityPage.cityPage(self.driver)
        self.searchPage = searchPage.searchPage(self.driver)
        time.sleep(5)

    def test05_Searchcity(self):
        time.sleep(2)
        self.homePage.city().click()
        time.sleep(1)
        title = self.cityPage.pagetitle().text
        self.assertEqual(title, "选择所在城市")
    '''
    def test06_Changecity(self):
        #切换城市为北京
        self.cityPage.changebeijing().click()
        cityname = self.homePage.city().text
        self.assertEqual(cityname, "北京")

    def test07_hot(self):
        self.homePage.search().click()
        self.searchPage.search().click()
        self.searchPage.search().send_keys("保险")
        time.sleep(2)
        searchresult = self.searchPage.searchresult().text
        self.assertEqual(searchresult, "保险")
    '''
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()