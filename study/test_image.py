#-*-coding:utf-8-*-
import urllib2
import re
import os
URL='http://image.baidu.com/channel/wallpaper'
read=urllib2.urlopen(URL).read()

pat =  re.compile(r'src="http://.+.js">')
urls=re.findall(pat,read)
for i in urls:
    url= i.replace('src="','').replace('">','')
    try:
        iread=urllib2.urlopen(url).read()
        name=os.path.basename(url)
        with open(name,'wb') as jsname:
            jsname.write(iread)
    except:
        print url,"url error"