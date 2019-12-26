'''
#add()
set1 = {1,2,3,4,5,6,7,8,9,0}

set1.add('A')

print(set1)

#pop() & remove() & discard()

set1 = {'晶晶','津津','吉吉','静静','菁菁','京京','婧婧'}

#print(set1.pop())
#print(set1.remove('京京1'))
#print(set1.discard('京京1'))
print(set1)

#clear()
set1 = {'晶晶','津津','吉吉','静静','菁菁','京京','婧婧'}

set1.clear()

print(set1)

#copy()

set1 = {'晶晶','津津','吉吉','静静','菁菁','京京','婧婧'}

set2 = set1.copy()

print(set2)
'''


#集合运算函数

#difference()差集 
set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

result = set1.difference(set2)

print(result)

#difference_update()差集更新

set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

set1.difference_update(set2)

print(set1)


#intersection()交集


set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

result = set1.intersection(set2)

print(result)

#intersection_update()交集更新

set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

set1.intersection_update(set2)

print(set1)

#union()并集

set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

result = set1.union(set2)

print(result)

#update()并集更新

set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

set1.update(set2)

print(set1)


#超集子集运算
set1 = {'蓝天','白云','农妇','山泉','田'}

set2 = {'农妇','山泉'}


result = set1.issuperset(set2)
print(result)


result = set2.issubset(set1)
print(result)

#非相交集合

set1 = {1,2,3,4,5,6,7}

set2 = {'A','B','C','D',2}

result = set1.isdisjoint(set2)

print(result)

#symmetric_difference对称差集操作
set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

result = set1.symmetric_difference(set2)

print(result)

#symmetric_difference_update对称差集操作
set1 = {'黄土','高坡','盆地','黑土','白云','丘陵'}

set2 = {'乔峰','鸠摩智','高坡','松下梅川衣服','黄土','井上梅川酷子'}

set1.symmetric_difference_update(set2)

print(set1)
