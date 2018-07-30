#coding=utf-8

from common.util import Util
import yaml
import unittest,time


from selenium import webdriver

class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver
        #初始化登录的数据
        self.data = Util().operateYaml("../data/inputData/loginData.yaml")
        self.username = self.data['login']['login_data_01']['username']
        self.password = self.data['login']['login_data_01']['pwd']

        self.pagedata = Util().operateYaml("../data/pageData/pageData.yaml")

    def login(self):

        self.driver.find_element_by_xpath(self.pagedata['login']['name']).send_keys(self.username)
        self.driver.find_element_by_xpath(self.pagedata['login']['password']).send_keys(self.password)
        self.driver.find_element_by_css_selector(self.pagedata['login']['loginButton']).click()
        time.sleep(3)
        print self.driver.find_element_by_xpath(self.pagedata['login']['loginSuccAssert']).text
            
            


            
    