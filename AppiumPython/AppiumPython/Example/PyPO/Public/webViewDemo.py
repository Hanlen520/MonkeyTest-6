# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import os
import unittest
from appium import webdriver
sys.path.append(sys.path[0])
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        #desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['chromeOptions']={'androidProcess': 'com.example.jack.webviewtest'}
        desired_caps['udid'] = '98LFBNP22EYL'
        #desired_caps['app'] = PATH('d:\\testPackage\\v7.0.0_debug_20160729122352291_zhangshuo@rd.apk')
        desired_caps['appPackage'] = 'com.example.jack.webviewtest'#'com.ss.android.article.lite'
        desired_caps['appActivity'] = '.MainActivity' #'.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test1(self):
        time.sleep(2)
        s=self.driver.contexts
        for i in s:
            print i
        print self.driver.current_context
        time.sleep(4)
        self.driver.switch_to.context("WEBVIEW_com.example.jack.webviewtest")
        time.sleep(5)
        print self.driver.page_source
        bb=self.driver.find_element_by_xpath("//*[@id='word']")
        bb.click()
        bb.send_keys("test")
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)