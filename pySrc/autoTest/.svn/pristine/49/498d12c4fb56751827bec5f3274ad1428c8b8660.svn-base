# coding=utf-8
'''
Created on 20180212

@author: wangxu
'''

from elementInit import tableSearchElement,findElementAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tableSearchAction(self,expression):
    br = self.br
    express = self.expression
    element = tableSearchElement.elementInit()
    we = findElementAPI
    #判断页面元素是否加载完
    wait = WebDriverWait(br, 10)
    wait.until(EC.presence_of_all_elements_located, "页面元素未加载完全")
    print(express)
    try:
        br.implicitly_wait(3)
        for inputXpath in range(0,32):
            exp = express.text.split(',')
            for i in range(0,32):
                we.findXpath(br,element[inputXpath]).send_keys(exp[i])
        we.findXpath(br,element[33]).click()
    except:
        print('检索失败')

