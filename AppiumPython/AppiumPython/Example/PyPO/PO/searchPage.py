# -*- coding: utf-8 -*-
import Base,time,unittest
class searchPage():
    driver=Base.Base.driver
    def hot(self):
        time.sleep(4)
        return self.driver.find_element_by_name("热门搜索")
    def search(self):
        time.sleep(5)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_search")
    def insurance(self):
        time.sleep(4)
        return self.driver.find_element_by_name("保险")
    def finan(self):
        time.sleep(4)
        return self.driver.find_element_by_name("理财")
    def sear_click(self):
        self.search().click()
    def asser_search(self):
        self.search()
        self.hot()
        self.search()
        self.insurance()
        self.finan()
