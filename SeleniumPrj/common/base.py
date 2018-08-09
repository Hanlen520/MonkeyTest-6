#-*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BaseCommon(object):  
  
    def __init__(self, driver):
        self.driver = driver  
  
    def back(self):
        #浏览器后退按钮 
        self.driver.back()  
  
    def forward(self):  
        #浏览器前进按钮  
        self.driver.forward()  
  
    def openUrl(self, url):  
        self.driver.get(url)
        
    def closeBrowser(self):
        self.driver.close() 
  
    def quitBrowser(self):
        self.driver.quit()
        
    def fresh(self):
        self.driver.refresh()

    def screenshot(self,path):  
        #path = "D:\baidu_img.jpg"
        self.driver.get_screenshot_as_file(path)
        
    def untilTime(self,attrib,attrCont):
        if attrib == "ID":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.ID,attrCont))
                )
        elif attrib == "CLASS_NAME":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME,attrCont))
                )
        elif attrib == "CSS_SELECTOR":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,attrCont))
                )
        elif attrib == "XPATH":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.XPATH,attrCont))
                )
        elif attrib == "LINK_TEXT":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT,attrCont))
                )
        elif attrib == "PARTIAL_LINK_TEXT":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,attrCont))
                )
        return elem

    def find_element(self, identifyBy, c):
        elem = None
        try:
            if identifyBy == By.ID:
                elem = self.driver.find_element_by_id(c)
            elif identifyBy == By.XPATH:
                elem = self.driver.find_element_by_xpath(c)
            elif identifyBy == By.CLASS_NAME:
                elem = self.driver.find_element_by_class_name(c)
            elif identifyBy == By.LINK_TEXT:
                elem = self.driver.find_element_by_link_text(c)
            elif identifyBy == By.PARTIAL_LINK_TEXT:
                elem = self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == By.NAME:
                elem = self.driver.find_element_by_name(c)
            elif identifyBy == By.TAG_NAME:
                elem = self.driver.find_element_by_tag_name(c)
            elif identifyBy == By.CSS_SELECTOR:
                elem = self.driver.find_element_by_css_selector(c)
        except NoSuchElementException as e:
            print "no find this element:",c
            elem = None
        finally:
            return elem