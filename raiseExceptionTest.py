#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)

try:
    mye(0)
except:
    print 1
else:
    print 2