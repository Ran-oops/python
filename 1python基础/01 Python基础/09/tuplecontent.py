#列表推导式
tuple1 = ['小米','小朱','小张','小王']

result = [i for i in tuple1]

print(result)

for x in result:
    print(x)


print('---------------------------------')

#元组推导式

tuple1 = ('小米','小朱','小张','小王')

result = (i for i in tuple1)

print(result)

#遍历一个元组推导式得到的生成器
for x in result:
    print(x)


#带有条件的推导式

tuple1 = (1,3,6,2,57,7,2,568,2,8,24,79,2,698,23,5,2,6,4,6)

result = (i for i in tuple1 if i % 2 ==1)
print(result)

for x in result:
    print(x)

#多个循环的推导式
tuple1 = ('不怕冷','冬天','祥龙','摩托车')
tuple2 = ('宋晓寒','李雪','闫瑞龙','孙嘉驰')
for x in result:
    print(x)

result = (x+'->'+y for x in tuple1 for y in tuple2)

print(result)

for i in result:
    print(i)


#多个循环的推导式 带有条件
tuple1 = ('不怕冷','冬天','祥龙','摩托车')
tuple2 = ('宋晓寒','李雪','闫瑞龙','孙嘉驰')
for x in result:
    print(x)

result = (x+'->'+y for x in tuple1 for y in tuple2 if tuple1.index(x) == tuple2.index(y))

print(result)

for i in result:
    print(i)
