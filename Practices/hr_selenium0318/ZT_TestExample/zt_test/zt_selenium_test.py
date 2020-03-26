"""
@Author  : Laura
@File    : zt_login.py
@Time    : 2020/3/18 14:25
"""
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
class TestZt(unittest.TestCase):

    def isElementExist(self, element):
        '''
        捕获异常的方法判断元素是否存在
        :param element: 元素路径表达式，如Xpath "str"
        :return:
        '''
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    @classmethod   #类方法修饰器
    def setUpClass(cls):  #必须使用@classmethod 装饰器,  所有case运行之前只运行一次    setUp():每个测试case运行之前运行
        #配置驱动path
        # chrome_driver = r"E:\Program Files\python 3.8.2\Lib\site-packages\selenium\chromedriver.exe"
        # 配置浏览器 浏览器中输入chrome://version/ 查看个人资料路径配置
        # option = webdriver.ChromeOptions()
        # option.add_argument(r'--user-data-dir = \Users\admin\AppData\Local\Google\Chrome\User Data\Profile 1')
        # self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.url = "http://zt.emhes.cn/"
        # self.verificationErrors = []
        global driver
        driver = cls.driver
        #进入首页并登陆
        driver.get(cls.url)
        time.sleep(1)
        driver.find_element_by_id("userName").send_keys("hwy")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        # 浏览器窗口最大化
        driver.maximize_window()

    def tearDown(self): #必须使用@classmethod装饰器, 所有case运行完之后只运行一次   tearDown():每个测试case运行完之后执行
        #关闭浏览器
        driver.quit()

    # def test_login(self):
    #     global driver
    #     driver = self.driver
    #     '''
    #     正确用户名和密码登陆
    #     username：hwy
    #     password：123456
    #     '''
    #     driver.get(self.url)
    #     time.sleep(1)
    #     user = "hwy"
    #     driver.find_element_by_id("userName").send_keys(user)
    #     driver.find_element_by_id("password").send_keys("123456")
    #     driver.find_element_by_id("loginBtn").click()
    #     # 断言
    #     login_text = driver.find_element_by_xpath("//*[@id='main_content']/div/div/section/div/div/div[2]/div[1]").text
    #     self.assertEqual(login_text, "早上好，{}，祝你开心每一天！".format(user))
    #     # print(login_text)
        #

