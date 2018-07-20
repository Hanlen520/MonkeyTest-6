#coding=utf-8
import Base


class messagePage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver
    # 消息页面标题
    def title(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/top_bar_text")

    # 返回首页按钮
    def goback(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/top_bar_lefticon")