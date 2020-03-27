"""
@Author  : Laura
@File    : zt_system_test.py
@Time    : 2020/3/26 10:26
"""
from Practices.hr_selenium0318.ZT_TestExample.zt_test.zt_selenium_test import TestZt
from selenium import webdriver
import unittest
import time


class TestGongGao(TestZt):

    def setUp(self):
        super().setUp()  #超继承，在setup函数上增添打开系统管理-用户管理
        # 进入系统管理
        self.driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        # 进入公告管理
        self.driver.find_element_by_link_text("公告管理").click()

    def test_system_gonggao_select(self):
        '''
        根据名称查询公告,如公告‘危险行为通告’
        '''
        # 输入公告‘危险行为通告’并查询
        self.driver.find_element_by_id('title').click()
        self.driver.find_element_by_id('title').send_keys('危险行为通告')
        self.driver.find_element_by_xpath('//button[1]').click()
        time.sleep(5)
        # 断言
        res = self.driver.find_element_by_xpath('//table/tbody/tr/td[2]/span').text
        print(res)
        self.assertEqual('危险行为通告', res)


    def test_system_gonggao_add(self):
        '''
        公告管理新增公告
        '''
        # 点击新增并输入内容保存
        self.driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="Title"]').click()  # 点击公告标题输入框
        self.driver.find_element_by_xpath('//*[@id="Title"]').send_keys("2020测试删除1")  # 输入名称
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="DisplayDate"]/div/i').click()  # 点击日历
        self.driver.find_element_by_xpath("//a[@title='下个月 (翻页下键)']").click()  # 日历翻页
        time.sleep(2)
        self.driver.find_element_by_xpath("//td[@title='2020年4月1日']").click()  # 输入时间
        doc = "这是通告内容"
        self.driver.find_element_by_id('Contents').send_keys(doc)  # 输入通告内容
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click()  # 点击保存，注意span不可点击
        time.sleep(5)
        # 断言
        self.driver.refresh()  # 刷新
        res = self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
        self.assertEqual('2020测试删除', res)


    def test_system_gonggao_update(self):
        '''
        修改已存在的指定公告
        修改公告序号:1
        标题修改为 :20200323 公告
        现实日期修改为:2020 03 30
        公告内容修改为：天气黄色警告，请小心驾驶
        '''
        #点击修改
        self.driver.find_element_by_xpath('//thead/following-sibling::tbody/tr[1]/td[7]/a[1]').click()
        self.driver.find_element_by_id("Title").clear()
        self.driver.find_element_by_id("Title").send_keys("20200323 公告") #修改公告标题
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@placeholder="请选择日期"]').click() #点击日历输入框
        time.sleep(2)
        self.driver.find_element_by_xpath("//td[@title='2020年3月30日']").click() #输入时间
        self.driver.find_element_by_id('Contents').clear()
        doc = "天气黄色警告，请小心驾驶"
        self.driver.find_element_by_id('Contents').send_keys(doc) #输入通告内容
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click() #点击保存，注意span不可点击
        #断言
        self.driver.refresh() #刷新
        res = self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
        self.assertEqual('2020安全管理通告', res)

    def test_system_gonggao_delete(self):
        '''
        按照名称删除已存在的公告
        根据名称查询公告,如“2020测试删除”
        删除已查询的公告
        :return:
        '''
        # 查询公告
        self.driver.find_element_by_id('title').click()
        self.driver.find_element_by_id('title').send_keys('2020测试删除')
        self.driver.find_element_by_xpath('//button[1]').click()
        # 判断
        time.sleep(5)
        show_date = self.driver.find_element_by_xpath('//tbody/tr[1]/td[5]').text
        show_text = self.driver.find_element_by_xpath('//tbody/tr[1]/td[6]').text
        print(show_text)
        print(show_date)
        # 删除查询结果第一项
        time.sleep(2)
        self.driver.find_element_by_xpath('//tbody/tr[1]//a[2]').click()
        # 点击确定
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='删除公告']/parent::div/following-sibling::div/button[2]").click()
        # 断言（不存在与删除记录名称及日期/内容相同的记录
        self.driver.refresh()  # 刷新浏览器
        self.driver.find_element_by_id('title').click()
        self.driver.find_element_by_id('title').send_keys('2020测试删除')
        self.driver.find_element_by_xpath('//button[1]').click()
        # 判断元素是否存在
        show = self.isElementExist("//p")
        if show == True:  # 查询无数据
            res = "暂无数据，删除成功"
            print(res)
        else:  # 查询有数据，判断第一条是否相符
            self.assertNotEqual(self.driver.find_element_by_xpath('//tbody/tr[1]/td[2]/span').get_attribute("title"),
                                "2021测试删除")  # 公告名称

