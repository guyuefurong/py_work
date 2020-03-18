"""
@Author  : Laura
@File    : subjects.py
@Time    : 2020/3/9 15:57
"""

# 1. 有1.2.3.4个数字，能组成多少个互不相同且无重复数字的三位数，用户输入任意个数字，组成任意位数，写成类：
#
# 存在的递归逻辑
# def ceshi(n):
#     if n==0:
#         return 1
#     return n*ceshi(n - 1)

# def muchnum():
#     num=[]
#     num.append(list(input("请输入数字：")))
#     n=int(input("请输入需要组成的位数："))
#     for num_i in num:   #取最大位数
#

# def fnm(n, m):
#     if m==0:
#         return 0
#     res=n * 10 ** (m-1) + fnm(n - 1, m-1)
#     return res
#
#
# print(fnm(3,2))
#
# input_list=[]          #创建列表容器存储输入列表
# input_list=list(input("请输入（0-9）之间的数字串："))     #获取输入数字并存储到输入列表
# m=int(input("请输入要获取的位数："))        #获取需要转换的位数
# for n in range(1, len(input_list)+1):       #递归方式获取所有组合数字
#     fnm(int(input_list[-n]), m)


# list=[8, 2, 3]
# list.reverse()
# print(list)


# print(input_list)
# print(len(input_list))


# 1. 停车场题目
# 有一个停车场，有停车区和排队区两大区域。停车区车辆可在任意车位停放，进入停车场后可以随时出去。当停车区停满后，后来的车辆需要在排队区等候，
# 当停车场有车离开后，排队最前的即可进入。已经排队的车辆不可以离开，只有进入停车区后才能离开。
# 现在设定停车区车位5个，排队区可拍3位。请实现功能。

class CarPark:

    def __init__(self, stop_set=5, wait_set=3):
        '''
        :param stop_set: 预设的停车区车位数量
        :param wait_set: 预设的排队区车位数量
        '''
        self.stop_set = stop_set
        self.wait_set = wait_set

    def car_park(self, come_car, go_car, wait_car):
        '''
        :param come_car: 驶入的车辆数
        :param go_car: 驶出的车辆数
        :param wait_car: 排队区等候的车辆数
        :return: 返回 none
        '''
        all_num = come_car - go_car + wait_car  #计算停车区+排队区总车辆
        stop_num = come_car - go_car    #计算停车场内已停车辆
        now_num = stop_num + wait_car
        # while True:
        if all_num < self.stop_set + self.wait_set:     #当总车辆小于规定数量时，可停车或排队；大于时无位置
                if now_num < self.stop_set:        #已停车辆小于设置数量时，可停车，否则将驶入排队区
                    print("剩余停车位{}个，欢迎光临，请缓慢驶入!".format(self.stop_set-now_num))
                elif self.stop_set <= now_num < (self.stop_set + self.wait_set):
                    print("停车位已满，请驶入排队区等候！")
        else:
            print("停车位已满，排队区已满，请离开！")




# if __name__ == '__main__':
#     CarPark().car_park(8, 3, 3)     #无车位无排队
#     CarPark().car_park(8, 3, 1)     #无车位有排队
#     CarPark().car_park(8, 5, 0)     #有车位无排队
#     CarPark().car_park(8, 5, 2)     #有车位有排队
#     CarPark().car_park(8, 5, 3)     # 有车位有排队
#
# 比如:
# 选择功能:1显示当前车辆情况，2停车，3离开
# 功能1
# #停车区川1，川2，川3，川4，川5，
# #排队区川6，川7。
# 功能2
# 输入:川8
# #停车场满，进入排队3号。
# 功能3
# 输入:川6
# #车辆排队，无法离开
# 功能3
# 输入:川2
# #车辆离开，排队区川6进入停车区。
global s_num
global w_num
stop_list = []
wait_list = []
stop_set = 2  # 设置停车区5个位置
wait_set = 1  # 设置排队区3个位置

'''显示菜单：1、停车； 2、离开； 3、显示当前车辆情况；'''
stop_list.extend("0"*stop_set)
# print(stop_list)
# print(wait_list)

while True:
    step = int(input("请输入要进行的操作：\n 1、停车； 2、离开； 3、显示当前车辆情况； "))
    s_num = 0
    w_num = 0
    for s in stop_list:
        if s != "0":
            s_num += 1
    for t in wait_list:
        if t != "":
            w_num += 1
    # print(s_num, w_num)
    #判断异常输入
    if step not in range(1, 4):
        print("您的输入有误，请重新输入")
        continue

    #选择菜单1 停车
    elif step == 1:
        # print(stop_list)
        '''
        停车区已满，排队区已满，提示离开
        停车区已满，排队区未满,提示驶入排队区等候，并计入排队列表中;
        停车区未满，提示驶入几号位停车，并计入车库列中，排队列表对应删除;
        空车位用“0” 标记.
        '''
        car = input("请输入停车车牌号：")
        if car not in stop_list or wait_list:
            if s_num == stop_set:   #停车区已满
                if w_num == wait_set:   #排队区已满
                    print("【停车场】已满，【排队区】已满，请离开")
                elif w_num < wait_set:
                    print("【停车区】已满，请驶入【排队区】{}号位等候！".format(w_num + 1))
                    wait_list.append(car)
                    print(wait_list)
            elif s_num < stop_set:
                i = 0
                while i < stop_set:
                    if stop_list[i] == "0":
                        print("欢迎光临，可驶入【停车区】：{} 号停车位！".format(i+1))
                        stop_list[i] = car
                        print(stop_list)
                        if car in wait_list:
                            wait_list.remove(car)
                        break
                    i += 1
        else:
            print("您的车辆已停入停车场或正在排队！")
        continue

    #选择菜单2 离开
    elif step == 2:
        '''
        车辆在排队时，无法离开；
        车辆在车库时，允许离开，离开后列表标记为 ”0“；
        否则提示，车辆不再监控范围内！ 
        '''
        car = input("请输入离开车牌号：")
        if car in wait_list:
            print("车辆排队中，无法离开")
        elif car in stop_list:
            print("谢谢光临，一路顺风")
            n = stop_list.index(car)
            stop_list[n] = "0"
            if w_num > 0:
                stop_list[n] = wait_list[0]
                wait_list.pop(0)
        else:
            print("车辆不再监控范围内!")


    #选择菜单3 显示当前车辆情况
    elif step == 3:
        #显示停车区车辆情况
        if s_num == 0:
            print("【停车区】暂无车辆,", end="")
        else:
            for n in range(0, s_num):
                print("【停车区】 {} 号位已停车辆为 {} \n".format(n+1, stop_list[n]))
        # 显示排队区车辆情况
        if w_num == 0:
            print("【排队区】暂无车辆")
        else:
            for n in range(0, w_num):
                print("【排队区】 {} 号位已排队车辆为 {} \n".format(n+1, wait_list[n]))
        continue
    else:
        print("输入有误，请重新输入！")






















