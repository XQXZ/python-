#coding=utf-8
#!/usr/bin/env python
import requests
r = requests.get("http://www.baidu.com")
print r.status_code
#print r.text
print r.encoding 
print r.apparent_encoding
