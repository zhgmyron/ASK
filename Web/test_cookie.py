__author__ = 'rzhao'
#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.smartisan.com/cn/#/")
driver.maximize_window()

time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[2]/h3/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[3]/div[1]/a[1]").click()
time.sleep(2)
div=driver.find_elements_by_class_name("dialog").find_element_by_name("username")
div.send_keys("86466359@qq.com")
driver.find_element_by_name("password").send_keys("Zxcvb1234567")

driver.find_element_by_class_name("btn btn-primary").click()