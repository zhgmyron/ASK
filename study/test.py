__author__ = 'rzhao'
#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name("tj_trnews").click()
time.sleep(5)
driver.find_element_by_id("passLog")

div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
div.send_keys("username")

driver.find_element_by_name("password").send_keys("password")

driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
driver.quit()