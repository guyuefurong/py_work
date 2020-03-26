"""
@Author  : Laura
@File    : zt_system_test.py
@Time    : 2020/3/26 10:26
"""
from zt_selenium_test import TestZt
from selenium import webdriver
import unittest
import time

class TestSystem(unittest.TestCase):

    def test_system_gonggao_select(self):
        '''
        根据名称查询公告,如公告‘危险行为通告’
        '''
        # 进入系统管理
        driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        # 进入公告管理
        driver.find_element_by_link_text("公告管理").click()
        # 输入公告‘危险行为通告’并查询
        driver.find_element_by_id('title').click()
        driver.find_element_by_id('title').send_keys('危险行为通告')
        driver.find_element_by_xpath('//button[1]').click()
        time.sleep(5)
        # 断言
        res = driver.find_element_by_xpath('//table/tbody/tr/td[2]/span').text
        print(res)
        self.assertEqual('危险行为通告', res)


    def test_system_gonggao_add(self):
        '''
        公告管理新增公告
        '''
        self.setUp()
        # 进入系统管理
        driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        # 进入公告管理
        driver.find_element_by_link_text("公告管理").click()
        # 点击新增并输入内容保存
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="Title"]').click()  # 点击公告标题输入框
        driver.find_element_by_xpath('//*[@id="Title"]').send_keys("2020测试删除1")  # 输入名称
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="DisplayDate"]/div/i').click()  # 点击日历
        driver.find_element_by_xpath("//a[@title='下个月 (翻页下键)']").click()  # 日历翻页
        time.sleep(2)
        driver.find_element_by_xpath("//td[@title='2020年4月1日']").click()  # 输入时间
        doc = "这是通告内容"
        driver.find_element_by_id('Contents').send_keys(doc)  # 输入通告内容
        driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
        driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click()  # 点击保存，注意span不可点击
        time.sleep(5)
        # 断言
        driver.refresh()  # 刷新
        res = driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
        self.assertEqual('2020测试删除', res)


    def test_system_gonggao_update(self):
        '''
        修改已存在的指定公告
        修改公告序号:1
        标题修改为 :20200323 公告
        现实日期修改为:2020 03 30
        公告内容修改为：天气黄色警告，请小心驾驶
        '''
        # 进入系统管理
        driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        #进入公告管理
        driver.find_element_by_link_text("公告管理").click()
        #点击修改
        driver.find_element_by_xpath('//thead/following-sibling::tbody/tr[1]/td[7]/a[1]').click()
        driver.find_element_by_id("Title").clear()
        driver.find_element_by_id("Title").send_keys("20200323 公告") #修改公告标题
        time.sleep(2)
        driver.find_element_by_xpath('//*[@placeholder="请选择日期"]').click() #点击日历输入框
        time.sleep(2)
        driver.find_element_by_xpath("//td[@title='2020年3月30日']").click() #输入时间
        driver.find_element_by_id('Contents').clear()
        doc = "天气黄色警告，请小心驾驶"
        driver.find_element_by_id('Contents').send_keys(doc) #输入通告内容
        driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
        driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click() #点击保存，注意span不可点击
        #断言
        driver.refresh() #刷新
        res = driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
        self.assertEqual('2020安全管理通告', res)

    def test_system_gonggao_delete(self):
        '''
        按照名称删除已存在的公告
        根据名称查询公告,如“2020测试删除”
        删除已查询的公告
        :return:
        '''
        # 进入系统管理
        driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        # 进入公告管理
        driver.find_element_by_link_text("公告管理").click()
        # 查询公告
        driver.find_element_by_id('title').click()
        driver.find_element_by_id('title').send_keys('2020测试删除')
        driver.find_element_by_xpath('//button[1]').click()
        # 判断
        time.sleep(5)
        show_date = driver.find_element_by_xpath('//tbody/tr[1]/td[5]').text
        show_text = driver.find_element_by_xpath('//tbody/tr[1]/td[6]').text
        print(show_text)
        print(show_date)
        # 删除查询结果第一项
        time.sleep(2)
        driver.find_element_by_xpath('//tbody/tr[1]//a[2]').click()
        # 点击确定
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='删除公告']/parent::div/following-sibling::div/button[2]").click()
        # 断言（不存在与删除记录名称及日期/内容相同的记录
        driver.refresh()  # 刷新浏览器
        driver.find_element_by_id('title').click()
        driver.find_element_by_id('title').send_keys('2020测试删除')
        driver.find_element_by_xpath('//button[1]').click()
        # 判断元素是否存在
        show = self.isElementExist("//p")
        if show == True:  # 查询无数据
            res = "暂无数据，删除成功"
            print(res)
        else:  # 查询有数据，判断第一条是否相符
            self.assertNotEqual(driver.find_element_by_xpath('//tbody/tr[1]/td[2]/span').get_attribute("title"),
                                "2021测试删除")  # 公告名称