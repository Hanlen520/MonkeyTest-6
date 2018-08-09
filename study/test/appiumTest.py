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
        #desired_caps['udid'] = '4d00420247913003'
        #desired_caps['app'] = PATH('d:\\testPackage\\v7.0.0_debug_20160729122352291_zhangshuo@rd.apk')
        desired_caps['appPackage'] = 'com.ss.android.article.lite'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test01(self):
        time.sleep(2)
        bb=self.driver.find_elements_by_id("com.ss.android.article.lite:id/afg")[2]
        bb.click()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)