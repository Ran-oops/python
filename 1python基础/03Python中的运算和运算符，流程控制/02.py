#成员运算

#字符串

#in
strval = 'if you lose myself'

result = 'lose' in strval

print(result)

#not  in

result = '姨夫' not in strval

print(result)


#列表

lists = ['赵美新','邓玉洁','徐影','李艳玲','万玲云']

result = '邓玉洁' in  lists

print(result)


result = '邓玉杰' not in lists

print(result)


#元组

tuples = ('吕欣','李丛丛','王娇娇','兰婉婷')

result = '吕欣' in tuples

print(result)


result = '张艺潇' not in tuples

print(result)


#集合

sets = {'杨帅','张云逸','王雷雨','王晓雨','张程阳','周光丽'}

result = '王晓雨' in sets

print(result)

result = '张程阳' not in sets

print(result)


#字典（判断键是否存在）

dicts = {'雍建凯':'李艳玲','赵美新':'张亮','丛浩':'张巧玲'}

result = '雍建凯' in dicts

print(result)


result = '吕欣' not in dicts

print(result)



