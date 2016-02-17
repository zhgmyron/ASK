#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("http://www.pricerunner.co.uk/")
driver.maximize_window()
menu=driver.find_element_by_class_name('menu-button')
ActionChains(driver).move_to_element(menu)
target=driver.find_element_by_class_name('login google-analytic-action')

ActionChains(driver).click(target)
driver.find_element_by_id("user").send_keys("Ron.Zhao@askmedia.com")
