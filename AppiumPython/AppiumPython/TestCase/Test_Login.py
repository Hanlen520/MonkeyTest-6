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
from Page import Base, homePage, mePage, loginPage, messagePage, setPage
from Page.Base import Base
from Public import Data
import time
from appium import webdriver

class Login(unittest.TestCase):
    def setUp(self):
        #self.driver = Base.driver

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Base.capabilities)
        self.homePage = homePage.homePage(self.driver)
        self.mePage = mePage.mePage(self.driver)
        self.messagePage = messagePage.messagePage(self.driver)
        self.loginPage = loginPage.loginPage(self.driver)
        self.setPage = setPage.setPage(self.driver)
        self.Data = Data.Datas()
        time.sleep(5)

    def test01_menu(self):
        time.sleep(2)
        t0 = self.homePage.workplace().text
        t1 = self.homePage.internet().text
        t2 = self.homePage.lifeService().text
        t3 = self.homePage.allClass().text
        #print(t0,t1,t2,t3)
        self.assertEqual(t0, "职场发展")
        self.assertEqual(t1, "互联网+")
        self.assertEqual(t2, "生活服务")
        self.assertEqual(t3, "全部分类")
    '''
    def test02_message(self):
        time.sleep(2)
        self.homePage.message().click()
        time.sleep(2)
        ms_t = self.messagePage.title().text
        self.assertEqual(ms_t, "消息中心")
        self.messagePage.goback().click()

    def test03_login(self):
        time.sleep(2)
        self.homePage.me().click()
        self.mePage.login().click()
        self.loginPage.login().click()
        self.loginPage.username_Clear()
        time.sleep(1)
        logindata = self.Data.loginData()
        #print(logindata[0])
        #print(logindata[1])
        self.loginPage.username().send_keys(logindata[0])
        self.loginPage.password().send_keys(logindata[1])
        self.loginPage.enter().click()
        username = self.mePage.username().text
        self.assertEqual(username, "Joson")

    def test04_logout(self):
        time.sleep(1)
        self.mePage.set().click()
        time.sleep(2)
        self.setPage.logout().click()
        time.sleep(2)
        logoutname = self.mePage.login_title().text
        self.assertEqual(logoutname,"立即登录")
    '''


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
