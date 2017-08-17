#coding=utf-8
#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print soup.title

#获取标签及内容
tag = soup.a
print tag

#获取标签名
print soup.a.name
print soup.a.parent.name
print soup.a.parent.parent.name

#获取标签属性
tag = soup.a
print tag.attrs

#获取class属性值
print tag.attrs['class']

print tag.attrs['href']

print type(tag.attrs)
print type(tag)

print soup.a.string
print soup.p.string
print type(soup.p.string)


# #
newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
print newsoup.b.string
print type(newsoup.b.string)
print newsoup.p.string
print type(newsoup.p.string)





