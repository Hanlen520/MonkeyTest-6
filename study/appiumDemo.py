# coding=utf-8
from appium import webdriver
import unittest
import time,os
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
class appiumDemo(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android' #测试的手机操作系统
        desired_caps['platformVersion'] = '4.2'  #手机操作系统版本
        desired_caps['deviceName'] = 'Android Emulator' #手机类型或模拟器类型
        desired_caps['appPackage'] ='com.ss.android.article.lite' #'com.nicksong.toastutil'#
        desired_caps['appActivity'] = '.activity.SplashActivity' #'.MainActivity'
        self.driver=webdriver.Remote("http://localhost:4827/wd/hub",desired_caps)
        self.width=self.driver.get_window_size()['width']
        self.height=self.driver.get_window_size()['height']
    def tearDown(self):
        self.driver.quit()
    def test3(self):
        time.sleep(5)
        list1=self.driver.find_elements_by_id("com.ss.android.article.lite:id/lr")
        self.assertEqual(list1[0].text,"推荐1")
        self.assertEqual(list1[1].text,"视频")
        self.assertEqual(list1[2].text,"热点")
        self.assertEqual(list1[3].text,"北京")
        self.assertEqual(list1[4].text,"娱乐")
        self.assertEqual(list1[5].text,"图片")
        self.assertEqual(list1[6].text,"懂车帝")
        TouchActions(self.driver).flick_element(list1[6],-0.8*self.width,0,3).perform()
        time.sleep(4)
        self.driver.find_element_by_name("体育")
        self.driver.find_element_by_name("财经")
        self.driver.find_element_by_name("国际")
        self.driver.find_element_by_name("健康")

    def test2(self):
        time.sleep(3)
        self.driver.find_element_by_name("视频").click()
        time.sleep(3)
        hh=self.driver.find_elements_by_id("com.ss.android.article.lite:id/k6")
        for z in range(0,len(hh)):
            if hh[z].text.isdigit():
                #print hh[z].text
                pass
            else:
                print hh[z].text
                raise TypeError
    def test03(self):
        time.sleep(5)
        self.driver.find_element_by_name("任务").click()
        time.sleep(4)
        print '123455'
        aa=self.driver.find_element_by_id("com.ss.android.article.lite:id/g0")
        print aa.text
        self.assertEqual(aa.text,"11")
        self.driver.find_element_by_name("微信一键登录")
        bb=self.driver.find_element_by_id("com.ss.android.article.lite:id/g6")
        self.assertEqual(bb.text,"其它登录方式")
    def test4(self):
        time.sleep(4)
        self.driver.find_elements_by_id("com.ss.android.article.lite:id/w5")[0].click()
        time.sleep(5)
        self.driver.find_element_by_id("com.ss.android.article.lite:id/a_i").click()
        time.sleep(3)
        hh=self.driver.find_element_by_id("com.ss.android.article.lite:id/jh")#评论EditText
        hh.click()
        hh.send_keys(u"好")
        self.driver.find_element_by_id("com.ss.android.article.lite:id/jk").click()#发表
        time.sleep(5)
        self.check_login()
    def check_login(self):
        time.sleep(3)
        zz=self.driver.find_element_by_id("com.ss.android.article.lite:id/eu")
        self.assertEqual(zz.text,"手机号")
        ff=self.driver.find_element_by_id("com.ss.android.article.lite:id/ey")
        self.assertEqual(ff.text,"请输入验证码")
        oo=self.driver.find_element_by_id("com.ss.android.article.lite:id/f2")
        self.assertEqual(oo.text,"进入头条")
        uu=self.driver.find_element_by_id("com.ss.android.article.lite:id/es")
        self.assertEqual(uu.text,"手机登录")


'''
        #查找控件的方式
        #1.通过id查找
        #self.driver.find_element_by_id("")
        #2.通过name查找
        #self.driver.find_element_by_name("")
        #3.通过class_name查找
        #self.driver.find_elements_by_class_name("android.widget.Button")
        #4.通过xpath查找
        #self.driver.find_element_by_xpath("")
        #5.通过uiautomator的方式查找
        # self.driver.find_element_by_android_uiautomator()
        #6.通过uiautomation的方式查找
        #self.driver.find_element_by_ios_uiautomation()

        #对控件操作  以下以element代表控件
        #获取手机屏幕分辨率
        #width=self.driver.get_window_size()['width']  获取宽  920
        #height=self.driver.get_window_size()['height'] 获取高  1080
        #1.点击
        #element.click()
        #2.点击坐标  手机左上角 (0,0)
        #self.driver.execute_script("mobile: tap",{"x":width*0.1,"y":640})
        #3.tap点击
        #TouchAction(self.driver).tap(element).perform()

        #4.滑动flick
        #向上滑动为负数，向下滑动为正数  按住一点进行滑动
        #TouchActions(self.driver).flick(-10,-30).perform()
        #5.对元素进行滑动  向左是负数，向右是整数
        #TouchActions(self.driver).flick_element(element,-100,-100,5).perform()
        #6.swipe滑动  直接滑动
        #startX，startY是滑动的起始坐标；endX和endY是滑动的结束坐标；touchCount (默认 为1): 触摸数量，即手指的个数；
        # duration是滑动的持续时间，单位s。
        #self.driver.execute_script("mobile: swipe",{'startX':100,'startY':100,'endX':100,'endY':200,'tapCount':1,'duration':2})
        #7.长按long_press
        #TouchActions(self.driver).long_press(element).perform()
        #8.按着某个点拖到另一个点  按住点
        #TouchAction(self.driver).press(x=10,y=11).move_to(x=100,y=100).release().perform()

        #9.获取值属性 text
        #e1=element.text
        #10.输入框输入文字
        #desired_caps['unicodeKeyboard']='true'
        #desired_caps['resetKeyboard']='true'
        #首先点击控件 获取到焦点再输入
        #element.click()
        #element.send_keys(u'宝马')
        #11.使用os命令  os命令相当于调用cmd命令
        #os.system("adb shell input text 宝马")
        #12.安卓keycode
        #self.driver.press_keycode(4)

        #断言方式 使用unittest 自带有assert的断言方式
        #1.校验值是否一致  assertEqual  预期值   实际值
        #self.assertEqual(element.text,"搜你想搜")
        #assert cmp("1","2")==0
        #2.校验值不一致
        #self.assertNotEqual("1","2")
        #3.包含关系
        #self.assertIn("你好","你好呀")
        #4.不包含
        #self.assertNotIn("你","他们")
        '''
if __name__ == '__main__':
    '''
    #1.使用unittest的方式执行用例
    suite = unittest.TestLoader().loadTestsFromTestCase(appiumDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''

    #2.使用HTMLTestRunner方式运行生成报告
    #定义一个单元测试容器
    testsuite=unittest.TestSuite()
    #将测试用例加到测试容器中
    testsuite.addTest(appiumDemo("test3"))
    resultDir="C:\\Users\\Jack\\Desktop\\class\\two\\"
    filename=resultDir+'result.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='XXX测试报告',
                    description='以下是XXX项目XXXX版本UI自动化测试报告：')
    #运行测试用例
    runner.run(testsuite)




