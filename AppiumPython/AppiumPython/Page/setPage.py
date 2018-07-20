#coding=utf-8
import Base
import time

class setPage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver
    # 退出按钮
    def logout(self):
        time.sleep(2)
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_logout")