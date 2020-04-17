"""
@Author  : Laura
@File    : hr_selenium.py
@Time    : 2020/3/16 15:43
"""
# encoding: utf-8  #指定编码格式
from selenium import webdriver #selenium 模块中导入指定部分webdriver（类）
import time #导入时间模块
import unittest

chrome_driver=r"E:\Program Files\python 3.8.2\Lib\site-packages\selenium\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver) # 实例化浏览器，executable_path指定了chromedriver所在的路径,程序运行时就会到该路径下启动chrome浏览器

url_1 = "http://dev.emhes.cn/"
browser.get(url_1) #获取url-1
time.sleep(2) #等待2s

# print("浏览器最大化")
# browser.maximize_window()  #将浏览器最大化显示time.sleep(2)
#
# print("设置浏览器宽480、高800显示")
# browser.set_window_size(480, 800)  #参数数字为像素点
# browser.maximize_window()
#
# print("浏览器后退/前进")
# url_2 = "https://www.runoob.com/python3/python3-module.html"
# browser.get(url_2) #获取url-2
# browser.back() #后退到url_1
# time.sleep(1)
# # browser.forward() #前进到url_2
#
# browser.find_element_by_id("kw").send_keys("selenium") #id定位输入框，并输入值“selenium”
# browser.find_element_by_id("su").click() #id定位搜索按钮，并点击
# time.sleep(3)
# browser.quit() #关闭整个窗口 broswer.close() 关闭当前窗口
# browser.quit() #关闭整个窗口 broswer.close() 关闭当前窗口




