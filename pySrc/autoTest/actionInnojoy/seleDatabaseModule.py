# coding:utf-8
'''
@author: wangxu

import sys
sys.path.append('E:\\workspace\\autoTest')
加入这两句是为了成功导入autoTest.loginModule，否则在命令行执行test.py时会报错
'''
import sys
sys.path.append('E:\\workspace\\autoTest')
from elementInit import findElementAPI,countryBaseElement,loginElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def selectDataMoudle(self,dataList):
    br = webdriver.Chrome()
    br.get('http://www.innojoy.com/search/index.html')
    checks = br.find_elements_by_xpath('//*[@type="checkbox"]')
    for i in checks:
        i.click()
    
