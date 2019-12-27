
#字典
dict1 = {'ET':'外星人','UFO':'不明飞行物','SM':'Sex Magic','ML':'毫升'}


#字典内涵

result = {key+'☆':value+'★'  for key,value in dict1.items()}

print(result)

#带有判断条件的字典内涵

result = {key:value for key,value in dict1.items() if len(key) == 2}

print(result)


#多个循环
dict1 = {'ET':'外星人','UFO':'不明飞行物','SM':'Sex Magic','ML':'毫升'}
dict2 = {'CH':'丛浩','ED':'BO起障碍','PPH':'痔疮手术','AD':'娃哈哈'}

result = {i+x : j+y  for i,j in dict1.items() for x,y in dict2.items()}
print(result)


#多个循环带有条件

dict1 = {'ET':'外星人','UFO':'不明飞行物','SM':'Sex Magic','ML':'毫升'}
dict2 = {'CH':'丛浩','ED':'BO起障碍','PPH':'痔疮手术','AD':'娃哈哈'}

result = {i+x : j+y  for i,j in dict1.items() for x,y in dict2.items() if len(i) != len(x)}
print(result)
