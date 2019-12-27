#元组推导式

tuple1 = ('空调','电扇','电灯泡','手电筒','电冰箱')

#简单的元组推导式
result = (i for i in tuple1)

print(result)#生成器


#for..in循环  可以去读生成器

for a in result:
    print(a)


#带有运算的元组推导式
tuple1 = (1,2,4,6,78,89,9,0,4,1,4,7,3)

result = (i + 100 for i in tuple1)

print(result)

#获取数据
for x in result:
    print(x)


#带有判断的元组推导式

tuple1 = (2,2,57,3,8,3,69,76,0,26,2,35,17)

#获取所有偶数
result = (i for i in tuple1 if i % 2 == 0)

print(result)

#获取数据;
for x in result:
    print(x)


#多个循环的元组推导式

girls = ('吕欣','李丛丛','王娇娇','兰婉婷')

boys = ('王雷雨','杨帅','王忠正','张家明')

result = (g+'---'+b for g in girls for b in boys)

print(result)

#获取数据
for x in result:
    print(x)


#带有条件的多个循环推导式

girls = ('吕欣','李丛丛','王娇娇','兰婉婷')

boys = ('王雷雨','杨帅','王忠正','张家明')

result = (g +'---'+b  for g in girls for b in boys if girls.index(g) ==  boys.index(b))
    
print(result)

#获取数据
for x in result:
    print(x)
