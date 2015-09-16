#-*-coding:utf-8-*-
__author__ = 'rzhao'
import string
import urllib
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
def test_file():
    poem='''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
        use Python1!
    '''

    f=file('poem.txt','a') # open for 'w'riting
    f.write(poem) # write text to file
    f.close() # close the file

    f=file('poem.txt')
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line=f.readline()
        if len(line)==0: # Zero length indicates EOF
            break
        print line,
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file

def test_store():
    #!/usr/bin/env python
    # Filename: pickling.py

    import cPickle as p
    #import pickle as p

    shoplistfile='shoplist.data'
    # the name of the file where we will store the object

    shoplist=['apple','mango','carrot']

    # Write to the file
    f=file(shoplistfile,'w')
    p.dump(shoplist,f) # dump the object to a file
    f.close()

    del shoplist # remove the shoplist

    # Read back from the storage
    f=file(shoplistfile)
    storedlist=p.load(f)
    print storedlist


def test_csdnhead():
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64)"
    headers = { 'User-Agent' : user_agent ,
                'Referer':'http://www.cnbeta.com/articles'
                }
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


    req = urllib2.Request('http://www.baidu.com')

    try: urllib2.urlopen(req)

    except URLError, e:
        print e.reason
def test_d():
    old_url = 'http://rrurl.cn/b1UZuP'
    req = Request(old_url)
    response = urlopen(req)
    print 'Old url :' + old_url
    print 'Real url :' + response.geturl()
    print 'infor'
    print response.info()
def test_se():
    req = Request('http://bbs.csdn.net/callmewhy')

    try:

        response = urlopen(req)

    except URLError, e:

        if hasattr(e, 'code'):

            print 'The server couldn\'t fulfill the request.'

            print 'Error code: ', e.code

        elif hasattr(e, 'reason'):

            print 'We failed to reach a server.'

            print 'Reason: ', e.reason
    else:
        print 'No exception was raised.'
def test_proxy():
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http" : 'http://112.195.81.53:9000'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    a_url = 'http://www.baidu.com/'
    response=opener.open(a_url)
    print response.read()




def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'
        print u'正在下载第' + str(i) + u'个网页，并将其存储为' + sName + '......'
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()



#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
#iPostBegin = 1
#iPostEnd = 10

#bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
#begin_page = int(raw_input(u'请输入开始的页数：\n'))
#end_page = int(raw_input(u'请输入终点的页数：\n'))


#baidu_tieba(bdurl,begin_page,end_page)
def test_very():

    postdata=urllib.urlencode({
        'username':'汪小光',
        'password':'why888',
        'continueURI':'http://www.verycd.com/',
        'fk':'',
        'login_submit':'登录'
    })
    req = urllib2.Request(
        url = 'http://secure.verycd.com/signin',
        data = postdata
    )
    result = urllib2.urlopen(req)
    str= result.read()
    print unicode(str,"utf-8")
test_very()





