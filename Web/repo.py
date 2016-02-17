__author__ = 'rzhao'
# coding = utf-8
from selenium import webdriver
import time
from web_function import sys_time
def repo_test(username):
    driver = webdriver.Chrome()
    driver.get("http://beta.repo.pricerunner.com/")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("test")
    driver.find_element_by_name("imgSubmit").submit()

    m=driver.find_element_by_class_name("repoHeader").is_displayed()
    if m:
        print "login successfully"
    else:
        print "failed"
    time.sleep(3)

    driver.find_element_by_link_text("Update your information").click()



    se=driver.find_elements_by_tag_name("textarea")
    for s in se:
        if s.get_attribute("class") =="editValue txt":
            s.clear()
            s.send_keys('test')

    driver.find_element_by_id('editSubmit').submit()
    a =driver.switch_to.alert
    a.accept()
    sscreen=sys_time() + username

    driver.get_screenshot_as_file("F:/screen/Repo/"+sscreen+".png")

    driver.quit()
