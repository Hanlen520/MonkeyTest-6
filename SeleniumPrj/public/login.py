#coding=utf-8
from SeleniumPrj.common.util import Util
from selenium import webdriver
from SeleniumPrj.page.loginPage import loginPage
from SeleniumPrj.page.navbarPage import navbarPage
import time

class Mylogin():
    def __init__(self, driver):
        self.driver = driver

        #初始化登录的数据
        self.data = Util().operateYaml("../data/inputData/loginData.yaml")
        self.username = self.data['login']['login_data_01']['username']
        self.password = self.data['login']['login_data_01']['pwd']

    def login(self):
        page = loginPage(self.driver)
        name = page.get_input_name()
        password = page.get_input_password()
        btnLogin = page.get_button_login()
        if name and password and btnLogin:
            name.send_keys(self.username)
            password.send_keys(self.password)
            btnLogin.click()
            time.sleep(3)
            navbar = navbarPage(self.driver)
            if self.username == navbar.get_span_name().text:
                print "登录成功"
                return True
        else:
            print "no find elements"
        return False
# 测试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://crm.ddhs.51lianqian.net:7035/login')

    log = Mylogin(driver)
    log.login()