"""
@Author  : Laura
@File    : function.py
@Time    : 2020/3/9 14:06
"""

class CountTwoNum:
    '''两位数运算类'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_num(self):                    #addition 加法
        res=self.a+self.b
        return res

    def sub_num(self):                         #subtraction 减法
        res = self.a - self.b
        return res

    def mul_num(self):                          #multiplication 乘法
        res = self.a * self.b
        return res

    def div_num(self):                          #division 除法
        res = self.a / self.b
        return res


# if __name__ == '__main__':
#
#     # print(CountTwoNum(4, 2).add_num())
#     # print(CountTwoNum(4, 2).sub_num())
#     # print(CountTwoNum(4, 2).mul_num())
#     # print(CountTwoNum(4, 2).div_num())


class BubbleSort():
    '''冒泡排序类'''
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        for m in range(1, len(self.arr)):            #循环比较n-1次,控制次数
            # print("第{}层比较：".format(m))
            for n in range(0, len(self.arr)-1):
                if self.arr[n] > self.arr[n+1]:         #如果第前一位大于后一位则执行换位
                    self.arr[n], self.arr[n+1] = self.arr[n+1], self.arr[n]
                # print("第{}层，第{}次结果：".format(m, n+1), self.arr)
        return self.arr

# if __name__ == '__main__':
#     list=[1,9,6,5,7]
#     res=BubbleSort(list).bubbleSort()
#     print(res)



class Square:
    '''平方根运算'''
    def __init__(self, num):
        self.num = int(num)

    def square_num(self):
        res=self.num**(1/2)
        return res

# if __name__ == '__main__':
#     print(Square(10).square_num())



class Triangle():
    ''' 计算面积
       1. 计算三角行面积,输入三边长a,b,c
       公式描述：公式中a，b，c分别为三角形三边长，p=(a+b+c)/2为半周长，S为三角形的面积。（开根号有精度损失）
        s=根号下（p(p-a)(p-b)(p-c)） #海伦公式'''
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def triangle_area(self):
        p = (self.a+self.b+self.c)/2
        s = (p*((p-self.a)*(p-self.b)*(p-self.c)))**(1/2)
        return s




class Circular:
    '''计算圆形面积,输入半径R'''
    def __init__(self, r ,pai=3.14):
        self.r = r
        self.pai = pai

    def circular_area(self):
        s=self.pai * self.r**2
        return s


class Rectangle:
    '''计算矩形面积,输入长 l 和宽 w'''
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def rec_area(self):
        s=self.l * self.w
        return s

# if __name__ == '__main__':
#     print(Triangle(3,4,5).triangle_area())
#     print(Circular(5).circular_area())
#     print(Rectangle(5,4).rec_area())





class JudgeNum:
    '''输入数，判断是否正数/负数/0'''
    def judge_num(self):
        # global num
        while True:
            num_str = input("请输入要判断的数字：")
            try:
                num = int(num_str)
            except ValueError:
                print("输入错误!")
                continue
            if (num == 0):
                print("{}为零！".format(num))
            elif (num > 0):
                print("{}为正数!".format(num))
            elif (num < 0):
                print("{}为负数!".format(num))
            answer = input("是否继续判断？ Y/N").upper()
            if answer == "N":
                break

# if __name__ == '__main__':
#     JudgeNum().judge_num()





class JOENumber:
    '''判断奇偶数'''
    def joenumber(self):
        while True:
            try:
                num = int(input("请输入要判断的非0数字："))
            except:
                print("输入错误，请重新输入！")
                continue
            else:
                res = num % 2
                if num != 0:
                    if res == 0:
                        print("{}是偶数".format(num))
                    else:
                        print("{}是奇数".format(num))
                else:
                    print("请输入非0数！")
                    continue
                break


# if __name__ == '__main__':
#     JOENumber().joenumber()




class LeapYear:
    '''判断闰年'''
    def leap_year(self):
        input_year = int(input("请输入要判断的年份："))
        if input_year % 400 == 0:
            print("{}年是世纪闰年！".format(input_year))
        elif input_year % 4 == 0:
            print("{}年是闰年！".format(input_year))
        else:
            print("{}年不是闰年！".format(input_year))
        return


# if __name__ == '__main__':
#     LeapYear().leap_year()


class ProduceCalendar:
    '''输入年月，生成当年当月日历'''

    def pro_calendar(self, year, month):
        import calendar
        # year =int(input("年份："))
        # month = int(input("月份："))
        res = calendar.month(int(year), int(month))
        print(res)


ProduceCalendar().pro_calendar(2000,3)



























