from ast import Lambda
from distutils.command.config import LANG_EXT
from xml.sax.xmlreader import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from locator import*

class BasePageElement(object):
    def __set__(self,obj,value):
        driver=obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name((self.locator).send_keys(value))
    
    def __get__(self,obj,owner):
        driver=obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element=driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
        
