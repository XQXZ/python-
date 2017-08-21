#coding=utf-8
#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
'''
print soup.head
print
print soup.head.contents
print
print soup.body.contents
print
print len(soup.body.contents)
print
print soup.body.contents[1]



print soup.title.parent
print 
print soup.html.parent

print 
print 
print
print soup.a.parent

'''
'''#标签树的上行遍历
soup = BeautifulSoup(demo,"html.parser")
for parent in soup.a.parents:
    if parent is None:
        print parent
    else:
        print parent.name
'''
print soup.a.next_sibling
print soup.a
print soup.a.parent
print soup.a.previous_sibling
print soup.a.next_sibling.next_sibling



