# coding:utf-8
'''
@author: wangxu

import sys
sys.path.append('E:\\workspace\\autoTest')
加入这两句是为了成功导入autoTest.loginModule，否则在命令行执行test.py时会报错
'''
import time
import sys
sys.path.append('E:\\workspace\\autoTest')
import unittest
from testCase import loginTest, simpSearchTest, tableSearchTest  
# 这里需要导入测试文件
import HTMLTestReportCN

def Suite():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # 将测试用例加入到容器
#    suiteTest.addTest(loginTest.TestCase('loginForEmail'))
#    suiteTest.addTest(loginTest.TestCase('loginForPhone'))
#    suiteTest.addTest(simpSearchTest.TestCase("simpleSearchTest"))
    suiteTest.addTest(tableSearchTest.TestCase("tableSearchTest"))
    return suiteTest


if __name__ == '__main__':
    # 确定生成报告的路径
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filePath = "./report/" + now + '_report.html'
    print (filePath)
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='wangxu'
    )
    runner.run(Suite())
    fp.close()
