# _*_ coding:utf-8 _*_
import urllib2
import cookielib
from bs4 import BeautifulSoup

cJar = cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cJar))
urllib2.install_opener(opener)
# 将cookie存入本地
cJar.save("my.cookie.txt")

url = "https://item.taobao.com/item.htm?spm=a219r.lm5704.14.7.LjuGQW&id=45235239258&ns=1&abbucket=15#detail"

# header验证
request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0')
request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
request.add_header('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
request.add_header('Connection', 'Keep-Alive')
request.add_header('Host', 'item.taobao.com')
# 这里是关键，访问淘宝首页，获取cookie进行设置，否则将得到空页面
request.add_header('Cookie', 'cna=b4QuCcgvbFMCAXeHsSuREQMh')

# 检查链接有效性
try:    
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

taobao = response.read()
'''# 打印html内容
print taobao.decode('gbk','ignore').encode('utf-8')'''

# 将html写入文件
soup = BeautifulSoup(taobao)
txt = open("taobao.html", 'w')
txt.write(soup.prettify().encode('utf-8'))
txt.close()