#coding=utf-8
import Base
#在行发现tab页
class discoverPage():
    driver=Base.Base.driver
    def praise(self):
        return self.driver.find_element_by_name("好评")
    def fresh(self):
        return self.driver.find_element_by_name("新鲜")
    def expert(self):
        return self.driver.find_element_by_name("行家有空")