#_*_coding:utf-8_*_
'''
������ʽ������Ӧ���ֶ�
'''
import re

def reFindStr(dstFileName):
    dstF = open(dstFileName,'r')
    count = 0
    
    for s in dstF.readlines():
        li = s.split('<REC>')
        for lists in li:
            count = count + 1
            lists = lists.split(';')
            print lists
    print count

if __name__ == '__main__':
    reFindStr()