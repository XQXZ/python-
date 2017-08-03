
#coding=utf-8
#人名以升序排列
import sys
print sys.path
f = open('/home/chen/桌面/mypython/8.3/name.txt','r')

def is_panlindrom_rec(name):
    if lrn(name) <= 1:
        return True
    else:
        if name[0] != name[-1]:
            return False
        else:
            return is_panlindrom_rec(name[1:-1])

def is_panlindrom(name): 
    low = 0
    high = len(name) - 1

    while low < high:
        if name[low] != name[high]:
            return False
        low += 1
        high -=1
    
    return True


def is_ascending(name):
    p = name[0]

    for c in name:
        if p > c:
            return False
        p = c

    return True




for line in f:
    line = line.strip()
    if is_ascending(line):
        print line
    


f.close()