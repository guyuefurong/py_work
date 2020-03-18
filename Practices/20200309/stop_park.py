"""
@Author  : Laura
@File    : stop_park.py
@Time    : 2020/3/13 14:49
"""
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
# global s_num
# global w_num
stop_list = []
wait_list = []
stop_set = 2  # 设置停车区5个位置
wait_set = 1  # 设置排队区3个位置

'''显示菜单：1、停车； 2、离开； 3、显示当前车辆情况；'''

stop_list.extend("0"*stop_set)
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

    #判断异常输入
    if step not in range(1, 4):
        print("您的输入有误，请重新输入")
        continue

    #选择菜单1 停车
    elif step == 1:
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