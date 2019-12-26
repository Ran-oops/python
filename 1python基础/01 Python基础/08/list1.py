'''
#c创建空列表

#list1 = []
list1 = list()

print(type(list1))
print(list1)


#创建一个数据的列表

list1 = ['鲨鱼']

print(type(list1))
print(list1)

#创建具有多个数据的列表

list1 = ['鲨鱼','鲸鱼','鲅鱼','琵琶鱼']

print(list1)
'''

#访问操作
list1 = ['娃娃鱼','胖头鱼','鳄鱼','美人鱼']
#通过索引访问数据
print(list1[3])


#列表的添加 （普通操作不可以 以后学函数才可以）
#list1[4] = '鱿鱼'
#print(list1)


#列表的修改
list1[1] = '鲍鱼'
print(list1)

#列表中元素的删除
del list1[2]
print(list1)



