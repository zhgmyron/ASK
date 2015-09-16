# -*- coding: utf-8 -*-
import urllib
import urllib2
import string
def test_very():

    postdata=urllib.urlencode({
        'username':'汪小光',
        'password':'why888',
        'continueURI':u'http://www.verycd.com/',
        'fk':'',
        'login_submit':'登录'
    })
    req = urllib2.Request(
        url = 'http://secure.verycd.com/signin',
        data = postdata
    )
    result = urllib2.urlopen(req)
    str= result.read()
    print str
test_very()