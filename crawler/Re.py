#coding=utf-8
#!/usr/bin/env python
 
import re
'''
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print match.group(0)
'''
'''
无结果
match2 = re.match(r'[1-9]\d{5}','BIT 100081')
if match2:
    print match2.group(0)  
'''
'''
错误
match2 = re.match(r'[1-9]\d{5}','BIT 100081')
print match2.group(0)
'''
'''
match2 = re.match(r'[1-9]\d{5}','100081 BIT')
if match2:
    print match2.group(0)
'''


'''
ls = re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
print ls
'''


'''
print re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
print re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
'''

'''
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print m.group(0)
'''


print re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TUS100084')
