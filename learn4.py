# _*_coding:utf8_*_

import urllib
import urllib2
import cookielib

filename = 'zhihucookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'username':'pickle.ahcai@163.com','password':'318318'})
loginurl = 'http://www.zhihu.com/?next=%2Fsettings%2Fprofile#signin'
result = opener.open(loginurl, postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
settingurl = 'https://www.zhihu.com/settings/profile'
result = opener.open(settingurl)
print result.read()