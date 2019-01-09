#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:48:03 2018

@author: lisicong
"""

from selenium import webdriver

path = "/Users/admin/Desktop/zhihuSpider/"

def login():
    #设置header伪装
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"')
    tem_path = path+"chromedriver"
    browser = webdriver.Chrome(executable_path=tem_path, chrome_options=options) 
    browser.get("https://www.zhihu.com/signin")
    browser.find_element_by_css_selector("button[class='Button Button--plain']").click()
    input("请扫描二维码进行登录,成功后请按回车")
    '''
    #以下方法可通过账号密码登录，但大概率需要填写二维码
    browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper Input").send_keys(input("请输入账号："))
    browser.find_element_by_css_selector(".SignFlow-password Input").send_keys(input("请输入密码："))
    browser.find_element_by_css_selector(".Button.SignFlow-submitButton").click()
    input("请查看是否需要输入验证码，完成后按下回车")
    '''
    #储存cookie供爬虫使用
    cookies = browser.get_cookies()
    browser.quit()
    #打开文件,储存cookies
    tem_path = path+"cookies.txt"
    out = open(tem_path,'w')
    out.write(str(cookies))
    out.close()
    
if_login=input("是否登录Y/N：")
if if_login == 'Y' or if_login == 'y':
    login()
