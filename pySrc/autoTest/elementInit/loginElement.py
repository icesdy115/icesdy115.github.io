# coding=utf-8
'''
@author: wangxu
登录页面元素初始化
'''


def elementInit():
    switchEmailInput = '//*[@id="emailBtn"]'
    switchToFrame = '_userlogin'
    emailInput = '//*[@used="1"]'
    phoneInput = '//*[@id="idPhone"]'
    passwdInput = '//*[@id="idPassword"]'
    buttonClick = '//*[@id="quote_sign"]'
    loginLink = '//*[@id="account_login"]'
    loginAfterUser = '//*[@id="account_user"]'
    alertMessage = '//*[@id="dialog-message-span"]'

    return switchEmailInput, switchToFrame, phoneInput, emailInput, passwdInput, buttonClick, loginLink, loginAfterUser, alertMessage
