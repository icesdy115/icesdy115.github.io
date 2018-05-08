# coding=utf-8
'''
Created on 2018年2月12日

@author: wangxu
'''

from elementInit import loginElement,findElementAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def loginForEmail(self, emailName, passWord):
    br = self.br
    name = self.emailName
    password = self.passWord
    message1 = 'python返回一个值不能全部读取'
    element = loginElement.elementInit()
    we = findElementAPI
    # 判断页面元素是否加载完
    wait = WebDriverWait(br, 10)
    wait.until(EC.presence_of_all_elements_located, "页面元素未加载完全")
    try:
        we.switchFrame(br, element[1])
        we.findXpath(br,element[0]).click()
        we.findXpath(br,element[3]).send_keys(name)
        we.findXpath(br,element[4]).send_keys(password)
        we.findXpath(br,element[5]).click()
    except:
        srcName = ('登录操作失败，请假查环境是否正常')
        return srcName
    # 判断登录是否弹出框
    br.implicitly_wait(10)
    try:
        srcName = we.findXpath(br,element[7]).text
        lenElement = 1
    except:
        lenElement = 0
    if lenElement == 0:
        try:
            srcName = we.findXpath(br,element[8]).text
        except:
            message1 = '未找到元素'
            return message1
    return srcName, message1

def loginForPhone(self, phoneName, passWord):
    br = self.br
    name = self.phoneName
    password = self.passWord
    message1 = 'python返回一个值不能全部读取'
    element = loginElement.elementInit()
    we = findElementAPI
    # 判断页面元素是否加载完
    wait = WebDriverWait(br, 10)
    wait.until(EC.presence_of_all_elements_located, "页面元素未加载完全")
    try:
        we.switchFrame(br,element[1])
        we.findXpath(br,element[2]).send_keys(name)
        we.findXpath(br,element[4]).send_keys(password)
        we.findXpath(br,element[5]).click()
    except:
        srcName = ('登录操作失败，请检查环境是否正常')
        return srcName
    # 判断登录是否弹出框
    br.implicitly_wait(3)
    try:
        srcName = we.findXpath(br,element[7]).text
        lenElement = 1
    except:
        lenElement = 0
    if lenElement == 0:
        try:
            srcName = we.findXpath(br,element[8]).text
        except:
            message1 = '未找到元素'
            return message1

    return srcName, message1
