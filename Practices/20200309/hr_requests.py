"""
@Author  : Laura
@File    : hr_requests.py
@Time    : 2020/3/17 10:06
"""
import requests
from fake_useragent import UserAgent

'''header 第三方库，UserAgent '''

# ua=UserAgent()
# print(ua.ie)
# print(ua.opera)
# print(ua.chrome)
# print(ua.firefox)
# print(ua.safari)
# print(ua.random)
# print(ua.random)
# print(ua.random)


class HttpRequest:

    def request(self, method, url, datas=None, header=None, cookie=None): #类函数的参数
        res= requests.request(method, url, data=datas, headers=header, cookies=cookie) #requests的参数必须符合要求
        return res



if __name__ == '__main__':


    '''w伪装浏览器 方法一：复制粘贴User-Agent
    方法二：使用header第三方库 '''
    # header1 = {"User-Agent":"Mozilla/5.0"}
    us = UserAgent(verify_ssl=False)
    header1={"User-Agent":us.chrome} #us.ie   us.
    url = "https://www.baidu.com"
    # print(header1)
    HttpRequest().request("post", url, header=header1)