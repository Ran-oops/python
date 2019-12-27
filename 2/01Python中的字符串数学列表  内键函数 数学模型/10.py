#导入随机模块
import random

#使用随机模块中的函数

#获取0～1之间的随机数 包含0不包含1  random()

result = random.random()

print(result)


#使用random函数 随机0-100

import math


result = 50 + math.floor(random.random() * 50)

print(result)


#choice 随机获取序列中的值

one = [1,2,3,4,5,6,7,8,9,10]

two = [1,2,3,4,5,6,7,8,9,10]

three = [1,2,3,4,5,6,7,8,9,10]

four  = [1,2,3,4,5,6,7,8,9,10]

five = [1,2,3,4,5,6,7,8,9,10]


#第一个球
result1 = random.choice(one)
print(result1)

#第2个球
result2 = random.choice(two)
print(result2)

#第3个球
result3 = random.choice(three)
print(result3)

#第4个球
result4 = random.choice(four)
print(result4)

#第5个球
result5 = random.choice(five)
print(result5)

#shuffle 随机打乱序列

one = [1,2,3,4,5,6,7,8,9,10]

print(one)

random.shuffle(one)

print(one)


#randrange()  获取指定范围内指定间隔的整数

result = random.randrange(50,100,5)

print(result)


#uniform() 返回指定返回内的随机小数

result = random.uniform(10,20)

print(result)





