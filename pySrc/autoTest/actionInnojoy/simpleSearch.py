# coding=utf-8
'''
@author: wangxu
'''
from elementInit import simpleSearchElement,findElementAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def simpleSearchAction(self, expression):
    message = 'python返回一个值不能全部读取'
    br = self.br
    express = self.expression
    element = simpleSearchElement.elementInit()
    we = findElementAPI
    # 判断页面元素是否加载完
    wait = WebDriverWait(br, 10)
    wait.until(EC.presence_of_all_elements_located, "页面元素未加载完全")
    try:
        # menu = we.findXpath(br,'/html/body/div[1]/div/ul[1]/li[2]/a')
        # menu.findXpath('/html/body/div[1]/div/ul[1]/li[2]/div/a[1]').click()
        br.implicitly_wait(3)
        we.findXpath(br,element[0]).send_keys(express)
        we.findXpath(br,element[1]).click()
        br.implicitly_wait(25)
        patentNum = int(self.br.find_element_by_xpath(
                        '//*[@id="numcollect"]').text)
    except:
        message = ('检索失败')
    return patentNum,message
