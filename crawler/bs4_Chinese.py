#coding=utf-8
#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup("<p>中文</p>","html.parser")

print soup.p.string
print soup.p.prettify()