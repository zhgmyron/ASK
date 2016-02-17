__author__ = 'zhaor'
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/login/init")

driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
driver.delete_cookie("key-aaaaaaa")
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])



driver.delete_all_cookies()
driver.close();