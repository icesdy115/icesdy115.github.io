#_*_coding:utf-8_*_
import os

def fileList():
    openDir = 'C:\\Users\\Administrator\\Desktop\\yinzheng\\before'
    lfile=os.listdir(openDir)
    
    for sfileName in lfile:
        print (sfileName)

if __name__ == '__main__':
    fileList()