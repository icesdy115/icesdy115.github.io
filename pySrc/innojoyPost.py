#!/usr/bin/env python
#_*_coding:utf-8_*_ 
import httplib2
import urllib2
import urllib
import string
#httplib2.debuglevel = 1

paramsSearch = urllib.urlencode({
    #"requestModule":"PatentSearch",
	"Action":"Search",
	"AddOnes":"",
	"DBOnly":0,
	"Database":"wgzl,syxx,fmzl",
	"DelOnes":"",
	"GUID":"",
	"Page":"1",
	"PageSize":"10",
	"Query":"car",
	"RemoveOnes":"",
	"SmartSearch":"",
	"Sortby":"-PD,PNM",
	"TreeQuery":"",
	"TrsField":"",
	"Verification":"",
	"userId":"6453A022-C9D0-4EA5-B5C0-660260255010"
})  
headers = {
	"Accept":"application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Cache-Control":"no-cache",
	"Connection":"keep-alive",
	#"Content-Length":373,
	"Content-Type":"application/json; charset=UTF-8",
	"Cookie":"Hm_lvt_9ebd156ac7d2304301a6a7f0434e8257=1449543761; Hm_lpvt_9ebd156ac7d2304301a6a7f0434e8257=1449544675",
	"Host":"new.innojoy.com:8088",
	"Pragma":"no-cache",
	"Referer":"http://new.innojoy.com:8088/searchresult/default.html",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
	"X-Requested-With":"XMLHttpRequest"
	}  

#reqLogin = urllib2.Request("http://new.innojoy.com:8088/searchresult/default.html",paramsLogin,headers)
req = urllib2.Request("http://new.innojoy.com:8088/searchresult/default.html",paramsSearch,headers)
#reqLogin = urllib2.urlopen(reqLogin)
request = urllib2.urlopen(req)

thePage = request.read()

print len(thePage)
fName = 'test1.html'
f = open(fName,'w+')
f.write(thePage)
f.close