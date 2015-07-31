#coding:utf-8

import _6_1,input_type

print ('循环递增打印你的年龄，比如你的年龄是偶数，则从2开始打印，否则从一开始打印，每次的递增数量为1。')
age=_6_1.My_age(11)
#age.print_age_list()
print ('创建一个列表，包含5种不同的办公室的物品，创建一个循环，按顺序打印这个列表并写出顺序号。')
office_use=['桌子','椅子','电脑','文件夹','纸笔']
office=_6_1.My_office(office_use)
#office.print_office_use()
print ('月球上你的体重是在地球上的16.5%，假设你每年增长1公斤，打印未来15年你的体重状况。')
weight=_6_1.My_weight(50)
#weight.print_weight()
print ('用函数计算任务四第三个问题中的你的体重（参数为当前体重和体重的年增量）')
weight_first=_6_1.My_weight_first(50,2)
#weight_first.print_weight()
print ('用函数计算任务四第三个问题中的你的体重（参数为当前体重、体重的年增量和统计的年数）')
weight_second=_6_1.My_weight_second(60,2,10)
#weight_second.print_weight()
print ('用函数计算任务四第三个问题中的你的体重，当前体重、体重的年增量和统计年数都由输入给出。')
print ('请输入你的体重：',end='')
weightnext=input()
while not input_type.is_float(weightnext):
    print ('请正确输入体重：',end='')
    weightnext=input()
weightnext=float(weightnext)
print ('请输入你的体重年增量：',end='')
up=input()
while not input_type.is_float(up):
    print ('请正确输入体重年增量：',end='')
    up=input()
up=float(up)
print ('请输入统计年数：',end='')
year=input()
while not input_type.is_int(year):
    print ('请正确输入统计年数：',end='')
    year=input()
year=int(year)
weight_third=_6_1.My_weight_third(weightnext,up,year)
weight_third.print_weight()