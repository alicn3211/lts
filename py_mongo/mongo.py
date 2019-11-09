#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:14:14 2019

@author: ali
"""

from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn.stu
myset = db.class4

#myset.insert({'name':'chendm','king':'kangxi'})
#myset.insert_many([{'name':'tanggq','king':'yongz'},{'name':'chenjianbin','king':'yongzhen'},
#                  {'name':'zhengshaoqiu','king':'qianlong'}])

#myset.save({'_id':1,'name':'wuqilong','king':'siye'})
#print(dir(myset))

cursor = myset.find({},{'_id':0})
print(cursor)
for i in cursor:
    print(i['name'],'--------',i['king'])
conn.close()