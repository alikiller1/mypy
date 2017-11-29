#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");

printinfo(50, "miki");

total=0;
def calculate(a,b):
    total=a+b;
    print total;
    return total;
print calculate(1,2);
total=calculate(1,2);
print total;
