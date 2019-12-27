#元组的序列操作


#元组相加
tuple1 = ('肉夹馍','土豆丝卷饼','山东烧饼','煎饼','煎饼果子')

tuple2 = ('抄手','燃面','砂锅面','砂锅土豆粉')

result = tuple1 + tuple2

print(result)

#模拟修改元组

tuple1 = ('肉夹馍','土豆丝卷饼','山东烧饼','煎饼','煎饼果子')

result = tuple1[0:3] + ('糁',) + tuple1[3:]

print(result)


#元组相乘

tuple1 = ('雍建凯','李艳玲')

result = tuple1 * 5

print(result)


#分片操作

tuple1 = ('张飞','岳飞','双飞','王菲','飞飞','咖妃','尿嫔')

print(tuple1[2:5])

print(tuple1[2:])

print(tuple1[:5])

print(tuple1[:])

print(tuple1[::2])


#成员检测

tuple1 = ('张建宇','邢天宇','田宇','王雷雨','王晓雨')


result = '田宇' in tuple1

print(result)


result = '吕欣' not in tuple1

print(result)
