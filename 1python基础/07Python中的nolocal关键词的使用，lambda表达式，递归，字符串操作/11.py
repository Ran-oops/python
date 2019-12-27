#计算字符串长度 len

str1 = '如果被五步蛇咬伤了，怎么才能活着到医院，走四步，让蛇再咬一口，再走四步，再咬一口！'

result = len(str1)

print(result)


#计算字符出现次数 count

str1 = '大一：兄弟给我介绍个女朋友呗；大二：兄弟给我介绍个女的呗；大三：兄弟给我介绍个呗；大四：兄弟你过来一下呗'

#result = str1.count('兄弟')

result = str1.count('兄弟',10,40)

print(result)



#获取指定字符串的位置 find & index

str1 = '大一：兄弟给我介绍个女朋友呗；大二：兄弟给我介绍个女的呗；大三：兄弟给我介绍个呗；大四：兄弟你过来一下呗'

#result = str1.find('女朋友')

result = str1.find('女朋友',15,25)

print(result)


#result = str1.index('女朋友')

result = str1.index('女朋友',15,25)

print(result)
