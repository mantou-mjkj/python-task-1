#coding:utf-8


#类化4-1：循环递增打印你的年龄，比如你的年龄是偶数，则从2开始打印，否则从一开始打印，每次的递增数量为1。
class My_age(object):
    def __init__(self,age):
        self.__age=age

    def set_age(self,age):
        self.__age=age

    def get_age(self):
        return self.__age

    def print_age_list(self):
        if  self.__age%2==0:
            age_list=list(range(2,self.__age+1))
        else:
            age_list=list(range(1,self.__age+1))
        print (age_list)


#类化4-2：创建一个列表，包含5种不同的办公室的物品，创建一个循环，按顺序打印这个列表并写出顺序号。
class My_office(object):
    def __init__(self,office_use):
        self.__office_use=office_use

    def set_office_use(self,office_use):
        self.__office_use=office_use

    def get_office_use(self):
        return self.__office_use

    def print_office_use(self):
        i=1
        for use in self.__office_use:
            print ('%d : %s' % (i , use))
            i=i+1


#类化4-3：月球上你的体重是在地球上的16.5%，假设你每年增长1公斤，打印未来15年你的体重状况。
class My_weight(object):
    def __init__(self,weight):
        self.__weight=weight

    def set_weight(self,weight):
        self.__weight=weight

    def get_weight(self):
        return self.__weight

    def moon_weight(self):
        self.__moon_list=[]
        weight=self.__weight
        year=1
        while year<16:
            moon_weight=weight*0.165
            self.__moon_list.append(moon_weight)
            year=year+1
            weight=weight+1

    def earth_weight(self):
        self.__earth_list=[]
        weight=self.__weight
        year=1
        while year<16:
            self.__earth_list.append(weight)
            year=year+1
            weight=weight+1

    def print_weight(self):
        self.earth_weight()
        self.moon_weight()
        i=0
        while i<15:
            print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , self.__earth_list[i] , self.__moon_list[i]))
            i=i+1


#类化5-2：用函数计算任务四第三个问题中的你的体重（参数为当前体重和体重的年增量）
class My_weight_first(object):
    def __init__(self,weight,up):
        self.weight=weight
        self.up=up

    def set_weight(self,weight):
        self.weight=weight

    def get_weight(self):
        return self.weight

    def set_up(self,up):
        self.up=up

    def get_up(self):
        return self.up

    def moon_weight(self):
        self.moon_list=[]
        weight=self.weight
        year=1
        while year<16:
            moon_weight=weight*0.165
            self.moon_list.append(moon_weight)
            year=year+1
            weight=weight+self.up

    def earth_weight(self):
        self.earth_list=[]
        weight=self.weight
        year=1
        while year<16:
            self.earth_list.append(weight)
            year=year+1
            weight=weight+self.up

    def print_weight(self):
        self.earth_weight()
        self.moon_weight()
        i=0
        while i<15:
            print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , self.earth_list[i] , self.moon_list[i]))
            i=i+1


#类化5-3:用函数计算任务四第三个问题中的你的体重（参数为当前体重、体重的年增量和统计的年数）
class My_weight_second(object):
    def __init__(self,weight,up,year):
        self.weight=weight
        self.up=up
        self.year=year

    def set_weight(self,weight):
        self.weight=weight

    def get_weight(self):
        return self.weight

    def set_up(self,up):
        self.up=up

    def get_up(self):
        return self.up

    def set_year(self,year):
        self.up=up

    def get_year(self):
        return self.year

    def moon_weight(self):
        self.moon_list=[]
        weight=self.weight
        year=self.year
        i=0
        while i<year:
            moon_weight=weight*0.165
            self.moon_list.append(moon_weight)
            i=i+1
            weight=weight+self.up

    def earth_weight(self):
        self.earth_list=[]
        weight=self.weight
        year=self.year
        i=0
        while i<year:
            self.earth_list.append(weight)
            i=i+1
            weight=weight+self.up

    def print_weight(self):
        self.earth_weight()
        self.moon_weight()
        year=self.year
        i=0
        while i<year:
            print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , self.earth_list[i] , self.moon_list[i]))
            i=i+1


#类化5-4：用函数计算任务四第三个问题中的你的体重，当前体重、体重的年增量和统计年数都由输入给出。
class My_weight_third(object):
    def __init__(self,weight,up,year):
        self.weight=weight
        self.up=up
        self.year=year

    def set_weight(self,weight):
        self.weight=weight

    def get_weight(self):
        return self.weight

    def set_up(self,up):
        self.up=up

    def get_up(self):
        return self.up

    def set_year(self,year):
        self.up=up

    def get_year(self):
        return self.year

    def moon_weight(self):
        self.moon_list=[]
        weight=self.weight
        year=self.year
        i=0
        while i<year:
            moon_weight=weight*0.165
            self.moon_list.append(moon_weight)
            i=i+1
            weight=weight+self.up

    def earth_weight(self):
        self.earth_list=[]
        weight=self.weight
        year=self.year
        i=0
        while i<year:
            self.earth_list.append(weight)
            i=i+1
            weight=weight+self.up

    def print_weight(self):
        self.earth_weight()
        self.moon_weight()
        year=self.year
        i=0
        while i<year:
            print ('第%d年，在地球体重：%.2f kg，在月球体重：%.2f kg' % (i+1 , self.earth_list[i] , self.moon_list[i]))
            i=i+1

