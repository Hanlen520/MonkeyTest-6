#coding=utf-8
import Base
import time


class mePage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver
    # 我约的行家
    def myExpert(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_tutors_list")

    # 我的心愿单
    def myWish(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"我的心愿单\"]")

    # 我的礼券
    def myGift(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_user_coupon_list")

    # 成为行家
    def specialise(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_apply_tutor")

    # 帮助
    def help(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"帮助\"]")

    # 在线客服
    def service(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"在线客服\"]")

    # 立即登录
    def login(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/relative_layout_user_avatar_area")

    # 登录后用户名
    def username(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_user_nick_name")

    # 设置按钮
    def set(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/image_view_setting")

    # 立即登录标签
    def login_title(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_user_nick_name")
