#集合操作

#创建空集合

sets = set()

print(type(sets))

print(sets)

#具有多个数据的集合

sets = {12,3,6,4,8,2,5,2,57,8,3,3}

print(sets)


#集合可以使用的数据

sets = {'晷',12,12.5,True,1+2j,(1,2),frozenset('冰冻')}

print(sets)


#序列操作

#成员检测

sets = {'刘备','刘禅','刘表','刘柱','刘水','刘亦菲'}

result = '刘表' in sets

print(result)

result = '刘表' not in sets

print(result)


#序列函数

sets = {'刘备','刘禅','刘表','刘柱','刘水','刘亦菲'}

#len 检测集合长度
result = len(sets)

print(result)


#max & min 最大值/最小值

sets = {123,4,6,246,856,235,4557,357,568,468,670,89}

maxresult = max(sets)

print(maxresult)

minresult = min(sets)

print(minresult)


