__author__ = 'rzhao'
import web_function
from selenium import webdriver
import time
#login
driver = webdriver.Chrome()
driver.get("http://beta.revo.pricerunner.com/")

driver.maximize_window()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("beta_test@email.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("test")
driver.find_element_by_name("imgSubmit").submit()
#menu
driver.find_element_by_link_text("Merchant Maintenance").click()
driver.find_element_by_xpath("//*[@id='FF4']/ul/li[10]/a/span").click()
driver.find_element_by_link_text("Validate Retailer Info").click()
#select country
m=driver.find_element_by_class_name("countryList")
m.find_element_by_xpath("//option[@value='GBR']").click()

p= driver.find_element_by_id("pageSize-obsolete")
p.find_element_by_xpath("//option[@value=25]").click()

print driver.find_element_by_xpath('//*[@id="list-table"]/tbody/tr[9]/td[2]').text
print driver.find_element_by_xpath('//*[@id="list-table"]/tbody/tr[2]/td[3]').text
print driver.find_element_by_xpath('//*[@id="list-table"]/tbody/tr[4]/td[3]').text
rowCount = len(driver.find_elements_by_xpath('//*[@id="list-table"]/tbody/tr'))


for i in range(2,rowCount):
    print driver.find_element_by_xpath('//*[@id="list-table"]/tbody/tr[%s]/td[3]'%(i)).text


