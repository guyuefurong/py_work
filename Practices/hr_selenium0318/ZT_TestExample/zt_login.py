"""
@Author  : Laura
@File    : zt_login.py
@Time    : 2020/3/18 14:25
"""
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains


class TestZt(unittest.TestCase):
    def setUp(self):
        chrome_driver = r"E:\Program Files\python 3.8.2\Lib\site-packages\selenium\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.implicitly_wait(5)
        self.url = "http://zt.emhes.cn/"
        self.verificationErrors = []
        global driver
        driver = self.driver


    # def test_login(self):
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
    #     login_text = driver.find_element_by_xpath("//*[@id='main_content']/div/div/section/div/div/div[2]/div[1]").text
    #     self.assertEqual(login_text,"下午好，{}，祝你开心每一天！".format(user))
    #     # print(login_text)

    def test_setting(self, day):
        '''
        设置-系统设置-修改上线天数
        day: 需要设定的天数
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
        time.sleep(10)
        # 定位系统设置-上线天数 设置框并输入天数 day
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div[2]/input").send_keys(day)
        time.sleep(30)
        # 定位并点击保存
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()














if __name__ == '__main__':
    # unittest.main()






