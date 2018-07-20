#coding=utf-8
import Base
#在行我的页面
class mePage():
    driver=Base.Base.driver
    def wo(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_title")
    def appoint(self):
        return self.driver.find_element_by_name("我约的行家")
