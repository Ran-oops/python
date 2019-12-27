#列表的序列操作


#列表相加
lists1 = ['张全蛋']

lists2 = ['赵铁柱','李小花']


lists = lists1 + lists2

print(lists)


#列表相乘

lists = ['小嘴']

result = lists * 5

print(result)


#索引操作

lists = ['守护在她身边','帮她盖上被子','亲吻她一下','把她XX了']


#男人的期待
print(lists[2])
print(lists[3])
print(lists[3])
print(lists[3])
print(lists[1])
print(lists[0])

#女人的期待
print(lists[2])
print(lists[1])
print(lists[0])

#取片操作

lists = ['李丛丛','吕欣','李艳玲','万玲云','游可欣','邓玉杰']

print(lists[1:4])

print(lists[2:])

print(lists[:3])

print(lists[::3])

#成员检测

result = '邓玉杰' in lists

print(result)


result = '李亚' not in lists

print(result)


#序列相关的函数操作

#len 获取列表的长度

lists = ['李丛丛','吕欣','李艳玲','万玲云','游可欣','邓玉杰']

result = len(lists)

print(result)


#max & min 获取列表中的最大值/最小值

lists = [1,36,2,67,5,2,8,34,8,358]

result = max(lists)

print(result)

result = min(lists)

print(result)




