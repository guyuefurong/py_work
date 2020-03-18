"""
@Author  : Laura
@File    : 0310.py
@Time    : 2020/3/10 15:30
"""
# f=open("E:\py_work\Practices\\20200309\lami.txt", "r+")
# print(f.readlines())
# for line in f:
#     print(line, "\n")
# print(f.read())
# fileObject.seek(offset[, whence])方法用于移动文件读取指针到指定位置。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
# 读取指定位置的内容：
# print(f.seek(2))
# print(f.read(1))


# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
# #         print("您输入的不是数字，请再次尝试输入！")
# #
# list=[1,2]
# list.extend("0"*5)
# print(list)
# for i in range(0, 5):
#     print(i)




import unittest
import selenium

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=3) #verbosity=3 参数表示结果的详细程度