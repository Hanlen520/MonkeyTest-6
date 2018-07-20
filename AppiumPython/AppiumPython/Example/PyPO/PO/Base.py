#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
import time
from appium import webdriver
class Base():
    capabilities = { 'platformName':'Android',
					 'platformVersion':'5.0.2',
					 'deviceName':'Xperia S',
					 'appPackage':'com.guokr.mentor',
					 'appActivity':'.ui.activity.MainActivity',
					 'unicodeKeyboard':True,
					 'resetKeyboard':True}
    driver=webdriver.Remote('http://localhost:4723/wd/hub',capabilities )
driver=Base().driver




