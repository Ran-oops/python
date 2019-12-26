#导入math模块
import math

#ceil()   &  floor()
num = 7.5

#向上取整操作
result = math.ceil(num)
print(result)


#向下取整操作
result = math.floor(num)
print(result)


#四舍五入操作
result = round(num)
print(result)

#pow() 计算一个数值的N次方

num = 7

#result = math.pow(7,2)
result = 7**2

print(result)

#sqrt() 开平方

num = 25

result = math.sqrt(num)
print(result)

#fabs() 获取绝对值

num = -99.5

result = math.fabs(num)

print(result)

#abs()
num = -99

result = abs(num)

print(result)


#modf() 将一个浮点数拆成整数和小数部分组成的元组
num = 3.141592653

result = math.modf(num)
print(result)


#copysign()
num1 = 15
num2 =  5

result = math.copysign(num1,num2)
print(result)


#fsum() 将一个序列的所有数据求和
lists = {1,3,5,7}

result = math.fsum(lists)
print(result)

#sum() 将一个序列的所有数据求和
lists = {1,3,5,7.5}

result = sum(lists)
print(result)

#输出圆周率
print(math.pi)

#输出自然对数e的值
print(math.e)
