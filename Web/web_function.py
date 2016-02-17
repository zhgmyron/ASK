__author__ = 'rzhao'
from selenium import webdriver
import time
import MySQLdb

def mysql_connect(host,user,passwd,db,sql):
    conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    data= cursor.fetchall()
    for row in data:
        ID= row[0]
        firstname = row[1]
        valid= row[5]
        defaultam= row[6]

        print "ID=%s,firstname=%s,valid=%s,defaultam=%s"%(ID,firstname,valid,defaultam)
    conn.close()

def quit(self):
    driver = self.driver
    driver.quit()
def web_login(self,username,passwd,country='UK',adapter='Default'):
    driver = self.driver

    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(passwd)
    if driver.find_element_by_id("country").is_displayed():
        driver.find_element_by_id("country").send_keys(country)
    if driver.find_element_by_name("adapter").is_displayed():
        driver.find_element_by_name("adapter").send_keys(adapter)
    driver.find_element_by_name("imgSubmit").submit()
def sys_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

