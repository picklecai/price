# _*_ coding:utf-8 _*_

import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://www.qiushibaike.com/hot/page/1"

# header验证
user_agent  = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}

request = urllib2.Request(url)
response = urllib2.urlopen(request)
qiushi = response.read()
soup = BeautifulSoup(qiushi)

# 将html写入文件
txt = open("qiushi.html", 'w')
txt.write(soup.prettify())
txt.close()

# 抓取最新段子
txt1 = open("duanzi.txt", 'a')
txt1.write(soup.div.string) 
txt1.close()