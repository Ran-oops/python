#集合函数



sets1 = {'王晓雨','张蓓','李丛丛','牛少朋','吕欣','刘笑国','王猛'}

boys = {'王猛','张云逸','牛少朋','王晓雨','牛广林','任泽权','韩培南'}

girls = {'李亚','周光丽','徐影','邓玉杰','赵美新','李艳玲','游可欣','万玲云','吕欣','李丛丛'}

'''
#difference  差集   b = a +1

result = sets1.difference(boys)

print(result)


#difference_update  差集更新操作 a = a +1

sets1.difference_update(boys)

print(sets1)
'''

'''
#intersection 交集

result = sets1.intersection(boys)

print(result)


#intersection_update 交集更新

sets1.intersection_update(girls)

print(sets1)
'''

'''
#union 并集

result = sets1.union(boys)

print(result)


#update 并集更新操作

sets1.update(boys)

print(sets1)

'''

'''
#issuperset 检测一个集合是否是另一个集合的超集

py1girl = {'吕欣','李丛丛'}

result = sets1.issuperset(py1girl)

print(result)



#issubset 检测一个集合是否是另一个集合的子集

result = py1girl.issubset(sets1)

print(result)


#isdisjoint检测两个集合之间是否具有相交的部分

result = boys.isdisjoint(girls)

print(result)
'''

'''
#symmetric_difference 对称差集操作

result = sets1.symmetric_difference(boys)

print(result)


#symmetric_difference_update() 对称差集更新操作

sets1.symmetric_difference_update(boys)

print(sets1)
'''
