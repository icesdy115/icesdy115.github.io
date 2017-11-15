#_*_coding:utf-8_*_
'''
获取文件夹中的文件名，循环读取文件内容
使用正则表达式，查找是否存在相应的字段
输出匹配字段数
'''
import os
import re

def souFileRead():
    openDir = 'C:\\Users\\wangxu\\Desktop\\before'
    reFileName = 'C:\\Users\\wangxu\\Desktop\\reMatch.txt'
    reExp = open(reFileName,'r')
    resultFile = 'C:\\Users\\wangxu\\Desktop\\result.txt'
    resultF = open(resultFile,'w')
    fileSum = 0     # 初始化文件字段数
    fileKwSum = 0   # 初始化查询结果总数
    '''循环获取正则表达式内容'''
    for reList in reExp.readlines():
        regLists = reList.split(';')
        regLen = len(regLists)
        for regs in regLists:
            resultF.writelines('正则表达式: %s \n' % regs)
            '''循环获取文件名'''
            for sfileName in os.listdir(openDir):    # 循环获取单个文件名
                fileName = os.path.join(openDir, sfileName)     # 使用os.path.join拼接文件完整路径用于读取文件
                srcF = open(fileName, 'r')
                sum = 0     # 初始化单个文件统计数量
                keyWordCount = 0  # 初始化单个文件关键词统计数量

                for lists in srcF.readlines():
                    keyWords = lists.split(';')     # 对打开的trs文件进行切片处理

                    for kw in keyWords:
                        sum = sum + 1
                        if re.search(regs, kw):
                            keyWordCount = keyWordCount + 1
                fileKwSum = fileKwSum + keyWordCount
                fileSum = fileSum + sum
                srcF.close()
                #resultF.writelines('    file name:%s, file words sum:%s \n' % (sfileName, sum))
                resultF.writelines('目标文件：%s, 正则表达式匹配记录数:%s \n' % (sfileName, keyWordCount))

        fileSum = fileSum / regLen
        resultF.writelines('文件总记录数:%d \n' % fileSum)
        resultF.writelines('正则表达式检索到的记录数:%d \n' % fileKwSum)

    print ('Success!')

    reExp.close()
    resultF.close()

if __name__ == '__main__':
    souFileRead()
