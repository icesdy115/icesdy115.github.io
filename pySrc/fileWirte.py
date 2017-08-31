#coding=utf-8
import os


def testLen():
    if os.path.isfile('C:\\Users\\wangxu\\Desktop\\test.txt'):
        testStr = 'name:wangxu,age:32|name:haha,age:31'

        for str2 in testStr.split('|'):
            fName = 'C:\\Users\\wangxu\\Desktop\\test.txt'
            f = open(fName, 'w+')
            f.write(str2)
            f.close()
            for lines in open('C:\\Users\\wangxu\\Desktop\\test.txt'):
                print(lines)
    else:
        print('no file')


#	for lines in open('C:\\Users\\wangxu\\Desktop\\pyStudy\\test.py','r'):
#		print lines

if __name__ == '__main__':
    testLen()
