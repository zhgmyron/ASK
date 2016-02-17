__author__ = 'rzhao'
#coding=utf-8
import sys

from selenium import webdriver
import unittest,time
from web_function import web_login
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://dev.revo.pricerunner.com/"
        self.username='dev_test@email.com'
        self.password='test'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_weblogin(self,country='UK',adapter='Default'):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(self.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)
        if driver.find_element_by_id("country").is_displayed():
            driver.find_element_by_id("country").send_keys(country)
        if driver.find_element_by_name("adapter").is_displayed():
            driver.find_element_by_name("adapter").send_keys(adapter)
        driver.find_element_by_name("imgSubmit").submit()
    def test_revooperate(self):
        driver = self.driver
        driver.find_element_by_link_text("Merchant Maintenance")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()