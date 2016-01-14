#coding=utf-8
import urllib2
import cookielib
from urllib2 import urlopen, Request

cJar = cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cJar))
urllib2.install_opener(opener)

testURL='http://item.taobao.com/item.htm?id=20236130559'
req = Request(testURL)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
req.add_header('Connection', 'Keep-Alive')
req.add_header('Host', 'item.taobao.com')
# 这里是关键，访问淘宝首页，获取cookie进行设置，否则将得到空页面
req.add_header('Cookie', 'cna=b4QuCcgvbFMCAXeHsSuREQMh')
h = urlopen(req)
res = h.read()
print res.decode('gbk','ignore').encode('utf-8')
cJar.save("my.cookie.txt")