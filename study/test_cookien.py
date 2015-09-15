__author__ = 'rzhao'
#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.12306.cn/opn/login/init")

time.sleep(2)
driver.find_element_by_id("username").send_keys("zhgmyron")
driver.find_element_by_id("userDTO.password").send_keys("Zxcvb1234567")
cookie1= driver.get_cookies()
print cookie1
driver.delete_cookie("lzstat_uv")
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])
