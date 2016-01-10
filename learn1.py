# _*_coding:utf8_*_

import urllib
import urllib2

values = {"username":"picklecai", "password":"ahcai@318"}
data = urllib.urlencode(values)
url = "http://login.taobao.com"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl
