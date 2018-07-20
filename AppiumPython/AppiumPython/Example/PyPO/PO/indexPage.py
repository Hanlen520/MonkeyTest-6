#coding=utf-8
import Base
#在行首页
class indexPage():
    driver=Base.Base.driver
    search=driver.find_element_by_id("com.guokr.mentor:id/text_view_search")
    work_place=driver.find_element_by_name("职场发展")
    internet=driver.find_element_by_name("互联网+")
    life_service=driver.find_element_by_name("生活服务")
    psychology=driver.find_element_by_name("心理")
    tech=driver.find_element_by_name("教育学习")
    def search_click(self):
        self.search.click()