print ('please input your age:')
age=int(input())
while age<1:
    print ('please input the true age:')
    age=int(input())
if  age%2==0:
    age_list=list(range(2,age+1))
else:
    age_list=list(range(1,age+1))
print (age_list)