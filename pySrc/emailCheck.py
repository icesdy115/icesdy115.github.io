#_*_coding:utf-8_*_
import re

#验证邮箱格式
def emailCheck(e):
	mess = ['email input right',
		'email input format error',
		'email length more than 5']
	if len(e) >= 5:
		if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]", e):
			print(mess[0])
			return 1
		else:
			print(mess[1])
			return 2
	else:
		# print('email length more than 5')
		print(mess[2])
		return 3

def emailCheckTest():
	emailList = ("w@w.com", "wwwwww", "", "w")
	for ml in emailList:
		print ("Check email address is :" + ml)
		emailCheck(ml)

#取url扩展名
#===============================================================================
# def strings(url):
# 	lists = ['.php','.html','.asp','.jsp']
# 	for list in lists:
# 		suffix = re.findall(list,url)
# 		if len(suffix)>0:
# 			return list
# url ='http://www.baidu.com/tieba.html'
#
# a = strings(url)
# print a
#
# sum = lambda x,y : x + y
# print sum(1,2)
#===============================================================================

if __name__ == '__main__':
    emailCheckTest()
