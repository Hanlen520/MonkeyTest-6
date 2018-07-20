# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver
import unittest
import time
class ToastDemo(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        #desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName']='Uiautomator2'
        desired_caps['udid'] = '98LFBNP22EYL'
        #desired_caps['app'] = PATH('d:\\testPackage\\v7.0.0_debug_20160729122352291_zhangshuo@rd.apk')
        desired_caps['appPackage'] = 'com.nicksong.toastutil'#'com.ss.android.article.lite'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test1(self):
        time.sleep(5)
        self.driver.find_element_by_id("com.nicksong.toastutil:id/bt_default_toast").click()
        toast_loc=("xpath",".//*[contains(@text,'默认')]")
        e1=WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(toast_loc))
        print(e1.text)
