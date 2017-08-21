#coding=utf-8
#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

'''for tag in soup.find_all(True):
    print tag.name'''
'''
print soup.find_all('p','course')
print 
print soup.find_all(id='link1')
print
print soup.find_all(id='link')
print

import re
print soup.find_all(id=re.compile('link'))
'''

'''print soup#.prettify()'''
print soup.find_all(string="Basic Python")
print
import re
print soup.find_all(string=re.compile("python"))



