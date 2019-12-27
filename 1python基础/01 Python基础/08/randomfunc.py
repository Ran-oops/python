#导入随机数模块
import random

#random()  获取0～1之间的随机小数包含0不包含1
result = random.random()
print(result)

#choice() 随机获取列表中的值

lists = ['张大炮','鲍菊花','史尚飞','支付宝','刘产','禽兽']

result = random.choice(lists)

print(result)

#shuffle() 随机打乱序列


lists = ['张大炮','鲍菊花','史尚飞','支付宝','刘产','禽兽']

random.shuffle(lists)

print(lists)

#randrange() 随机获取指定范围内指定间隔的随机数值

result = random.randrange(50,100,2)
print(result)


#uniform() 随机获取指定范围内的所有数值包括小数

result = random.uniform(5,15)
print(result)
