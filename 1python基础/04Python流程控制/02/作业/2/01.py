'''
#普通变量赋值

mynum = 250

#输出值
print(mynum)
#获取数据类型
numtype = type(mynum)
print(numtype)

#获取id标识
numid = id(mynum)
print(numid)
'''



'''

#多个变量名指向同一个值

num1 = num2 = num3 = 290

print(num1)
print(id(num1))

print(num2)
print(id(num2))

print(num3)
print(id(num3))
'''



#多个变量指向多个值

#num1 = 250

#num2 = 0.03

#num3 = 2

num1,num2,num3 = 250,0.03,2


print(num1,num2,num3)
