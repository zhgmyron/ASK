__author__ = 'rzhao'
from selenium import webdriver
import time
from ..Web import test_cookie
def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys("username")
    driver.find_element_by_id("user_pwd").clear()
    driver.find_element_by_id("user_pwd").send_keys("123456")
    driver.find_element_by_id("dl_an_submit").click()
    time.sleep(3)