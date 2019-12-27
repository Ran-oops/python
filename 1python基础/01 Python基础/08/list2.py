#序列相加

list1 = ['蛏子','蛤蜊','海虹','牡蛎']
list2 = ['龙虾','皮皮虾','河虾']

lists = list1 + list2

print(lists)

#序列相乘

list1 = ['蟹肉棒','章鱼丸','虾球']

lists = list1 * 5

print(lists)

#索引操作

list1 = ['草鱼','鲫鱼','鲤鱼','鲢鱼','鳙鱼']
list1[1] = '鲶鱼'
print(list1[1])

#分片操作

list1 = ['草鱼','鲫鱼','鲤鱼','鲢鱼','鳙鱼']

print(list1[1:4])

print(list1[:4])

print(list1[1:])

print(list1[:])

print(list1[::2])

#成员检测
list1 = ['张飞','张辽','张郃','蟑螂','张开嘴']

#result =  '张郎' in list1
result =  '张郎' not in list1

print(result)

