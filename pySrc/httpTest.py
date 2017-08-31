#coding=utf-8
import httplib2

h = httplib2.Http()
#h.add_credentials('wangxu@dawei.com','111111')
resp,content = h.request('http://new.innojoy.com:8088/patent/patent.html?docno=CN201510233748.0&trsdb=fmzl')

print content
