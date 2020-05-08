"""
@Author  : Laura
@File    : driver management.py
@Time    : 2020/4/14 16:04
"""
'''
使用unittest+selenium+openpyxl+ddt+python
测试驾驶员管理新增驾驶员功能
selenium ：ui自动化测试
openpyxl ：读取表格大量数据
ddt：unittest框架中使原本不能传参的test_函数实现传参功能'''

from selenium import webdriver
import unittest
import openpyxl
from ddt import ddt,data
from Practices.New_test.test_tools import get_data







# url = "http://dev.emhes.cn/"
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
data=r"E:\py_work\Practices\New_test\test_data\driver_data.xlsx"
list = get_data("driver_data.xlsx")         #键返回的list 存储再变量中，便于取用，函数内部的变量为局部变量，不能全局使用
@ddt            #使用ddt时，需注意变量/数据 的实例化
class TestDiverM(unittest.TestCase):

    # def setUp(self):
    #     '''
    #     测试之前操作:
    #     打开浏览器并登陆至驾驶员管理界面
    #     :return:
    #     '''
    #     driver.get(url)
    #     driver.find_element_by_id("main-login_name").send_keys("ceshi01")
    #     driver.find_element_by_id("main-login_password").send_keys("123456")
    #     driver.find_element_by_xpath('//*[text()="登 录"]/parent::button').click()  ###点击登陆
    #     s_time(10)
    #     driver.find_element_by_xpath('//*[text()="车辆管理"]/parent::span/parent::div').click()
    #     s_time(3)
    #     driver.find_element_by_link_text("驾驶员管理").click()
    #     s_time(8)
    #
    # def tearDown(self):
    #     driver.quit()

    @data(*list)
    def test_add_driver(self, a):
        print(a)
        print(type(a))
        # driver.find_element_by_xpath('//*[text()="新增"]/parent::button').click()
        # s_time(5)#点击新增
        # driver.find_element_by_id("Name").click()
        # driver.find_element_by_id("Name").send_keys(a)       #输入姓名
        # driver.find_element_by_xpath("//form//button[1]").click()       #点击确定










if __name__ == '__main__':

    unittest.main()



# list=[1,2]

# @ddt
# class Te(unittest.TestCase):
#
#     @data(*list)
#     def test_add(self,a):
#
#         print(a)
#
#
# unittest.main()
