#! /usr/bin/env python
 
#coding=utf-8
while True:
    num = int(raw_input())
    nump = 0
    numt = num

    while numt != 0:
        nump = nump * 10 + numt%10
        numt = numt/10

    if num == nump:
        print 'is a palin'
    else:
        print 'no'  