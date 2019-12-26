'''
#创建列表

#1.创建空列表

#lists = []#方法1

lists = list()#方法2

print(type(lists))

print(lists)


#2.创建具有一个数据的列表

lists = ['大头死变态']

print(type(lists))

print(lists)

#3.创建具有多个数据的列表

lists = ['王尼玛','王尼妹','王蜜桃','唐马儒']

print(type(lists))

print(lists)
'''


#列表的基本操作

#1.访问列表的元素

lists = ['九纹龙','花和尚','及时雨','立地太岁']

print(lists[0])


#2.修改列表中的元素

lists[2] = '呼保义'

print(lists)

#3.添加元素（正常操作无法添加元素 需要借助函数）

#4.删除元素

del lists[2]

print(lists)

#5.删除任意变量

del lists

print(lists)



