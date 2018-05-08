# coding:utf-8
'''
@author: wangxu

import sys
sys.path.append('E:\\workspace\\autoTest')
加入这两句是为了成功导入autoTest.loginModule，否则在命令行执行test.py时会报错
'''
import sys
from macpath import split
sys.path.append('E:\\workspace\\autoTest')
from elementInit import baseURL
from actionInnojoy import loginModule, tablesearchModule
from selenium import webdriver
import unittest
from xml.etree import ElementTree as ET

class TestCase(unittest.TestCase):

    def setUp(self):      
#        self.br = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
        URL = baseURL.urlInit()
        self.baseURL = URL[0]

    def tableSearchTest(self):
        u"""表格检索"""
        #读取xml文件中的检索式和预期结果
        per = ET.parse('./testData/tableSearchData.xml')
        p=per.findall('./exp1')
        for oneper in p:
            for child in oneper.getchildren():
                data = child.text.split('|')
 #               self.br = webdriver.Remote("http://192.168.202.121:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
                self.br = webdriver.Chrome()
                self.br.get(self.baseURL)
                self.emailName = 'liyuxin3154@163.com'
                self.passWord = '111111'
                login = loginModule
                login.loginForEmail(self,self.emailName, self.passWord)
                dstPatentNum = data[1]
                search = tablesearchModule.tableSearchAction(self, data[0])
                patentNum = search[0]
                self.assertEqual(patentNum, int(dstPatentNum), '检索结果与预期不一致')

    def tearDown(self):
        self.br.quit()