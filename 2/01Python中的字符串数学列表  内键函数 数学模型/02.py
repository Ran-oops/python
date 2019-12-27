#strip 去掉字符串左右两侧指定的字符 不指定则去掉空格
'''
str1 = ' renzequan@wushengyu.com  '

print(str1)

result = str1.strip()

print(result)
'''

str1 = '111renzequan@wushengyu.com111'

print(str1)

result = str1.strip('1')

print(result)


#lstrip X去掉字符串左两侧指定的字符 不指定则去掉空格

str1 = '0000001235000000'

print(str1)

result = str1.lstrip('0')

print(result)

#rstrip去掉字符串右两侧指定的字符 不指定则去掉空格

str1 = '一群小星星飘过～☆☆☆☆☆☆☆☆☆☆☆'

print(str1)

result = str1.rstrip('☆')

print(result)
