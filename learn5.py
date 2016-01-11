# _*_coding:utf8_*_

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 打印html的内容
soup = BeautifulSoup(html)
'''print soup.prettify()

# 将html写入文件
txt = open("html.html", 'w')
txt.write(soup.prettify())
txt.close()'''

# 打印标签
print soup.title
print soup.head
print soup.a
print soup.p

# 打印标签类型
print type(soup.a)

# 打印name
print soup.name
print soup.head.name

# 打印属性
print soup.a.attrs
print soup.p.attrs
print soup.title.attrs
print u"p的class是："
print soup.p['class']
print soup.p.get('class')

# 修改属性
soup.p['class'] = 'newclass'
print soup.p

# 删除属性
del soup.p['class']
print soup.p

# 打印标签内文字
print soup.p.string

# comment
print soup.a
print soup.a.string
print type(soup.a.string)
