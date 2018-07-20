#coding=utf-8
import Base, time

class cityPage():
    #driver = Base.Base.driver
    def __init__(self,driver):
        self.driver=driver
    # 页面标题
    def pagetitle(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/text_view_choose_city")

    # 切换北京城市
    def changebeijing(self):
        return self.driver.find_element_by_xpath("//android.widget.GridView[@resource-id=\"com.guokr.mentor:id/gridview\"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")

    # 关闭窗口按钮
    def closewindow(self):
        return self.driver.find_element_by_id("com.guokr.mentor:id/image_view_close_choose_city")