class TestYongHu(TestZt):

    def setUp(self):
        super().setUp()  #超继承，在setup函数上增添打开系统管理-用户管理
        # 进入系统管理
        self.driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        #进入用户管理
        self.driver.find_element_by_link_text("用户管理").click()



    def test_yonghu_select(self):
        '''
        测试按照用户名搜索用户
        搜索账户名：test1
        :return:
        '''
        #定位账户搜索框并输入 test1
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入用户账号"]').send_keys('test1')
        time.sleep(3)
        #点击查询按钮
        self.driver.find_element_by_xpath("//span[text()='查询']/parent::button").click()
        time.sleep(2)
        #断言
        res = self.driver.find_element_by_xpath('//tbody/tr[1]/td[2]').text
        self.assertEqual('test1', res)


    def test_yonghu_add(self):
        '''
        测试新增用户（默认状态下）
        :return:
        '''
        # 点击新增
        self.driver.find_element_by_xpath('//a[@href="/user/create"]/button').click()
        # 输入新增内容，其他默认
        self.driver.find_element_by_id("Username").send_keys("新增账户名")   #输入账户名
        self.driver.find_element_by_id("password").send_keys("123456")      #输入新密码
        self.driver.find_element_by_id("rePassword").send_keys("123456")    #输入重复密码
        self.driver.find_element_by_id("NickName").send_keys("新增昵称")    #输入昵称
        #点击确定
        self.driver.find_element_by_xpath("//button[1]").click()
        #断言





    def test_yonghu_update(self):
        '''
        测试修改用户信息
        :return:
        '''
        #查询要删除的账号记录
        #点击删除
        #点击确定
        #断言


    def test_yonghu_delete(self):
        '''
        测试删除用户
        :return:
        '''
        pass

    def test_yonghu_uppw(self):
        '''
        测试修改用户秘密
        :return:
        '''
        pass



class TestJueSe(TestZt):

    def setUp(self):
        super().setUp()  #超继承，在setup函数上增添打开系统管理-角色管理
        # 进入系统管理
        self.driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        #进入角色管理
        self.driver.find_element_by_link_text("角色管理").click()
        #断言





    def test_juese_select(self):
        pass


    def test_juese_add(self):
        pass


    def test_juese_update(self):
        pass


    def test_juese_delete(self):
        pass





class TestRiZhi(TestZt):

    def setUp(self):
        super().setUp()  #超继承，在setup函数上增添打开系统管理-角色管理
        # 进入系统管理
        self.driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
        #进入系统日志
        self.driver.find_element_by_link_text("系统日志").click()



    def test_rizhi_select_byuser(self):
        '''
        测试根据操作人员查询
        操作人员：hwy
        :return:
        '''
        #搜索框输入操作人员
        self.driver.find_element_by_id("userName").send_keys("hwy")
        #点击查询
        self.driver.find_element_by_xpath("//button").click()
        #断言




    def test_rizhi_select_bystyle(self):
        pass


    def test_rizhi_select_bytime(self):
        pass

class Car(TestZt):
    def test_car(self):
        # 进入车辆在线政务
        self.driver.find_element_by_xpath('//*[@id="root"]//li[6]/div').click()
        # 进入车辆管理
        self.driver.find_element_by_link_text("车辆管理").click()
        self.getliebiao()







if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Car('test_car'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)