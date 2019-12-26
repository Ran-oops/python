#基本操作

dict1 = {'llbt':'张顺','xbw':'周通','gss':'时迁','qms':'杨志'}

#访问操作
print(dict1['qms'])
print(dict1['gss'])

#直接添加元素（键值对）

dict1['hhs'] = '鲁智深'

print(dict1)

#修改
dict1['xbw'] = '周伯通'

print(dict1)

#删除元素

del dict1['gss']

print(dict1)

#删除字典
del dict1

#print(dict1)
