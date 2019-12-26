#z字典遍历

dict1 = {'ET':'外星人','UFO':'不明飞行物','SM':'Sex Magic','ML':'毫升'}

#for ...in 循环

for i in dict1:
    print(i)#键
    print(dict1[i])#值


#for..in 键值遍历

for i,j in dict1.items():
    print(i)
    print(j)


#测试
#print(type(dict1.items()))
