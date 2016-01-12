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

作者说是headers验证的问题。  

加上验证：  

    # header验证
	user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}  

仍然以上错误。后来才发现，添加这段代码后，没有更改Request的参数：  

    request = urllib2.Request(url, headers=headers)  

下一个错误提示是：  

    txt.write(soup.prettify())
 ‘ascii’ codec can’t encode characters in 421-428  

参照这里：http://blog.csdn.net/panyanyany/article/details/17251225，改成：  

    txt.write(soup.prettify().encode('utf-8'))
解决。

下一个错误提示是：
    txt1.write(soup.div.string)  
~~"Nonetype" object has no attribute 'string'~~   
TypeError: expected a character buffer object  

打印soup.div.string类型，原来是“NoneType”。于是给它加了个`str()`  

结果：html确实写进去了。但是`soup.div.string`用错了，导致txt文件中存的是一个none。