
# -*- coding: utf8 -*-
import sys
import os
import subprocess
import time
import re

from robotremoteserver import RobotRemoteServer

import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

class Web_UI:       
    def start(self, url):
        self.driver = webdriver.Chrome("C:\\Users\\ixqa\\Desktop\\robot_work\\chromedriver.exe")
        #self.driver.maximize_window()
        #self.driver = webdriver.Firefox()
        self.driver.get(url)
        
    def get_element(self, by, value, timeout=5):
        """
        Return a WebElement or raise exception
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException as e:
            raise TimeoutException("Fail to see element %s=%s" % (by, value))
            
    def test_element(self, by, value, timeout=5):
        """
        Return a WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException as e:
            return None

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True            
            
    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        return
    def unlike(self):
        time.sleep(3)
        self.get_element(By.XPATH,"//div[@id='player']/div[6]/a/i").click()
        
    def choose_first_radio(self):
        self.get_element(By.CSS_SELECTOR,"div.fix-switch div[id='promote-stations'] li:nth-child(1)").click()
        self.get_element(By.CSS_SELECTOR,"div.fix-switch div[id='promote-stations'] li:nth-child(1) div.overlap a.btn-radio").click()
        
    def input_search_bar(self,str):    
        self.get_element(By.XPATH, "//form[@id='search_form']/input").send_keys(str)
        self.get_element(By.ID, "search_btn_cnt").click()    
        
    def goto_radio(self):
        self.get_element(By.CSS_SELECTOR,"div[id='container']  div.sidebar-nav  li[ng-class=\"{'active' : app.control.highlightRadio}\"] a").click()


    
    def login(self, id, password):
        self.get_element(By.ID, "uid").send_keys(id)
        self.get_element(By.ID, "pwd").send_keys(password)
        self.get_element(By.ID, "login-btn").click()
        


if __name__ == '__main__':

       
    RobotRemoteServer(Web_UI(), host='0.0.0.0')
    exit()
       
    #wu = Web_UI()
    #wu.start("https://www.kkbox.com/play/")
    #wu.login("0932208479", "kkbox")
    #time.sleep(2)
    #wu.input_search_bar(u"清平調")
    #wu.goto_radio()
    #wu.choose_first_radio()  
    #time.sleep(3)
    #wu.unlike()

    
    
    