# python爬虫学习  

入门资料：[Python爬虫实战（4）：抓取淘宝MM照片 - Python - 伯乐在线](http://python.jobbole.com/81359/)

## 单网页内容  

代码：  

    # _*_ coding:utf-8 _*_
	
	import urllib
	import urllib2
	from bs4 import BeautifulSoup
	
	url = "http://www.qiushibaike.com/hot/page/1"
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

错误提示：  

![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-12/31276063.jpg)  

这句话：`httplib.badstatusline ''`  
Google到：[python - httplib.BadStatusLine: '' - Stack Overflow](http://stackoverflow.com/questions/27619258/httplib-badstatusline)  
> Based on Python Doc, httplib.BadStatusLine raised if a server responds with a HTTP status code that we don’t understand.  

服务器返回一个不认识的状态码。

说是headers验证的问题。