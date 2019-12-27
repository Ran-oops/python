#导入数学模块
import math

#ceil  向上取整

num = 5.0001

result = math.ceil(num)

print(result)


#floor向下取整

num = 9.9999999

result = math.floor(num)

print(result)


#pow一个数的N次方

result = math.pow(3,4)

print(result)


#sqrt 开平方

num = 81

result = math.sqrt(num)

print(result)


#fabs 获取绝对值  浮点型

num = -9

result = math.fabs(num)

print(result)


#modf 将数值分解为小数部分和整数部分

num = -12.138

result = math.modf(num)

print(result)


#copysign  符号复制


num1 = -99

num2 = -7

result = math.copysign(num1,num2)

print(result)


#fsum 将一个序列进行求和运算

lists = [1,35,7,21,7,246]

result = math.fsum(lists)

print(result)


#math模块中的值

#圆周率
print(math.pi)

#自然底数e

print(math.e)
