#coding:utf-8
print ('please input your wdight:')
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