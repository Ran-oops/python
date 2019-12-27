#集合函数

sets = {'古力娜扎','迪里热巴','玛尔扎哈','鹿晗','吴易凡'}

'''
#add() 向集合中添加值

sets.add('吴彦祖')

print(sets)

#pop() 随机删除集合中的值

sets.pop()

print(sets)


#remove 移除集合中指定的值(数据不存在报错)
sets.remove('鹿晗')

print(sets)


#discard() 移除集合中指定的值（数据不存在则不移除）


sets.discard('玛尔扎哈')

print(sets)



#clear() 清空集合
sets.clear()
print(sets)
'''
#copy() 复制集合

result = sets.copy()

print(result)
