#元组的操作

#1.创建空元组

#tuple1 = ()
tuple1 = tuple()

print(type(tuple1))

print(tuple1)

#2.创建具有一个元素的元组

tuple1 = ('不知妻美刘强东',)#tuple1 = '不知妻美刘强东',

print(type(tuple1))

print(tuple1)

#3.创建多个元素的元素

tuple1 = ('马云','马化腾','王健林','丁磊')#tuple1 = '马云','马化腾','王健林','丁磊'

print(type(tuple1))

print(tuple1)


#元组的基本操作（除了访问啥也干不了）

#使用索引访问元素

tuple1 = ('王思聪','牛广林','牛少鸟')

print(tuple1[2])

#删除整个元组

tuple1 = ('王思聪','牛广林','牛少鸟')

del tuple1

print(tuple1)
