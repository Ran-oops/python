#创建空的冰冻集合

fset = frozenset()

print(type(fset))

print(fset)


#创建具有元素的集合

fset = frozenset(('老大','老二','老三','老五'))

print(type(fset))

print(fset)


#遍历冰冻集合

for i in fset:
    print(i)



result = {i for i in fset}

print(result)

#尝试修改：无从下手


#冰冻集合的函数

copy() 复制集合

difference() 计算2个集合的差集

intersection() 计算2个集合的交集

union() 计算2个集合的并集

symmetric_difference() 对称差集

isdisjoint() 检测是否具有交集

issuperset() 检测是否是另一个集合的超集

issubset() 检测是否是另一个集合的子集