#     def test_setting_day(self):
#         '''
#         设置-系统设置-修改上线天数
#         设置为7天
#         '''
#         # 定位并点击【设置】
#         driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
#         time.sleep(5)
#
#         # 定位系统设置-输入框处理，先清除原值（选中后键盘回格键实现清除 ）
#         ss = driver.find_element_by_xpath('//*[text()="上线设置"]/parent::div/following-sibling::div[1]//input[1]')
#         # 方法一：选中删除再写入
#         # ss.send_keys(Keys.CONTROL+'a')  #1.选中
#         # ss.send_keys(Keys.BACKSPACE)    #2.删除
#         # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div[2]/input").send_keys(7) # 3.写入
#
#         # 方法二：选中直接写入
#         #     ActionChains(driver).double_click(ss).perform()
#         #     ss.send_keys(10)
#         # #
#         # 方法三：js代码 (暂时不通)
#         # js = 'document.querySelector("//*[text()="上线设置"]/parent::div/following-sibling::div[1]//input[1]").value="";'
#         # driver.execute_script(js)
#         # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div[2]/input").send_keys(10)
#
#         # 注意：
#         # ss.send_keys(Keys.CONTROL+'a').send_keys(Keys.BACKSPACE) #执行报错AttributeError: 'NoneType' object has no attribute 'send_keys'
#         # time.sleep(3)
#
#         time.sleep(5)
#         # 定位并点击保存
#         driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
#         #
#         # 断言
#         time.sleep(5)
#         driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
#         res = driver.find_element_by_xpath(
#             '//*[text()="上线设置"]/parent::div/following-sibling::div[1]//input[1]').get_attribute(
#             "value")  # 获得该元素value属性值
#         self.assertEqual("10", res)
#
#     def test_setting_vioce(self):
#         '''
#         设置-声音设置
#         勾选并开启报警声音提示
#         '''
#         # 定位并点击【设置】
#         driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
#         time.sleep(5)
#         # 点击勾选第一个输入框
#         driver.find_element_by_xpath("//*[text()='开启报警声音']/parent::label//input").click()
#         # 点击保存
#         driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
#
#         # 断言
#         res1 = driver.find_element_by_xpath("//*[text()='开启报警声音']/parent::label//input").is_selected()  # 判断是否为选中状态
#         print(res1)
#         res2 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
#         print(res2)
#         self.assertEqual(True, res2)
#
#         #
#
#     def test_setting_warning(self):
#         '''
#          设置-报警控制-终端报警-紧急报警
#          接收设置
#         '''
#         # 定位并点击【设置】
#         driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
#         time.sleep(5)
#         # 点击终端报警
#         driver.find_element_by_xpath('//*[text()="终端报警"]').click()
#         # 点击报警控制
#         driver.find_element_by_xpath(
#             "/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]").click()
#         # 定位紧急报警勾选框
#         # driver.find_element_by_xpath("//*[text()='紧急报警']/following-sibling::td//input").click()
#         driver.find_element_by_xpath("//tbody[@class='ant-table-tbody']/child::tr[1]/td[2]//child::input").click()
#         time.sleep(5)
#         # 定位并点击保存
#         driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
#
#         # 断言
#
#         #
#         #
#
#     def test_go_warning(self):
#         '''
#         首页-点击报警跳转报警页面
#         '''
#         # 点击实时报警
#         driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div/div[2]').click()
#         # 断言
#         res = driver.find_element_by_xpath('//*[@id="root"]//main//span').text
#         self.assertEqual('实时报警', res, '已跳转实时报警页面')
#
#         #
#
#     def test_go_message(self):
#         '''
#         首页-点击消息跳转多媒体页面
#         '''
#         # 定位并点击消息
#         driver.find_element_by_xpath('//*[@id="root"]//section/header/div[1]/div[1]').click()
#         # 断言
#         res = driver.find_element_by_xpath('//*[@id="root"]//main//span[text()="多媒体消息"]').text
#         self.assertEqual('多媒体消息', res)
#
#
#     def test_system_gonggao_select(self):
#         '''
#         根据名称查询公告,如公告‘危险行为通告’
#         '''
#         global driver
#         driver = self.driver
#         # 进入系统管理
#         driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
#         # 进入公告管理
#         driver.find_element_by_link_text("公告管理").click()
#         # 输入公告‘危险行为通告’并查询
#         driver.find_element_by_id('title').click()
#         driver.find_element_by_id('title').send_keys('危险行为通告')
#         driver.find_element_by_xpath('//button[1]').click()
#         time.sleep(5)
#         # 断言
#         res = driver.find_element_by_xpath('//table/tbody/tr/td[2]/span').text
#         print(res)
#         self.assertEqual('危险行为通告', res)
#
#
#     def test_system_gonggao_add(self):
#         '''
#         公告管理新增公告
#         '''
#         self.setUp()
#         # 进入系统管理
#         driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
#         # 进入公告管理
#         driver.find_element_by_link_text("公告管理").click()
#         # 点击新增并输入内容保存
#         driver.find_element_by_xpath("//button[2]").click()
#         time.sleep(5)
#         driver.find_element_by_xpath('//*[@id="Title"]').click()  # 点击公告标题输入框
#         driver.find_element_by_xpath('//*[@id="Title"]').send_keys("2020测试删除1")  # 输入名称
#         time.sleep(2)
#         driver.find_element_by_xpath('//*[@id="DisplayDate"]/div/i').click()  # 点击日历
#         driver.find_element_by_xpath("//a[@title='下个月 (翻页下键)']").click()  # 日历翻页
#         time.sleep(2)
#         driver.find_element_by_xpath("//td[@title='2020年4月1日']").click()  # 输入时间
#         doc = "这是通告内容"
#         driver.find_element_by_id('Contents').send_keys(doc)  # 输入通告内容
#         driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
#         driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click()  # 点击保存，注意span不可点击
#         time.sleep(5)
#         # 断言
#         driver.refresh()  # 刷新
#         res = driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
#         self.assertEqual('2020测试删除', res)
#
#
#     def test_system_gonggao_update(self):
#         '''
#         修改已存在的指定公告
#         修改公告序号:1
#         标题修改为 :20200323 公告
#         现实日期修改为:2020 03 30
#         公告内容修改为：天气黄色警告，请小心驾驶
#         '''
#         # 进入系统管理
#         driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
#         #进入公告管理
#         driver.find_element_by_link_text("公告管理").click()
#         #点击修改
#         driver.find_element_by_xpath('//thead/following-sibling::tbody/tr[1]/td[7]/a[1]').click()
#         driver.find_element_by_id("Title").clear()
#         driver.find_element_by_id("Title").send_keys("20200323 公告") #修改公告标题
#         time.sleep(2)
#         driver.find_element_by_xpath('//*[@placeholder="请选择日期"]').click() #点击日历输入框
#         time.sleep(2)
#         driver.find_element_by_xpath("//td[@title='2020年3月30日']").click() #输入时间
#         driver.find_element_by_id('Contents').clear()
#         doc = "天气黄色警告，请小心驾驶"
#         driver.find_element_by_id('Contents').send_keys(doc) #输入通告内容
#         driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div').click()  # 点击空白处跳出输入框
#         driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click() #点击保存，注意span不可点击
#         #断言
#         driver.refresh() #刷新
#         res = driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/span').text
#         self.assertEqual('2020安全管理通告', res)
#
#     def test_system_gonggao_delete(self):
#         '''
#         按照名称删除已存在的公告
#         根据名称查询公告,如“2020测试删除”
#         删除已查询的公告
#         :return:
#         '''
#         # 进入系统管理
#         driver.find_element_by_xpath('//*[@id="root"]//li[3]/div').click()
#         # 进入公告管理
#         driver.find_element_by_link_text("公告管理").click()
#         # 查询公告
#         driver.find_element_by_id('title').click()
#         driver.find_element_by_id('title').send_keys('2020测试删除')
#         driver.find_element_by_xpath('//button[1]').click()
#         # 判断
#         time.sleep(5)
#         show_date = driver.find_element_by_xpath('//tbody/tr[1]/td[5]').text
#         show_text = driver.find_element_by_xpath('//tbody/tr[1]/td[6]').text
#         print(show_text)
#         print(show_date)
#         # 删除查询结果第一项
#         time.sleep(2)
#         driver.find_element_by_xpath('//tbody/tr[1]//a[2]').click()
#         # 点击确定
#         time.sleep(2)
#         driver.find_element_by_xpath("//*[text()='删除公告']/parent::div/following-sibling::div/button[2]").click()
#         # 断言（不存在与删除记录名称及日期/内容相同的记录
#         driver.refresh()  # 刷新浏览器
#         driver.find_element_by_id('title').click()
#         driver.find_element_by_id('title').send_keys('2020测试删除')
#         driver.find_element_by_xpath('//button[1]').click()
#         # 判断元素是否存在
#         show = self.isElementExist("//p")
#         if show == True:  # 查询无数据
#             res = "暂无数据，删除成功"
#             print(res)
#         else:  # 查询有数据，判断第一条是否相符
#             self.assertNotEqual(driver.find_element_by_xpath('//tbody/tr[1]/td[2]/span').get_attribute("title"),
#                                 "2021测试删除")  # 公告名称
#
#
# if __name__ == '__main__':
#     from ZT_TestExample.zt_test.zt_shouye_test import TestShouYe
#     suit = unittest.TestSuite()
#     suit.addTest(TestShouYe("test_go_message"))
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suit)



if __name__ == '__main__':
#     # unittest.main()
#     # 执行用例
#     import zt_shouye_test
#
#     file_name = '../ceshibaogao.html'
#     # fp = open(file_name, 'wb')
#     suit = unittest.TestSuite()
#     # suit.addTest(zt_selenium_test.TestZt("test_system_gonggao_add"))
#     suit.addTest(zt_shouye_test.TestShouYe("test_go_message"))
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suit)
#     # HTMLTestRunner(stream=fp, description='测试报告描述', title='测试报告').run(suit)



    from test_shouye import TestShouYe
    loader= unittest.TestLoader
    file_name = '../ceshibaogao.html'
    fp = open(file_name, 'wb')
    suit = unittest.TestSuite()
    # suit.addTest(zt_selenium_test.TestZt("test_system_gonggao_add"))
    suit.addTest(loader.loadTestsFromTestCase(TestShouYe))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suit)
    HTMLTestRunner(stream=fp, description='测试报告描述', title='测试报告').run(suit)



