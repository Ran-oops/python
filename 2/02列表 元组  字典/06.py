#序列函数

#len() 检测元组的长度

tuple1 = ('吕布','吕蒙','吕欣','吕子乔','吕轻侯')

result = len(tuple1)

print(result)


#max & min  获取元组中的最大值/最小值

tuple1 = (3,32,5,77,1,-3,346,3,376,8)

maxresult = max(tuple1)

print(maxresult)

minresult = min(tuple1)

print(minresult)

#tuple 创建空元组或者将其他序列转化为元组

tuple1 = ()

print(tuple1)

tuple2 = tuple('今天天气不错，风和日丽的')

print(tuple2)
