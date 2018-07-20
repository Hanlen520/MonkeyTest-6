#coding=utf-8
import Base
import time

class homePage():

    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver
    # 菜单栏-职场发展
    def workplace(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"职场发展\"]")

    #  菜单栏-互联网+
    def internet(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"互联网+\"]")

    # 菜单栏-生活服务
    def lifeService(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"生活服务\"]")

    # 菜单栏-心理
    def mentality(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"心理\"]")

    # 菜单栏-教育学习
    def education(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"教育学习\"]")

    # 菜单栏-投资理财
    def invest(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"投资理财\"]")

    # 菜单栏-个人形象
    def image(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"个人形象\"]")

    # 菜单栏-全部分类
    def allClass(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"全部分类\"]")

    # 消息按钮
    def message(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/relative_layout_message_center_list_entrance")

    # 我的按钮
    def me(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/image_view_personal_center_bg")

    # 搜索框
    def search(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_search")

    # 城市信息
    def city(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_city")
    
    



