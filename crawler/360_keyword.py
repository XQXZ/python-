#coding=utf-8
#!/usr/bin/env python
import requests
#kv = {'wd':'Python'}
keyword = 'Python'
try:
    kv = {'q':keyword}
    r = requests.get("http://www.so.com/s",params = kv)
    print r.status_code
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print "爬取失败"