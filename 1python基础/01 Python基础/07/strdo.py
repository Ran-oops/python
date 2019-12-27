# +  字符串连接操作

str1 = '我和你妈同时掉水里'
str2 = '你先救谁?'

result = str1 + str2
print(result)


# * 字符串复制操作

starone = '★★★★★★★★★★\n'

strten = starone * 10

print(strten)

#字符串索引操作 （索引可正可负）

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(str1[25])


#字符串取片操作  字符串[开始索引:结束索引:间隔值]
str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#从开头到指定位置之前截取
print(str1[:6])

#从指定位置截取到最后
print(str1[21:])
print(str1[-5:])

#从开始索引截取到结束索引之前（不包含结束位置）
print(str1[7:12])

#截取整个字符串
print(str1[:])

#按照指定间隔截取字符串
print(str1[0:25:2])


