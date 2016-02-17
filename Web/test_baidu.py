#-*-coding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep


dr = webdriver.Chrome()

dr.get('http://www.qq.com')
today_top_link = dr.find_element_by_css_selector('#todaytop a')
content = today_top_link.text
url = today_top_link.get_attribute('href')
print content
print url

dr.get('http://www.weibo.com')
sleep(2)

dr.find_element_by_css_selector('#v6_pl_content_publishertop .W_input').send_keys(content+url)
dr.find_element_by_css_selector('#v6_pl_content_publishertop .btn_30px').click()
sleep(2)
dr.close()