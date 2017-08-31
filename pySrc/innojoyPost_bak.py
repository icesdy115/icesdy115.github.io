 # -*- coding: utf-8 -*-
import httplib2
import urllib
import string
#httplib2.debuglevel = 1
params = urllib.urlencode({
	"Action":"Search",
	"AddOnes":"",
	"DBOnly":0,
	"Database":"wgzl,syxx,fmzl",
	"DelOnes":"",
	"GUID":"",
	"Page":"1",
	"PageSize":"50",
	"Query":"car",
	"RemoveOnes":"",
	"SmartSearch":"",
	"Sortby":"-PD,PNM",
	"TreeQuery":"",
	"TrsField":"",
	#"Verification":"e40db9d0076b451fba5371b714bfd02a:g3id",
	"requestModule":"PatentSearch",
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
	"Cookie":"Hm_lvt_9ebd156ac7d2304301a6a7f0434e8257=1449205876,1449449085,1449469868,1449539090;Hm_lpvt_9ebd156ac7d2304301a6a7f0434e8257=1449539241",
	"Host":"new.innojoy.com:8088",
	"Pragma":"no-cache",
	"Referer":"http://new.innojoy.com:8088/searchresult/default.html",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
	"X-Requested-With":"XMLHttpRequest"
	}

conn, content = httplib2.Http().request("http://new.innojoy.com:8088/searchresult/default.html","POST", params, headers)

sName = string.zfill(0,5) + '.html' #自动填充成六位的文件名
f = open(sName,'w+')
f.write(content)
f.close()

#print (conn.status,conn.reason)
#print content

#print (response.status,response.reason)
