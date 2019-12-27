#冰冻集合


#创建冰冻集合
sets = frozenset()
print(type(sets))
print(sets)

#带有数据的冰冻集合

sets = frozenset(('冰棍','冰棒','雪糕','冰淇淋'))

print(sets)


#无法访问，可以遍历

for i in  sets:
    print(i)


#除此之外冰冻集合的用处：和其他集合进行集合操作仅此而已

sets2 = {'冰球','冰棒'}

result = sets2.intersection(sets)

print(result)
