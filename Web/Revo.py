__author__ = 'rzhao'
#coding=utf-8
import sys
from selenium import webdriver
import unittest,time
import f_core1
class Revo(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()
    def test_login(url,username,password):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
