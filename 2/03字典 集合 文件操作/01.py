#序列操作
#成员检测
dict1 = {'yt':'圆通','zt':'中通','st':'申通','ht':'汇通'}

#result = 'zt' in dict1

result = '中通' not in dict1

print(result)


#len 获取字典的元素个数

result = len(dict1)

print(result)


#max 最大值  min 最小值

#dict1 = {'a':12,'b':23,'c':4,'d':68}

dict1 = {42:'A',47:'F',236:'J',64:'H'}

maxresult = max(dict1)

print(maxresult)

minresult = min(dict1)

print(minresult)
