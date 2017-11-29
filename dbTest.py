#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="testdb",charset='utf8');
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * from student")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

for item in data:
    print item


# 关闭数据库连接
db.close()