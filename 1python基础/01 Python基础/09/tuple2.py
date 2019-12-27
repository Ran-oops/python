#序列操作
'''
#加法

tuple1 = ('王泽东','王泽西','王泽南','王泽北')

tuple2 = ('王泽左','王泽右','王泽前','王泽后')

result = tuple1 + tuple2

print(result)


#乘法
tuple1 = ('男学生','女学生')

result = tuple1 * 5

print(result)


#索引
tuple1 = ('西施','貂蝉','王昭君','杨玉环')

print(tuple1[2])
'''

#分片
tuple1 = ('吕布','许褚','典韦','关羽','张飞','赵云')

print(tuple1[2:5])
print(tuple1[:5])
print(tuple1[2:])
print(tuple1[:])
print(tuple1[1::2])

#成员检测

tuple1 = ('小鸡','小鸭','小鹅','小鸟')

result = '小鸡' in tuple1

print(result)


result = '小鸭鸭' not in tuple1

print(result)
