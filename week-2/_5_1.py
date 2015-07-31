#coding:utf-8

import input_type

#4-1函数化
def my_age():
    print ('please input your age:',end='')
    age=int(input())
    while age<1:
        print ('please input the true age:')
        age=int(input())
    if  age%2==0:
        age_list=list(range(2,age+1))
    else:
        age_list=list(range(1,age+1))
    print (age_list)


#4-2函数化
def office_use():
    office_use=['桌子','椅子','电脑','文件夹','纸笔']
    i=1
    for use in office_use:
        print ('%d : %s' % (i , use))
        i=i+1


#4-3函数化
def my_weight():
    print ('please input your wdight:',end='')
    weight=float(input())
    while weight<1:
        print ('please input the true whight:')
        weight=float(input())
    moon_list=[]
    earth_list=[]
    year=1
    while year<16:
        moon_weight=weight*0.165
        earth_list.append(weight)
        moon_list.append(moon_weight)
        year=year+1
        weight=weight+1
    i=1
    while i<16:
        print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i , earth_list[i-1] , moon_list[i-1]))
        i=i+1

#5-2：用函数计算任务四第三个问题中的你的体重（参数为当前体重和体重的年增量）
def my_weight_first(weight,up):
    moon_list=[]
    earth_list=[]
    year=1
    while year<16:
        moon_weight=weight*0.165
        earth_list.append(weight)
        moon_list.append(moon_weight)
        year=year+1
        weight=weight+up
    i=1
    while i<16:
        print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i , earth_list[i-1] , moon_list[i-1]))
        i=i+1


#5-3:用函数计算任务四第三个问题中的你的体重（参数为当前体重、体重的年增量和统计的年数）
def my_weight_second(weight,up,year):
    moon_list=[]
    earth_list=[]
    i=0
    while i<year:
        moon_weight=weight*0.165
        earth_list.append(weight)
        moon_list.append(moon_weight)
        i=i+1
        weight=weight+up
    i=0
    while i<year:
        print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , earth_list[i] , moon_list[i]))
        i=i+1


#5-4:用函数计算任务四第三个问题中的你的体重，当前体重、体重的年增量和统计年数都由输入给出。
def my_weight_third():
    print ('请输入你的体重：',end='')
    weight=input()
    while not input_type.is_float(weight):
        print ('请正确输入体重：',end='')
        weight=input()
    weight=float(weight)
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
    moon_list=[]
    earth_list=[]
    i=0
    while i<year:
        moon_weight=weight*0.165
        earth_list.append(weight)
        moon_list.append(moon_weight)
        i=i+1
        weight=weight+up
    i=0
    while i<year:
        print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , earth_list[i] , moon_list[i]))
        i=i+1


