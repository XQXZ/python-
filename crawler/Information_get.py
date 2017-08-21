#coding=utf-8
#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

for link in soup.find_all('a'):
    print link.get('href')

print soup.find_all('a')
print soup.find_all(['a','b'])
