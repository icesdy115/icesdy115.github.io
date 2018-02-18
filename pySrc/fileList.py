# _*_coding:utf-8_*_
import os

def fileList():
    filePath = "/home/wangxu"
    fileList = os.listdir(filePath)

    for fl in fileList:
        subfl = fl[0]
        if subfl == '.':
           pass 
        else:
            print (fl)

if __name__ == '__main__':
    fileList()
    