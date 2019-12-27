#使用0填充字符串到指定的长度  内容靠右

str1 = 'girl'
str1 = '998'

result = str1.zfill(10)

print(result)

#使用指定字符填充字符串到指定的长度 内容居中center

str1 = 'boy'

#result = str1.center(15)
result = str1.center(14,'★')

print(result)


#使用指定字符串将字符串填充到指定的长度 内容靠左对齐 ljust

str1 = 'cool'

#result = str1.ljust(10)
result = str1.ljust(10,'@')

print(result)



#使用指定字符串将字符串填充到指定的长度 内容靠右 rjust

str1 = 'cold'

#result = str1.rjust(14)
result = str1.rjust(14,'0')

print(result)


#maketrans()  制作一个翻译对照表

table = ''.maketrans('蜡笔小新','钢笔大舅')
print(table)


#translate() 进行替换操作
str1 = '蜡笔小新的爸爸也野原广志，蜡笔小新的妈妈是野原美伢,蜡笔小新的爷爷是野原银之介，蜡笔小新的妹妹是野原葵'

print(str1)

#替换操作

result = str1.translate(table)

print(result)
