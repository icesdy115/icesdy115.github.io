#coding=utf-8
'''
Created on 2018.3.14

@author: wangxu

selenium 元素定位二次封装
'''
from selenium import webdriver

def findID(driver,idName):
    f = driver.find_element_by_id(idName)
    return f

def findName(driver,name):
    f = driver.find_element_by_name(name)
    return f

def findClassName(driver,name):
    f = driver.find_element_by_class_name(name)
    return f

def findXpath(driver,xpath):
    f = driver.find_element_by_xpath(xpath)
    return f

def findCss(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f

def switchFrame(driver,iFrame):
    f = driver.switch_to_frame(iFrame)
    return f