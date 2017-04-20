#_*_coding:utf-8_*_
#! /usr/bin/env python

'''
获取文件夹中的文件名，循环读取文件内容
使用正则表达式，在处理后的文件中检索，查找是否存在相应的字段
'''
import os
import re
from innojoyYinZheng import reFindStr
from _ast import keyword
# from pandas import Series,DataFrame
# import pandas as pd

def souFileRead():
    openDir = 'C:\\Users\\Administrator\\Desktop\\yinzheng\\before'

    #循环获取单个文件名
    for sfileName in os.listdir(openDir):
        '''
                    使用os.path.join()连接目录路径和文件名，构成文件完整路径
                    首层for循环只获取了文件名，直接open没有完整路径，找不到文件
        '''
        fileName = os.path.join(openDir,sfileName)
        srcF = open(fileName,'r')
        sum = 0 #初始化单个文件统计数量
        keyWordCount = 0 #初始化单个文件关键词统计数量
        for lists in srcF.readlines():
            keyWords = lists.split(';')
            for kw in keyWords:
                sum = sum + 1
                if re.search('\\s[a-zA-Z]\\d{0,1}\\s(.+)',lists):
                    keyWordCount = keyWordCount + 1
        print 'file name: %s, file words sum:' % sfileName,sum
        print 'file name: %s, file keywords CN count:' % sfileName,keyWordCount

if __name__ == '__main__':
    souFileRead()
