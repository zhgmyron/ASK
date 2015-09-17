#-*-coding:utf-8-*-
__author__ = 'rzhao'

import urllib
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
def test_csdnhead():
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64)"
    headers = { 'User-Agent' : user_agent }
    values = {}
    values['username'] = "guangking1987@163.com"
    values['password']="Zxcvb1234567"
    data = urllib.urlencode(values)
    url = "https://passport.csdn.net/account/login"
    request = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(request)
    str= response.read()
    print unicode(str,"utf-8")
def test_csdnpost():

    values = {}
    values['username'] = "guangking1987@163.com"
    values['password']="Zxcvb1234567"
    data = urllib.urlencode(values)
    url = "http://passport.csdn.net/account/login"
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    str= response.read()
    print unicode(str,"utf-8")
def test_get():


    values={}
    values['username'] = "guangking1987@163.com"
    values['password']="Zxcvb1234567"


    url_values = urllib.urlencode(values)
    print url_values

    #name=Somebody+Here&language=Python&location=Northampton
    url = 'http://passport.csdn.net/account/login'
    full_url = url + '?' + url_values
    print full_url
    data = urllib2.urlopen(full_url)
    str= data.read()
    print unicode(str,"utf-8")
def test_e():


    req = urllib2.Request('http://www.baibai.com')

    try: urllib2.urlopen(req)

    except URLError, e:
        print e.reason
def test_d():
    old_url = 'http://rrurl.cn/b1UZuP'
    req = Request(old_url)
    response = urlopen(req)
    print 'Old url :' + old_url
    print 'Real url :' + response.geturl()
test_d()
