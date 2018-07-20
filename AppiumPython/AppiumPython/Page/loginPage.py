#coding=utf-8
import Base


class loginPage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver

    # 登录方式-注册
    def register(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/button_register_tab")

    # 登录方式-登录
    def login(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/button_login_tab")

    # 账号输入框
    def username(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/edit_text_login_phone_number")

    # 密码输入框
    def password(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/edit_text_phone_login_password")

    # 登录按钮
    def enter(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_phone_login")

    # 清除输入框数据
    def username_Clear(self):
        username = self.username()
        username.clear()



