#-*-coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.smartisan.com/cn/#/")
driver.maximize_window()

time.sleep(3)
driver.find_element_by_link_text(u'中文').click()
time.sleep(3)
nowhandle =driver.current_window_handle
driver.find_element_by_link_text(u'登录').click()
time.sleep(2)
m=driver.find_element_by_class_name('dialog')
allhandles= driver.window_handles
for handles in allhandles:
    if handles != nowhandle:
        driver.find_element_by_name("password").send_keys("Zxcvb1234567")
        driver.find_element_by_class_name("btn btn-primary").click()

