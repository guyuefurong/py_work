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

class TestZt(unittest.TestCase):
    def setUp(self):
        chrome_driver = r"E:\Program Files\python 3.8.2\Lib\site-packages\selenium\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.implicitly_wait(5)
        self.url = "http://zt.emhes.cn/"
        self.verificationErrors = []
        global driver
        driver = self.driver


    def test_login(self):
        '''
        正确用户名和密码登陆
        username：hwy
        password：123456
        '''
        driver.get(self.url)
        time.sleep(1)
        user = "hwy"
        driver.find_element_by_id("userName").send_keys(user)
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        # 断言
        login_text = driver.find_element_by_xpath("//*[@id='main_content']/div/div/section/div/div/div[2]/div[1]").text
        self.assertEqual(login_text, "下午好，{}，祝你开心每一天！".format(user))
        # print(login_text)

    def test_setting_day(self):
        '''
        设置-系统设置-修改上线天数
        设置为7天
        '''
        # 登陆账号和密码进入首页
        driver.get(self.url)
        time.sleep(1)
        user = "hwy"
        driver.find_element_by_id("userName").send_keys(user)
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        # 浏览器窗口最大化
        driver.maximize_window()
        # 定位并点击【设置】
        driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
        time.sleep(5)

        # 定位系统设置-输入框处理，先清除原值（选中后键盘回格键实现清除 ）
        ss = driver.find_element_by_xpath('//*[text()="上线设置"]/parent::div/following-sibling::div[1]//input[1]')
        #方法一：选中删除再写入
        # ss.send_keys(Keys.CONTROL+'a')  #1.选中
        # ss.send_keys(Keys.BACKSPACE)    #2.删除
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div[2]/input").send_keys(7) # 3.写入

        # 方法二：选中直接写入
        ActionChains(driver).double_click(ss).perform()
        ss.send_keys(7)

        # 方法三：js代码 (暂时不通)
        # js = 'document.querySelector("//*[text()="上线设置"]/parent::div/following-sibling::div[1]//input[1]").value="";'
        # driver.execute_script(js)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div[2]/input").send_keys(10)

        #注意：
        # ss.send_keys(Keys.CONTROL+'a').send_keys(Keys.BACKSPACE) #执行报错AttributeError: 'NoneType' object has no attribute 'send_keys'
        # time.sleep(3)

        time.sleep(5)
        # 定位并点击保存
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()

        # 断言


    def test_setting_warning(self):
        '''
         设置-报警控制-终端报警-紧急报警
         接收设置
        '''
        # 登陆账号和密码进入首页
        driver.get(self.url)
        time.sleep(1)
        user = "hwy"
        driver.find_element_by_id("userName").send_keys(user)
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        # 浏览器窗口最大化
        driver.maximize_window()

        # 定位并点击【设置】
        driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
        time.sleep(5)
        #点击终端报警
        driver.find_element_by_xpath('//*[text()="终端报警"]').click()
        #点击报警控制
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]").click()
        # 定位紧急报警勾选框
        # driver.find_element_by_xpath("//*[text()='紧急报警']/following-sibling::td//input").click()
        driver.find_element_by_xpath("//tbody[@class='ant-table-tbody']/child::tr[1]/td[2]//child::input").click()
        time.sleep(5)
        # 定位并点击保存
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()

        # 断言


    def test_setting_vioce(self):
        '''
        设置-声音设置
        勾选并开启报警声音提示
        '''
        # 登陆账号和密码进入首页
        driver.get(self.url)
        time.sleep(1)
        user = "hwy"
        driver.find_element_by_id("userName").send_keys(user)
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        # 浏览器窗口最大化
        driver.maximize_window()

        # 定位并点击【设置】
        driver.find_element_by_xpath("//*[@id='root']/section/section/header/div/div[3]").click()
        time.sleep(5)
        # 点击勾选第一个输入框
        driver.find_element_by_xpath("//*[text()='开启报警声音']/parent::label//input").click()
        # 点击保存
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()

        #断言
        res1 = driver.find_element_by_xpath("//*[text()='开启报警声音']/parent::label//input").is_selected()
        print(res1)
        res2 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
        print(res2)
        self.assertEqual(True, res2)

















if __name__ == '__main__':
    # 执行用例
    import zt_login
    # file = open("result.txt", "wb")
    suit = unittest.TestSuite()
    suit.addTest(zt_login.TestZt("test_setting_vioce"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)





