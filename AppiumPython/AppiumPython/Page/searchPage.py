#coding=utf-8
import Base
import time

class searchPage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver
    # 热门-保险
    def insure(self):
        return self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"保险\"]")
    # 查询结果
    def searchresult(self):
        # return self.driver.find_element_by_id("com.guokr.mentor:id/search_keywords")
        return self.driver.find_element_by_id("com.guokr.mentor:id/search_keywords")

    # 搜索输入框
    def search(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_search")

