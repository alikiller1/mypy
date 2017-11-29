#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("inputTest.py", "r+")
lines = fo.readlines();
for line in lines:
    print line