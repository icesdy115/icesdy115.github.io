# coding:utf-8
'''
@author: wangxu

import sys
sys.path.append('E:\\workspace\\autoTest')
'''
import sys
from macpath import split
sys.path.append('E:\\workspace\\autoTest')
from actionInnojoy import loginModule
from selenium import webdriver
from elementInit import baseURL
import unittest
from xml.etree import ElementTree as ET

class TestCase(unittest.TestCase):

    def setUp(self):
         self.br = webdriver.Chrome()
#        self.br = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        URL = baseURL.urlInit()
        self.baseURL = URL[0]

    def loginForEmail(self):
        u"""使用邮箱登录"""
        per=ET.parse('E:\\workspace\\autoTest\\testData\\userTestData.xml')
        p=per.findall('./email')       
        for oneper in p:
            for child in oneper.getchildren():
                data = child.text.split(',')
                self.br = webdriver.Chrome()
                self.br.get(self.baseURL)
                self.emailName = data[0]
                self.passWord = data[1] 
                #获取执行后的返回值
                login = loginModule.loginForEmail(self, self.emailName, self.passWord)
                #获取预期值和结果
                srcName = login[0]
                destStr = data[2]
                self.assertEqual(srcName, destStr,'提示信息错误！预期值与实际值不符')


    def loginForPhone(self):
        u"""使用手机号登录"""
        per = ET.parse('E:\\workspace\\autoTest\\testData\\userTestData.xml')
        p = per.findall('./phone')
        for oneper in p:
            for child in oneper.getchildren():
                data = child.test.split(',')
                self.br.get(self.baseURL)
                self.phoneName = data[0]
                self.passWord = data[1]
                #获取执行后的返回值
                login = loginModule.loginForPhone(self, self.phoneName, self.passWord)
                srcName = login[0]
                destName = data[2]
                self.assertEqual(srcName, destName, '提示信息错误！预期值与实际值不符')

    def tearDown(self):
        self.br.quit()