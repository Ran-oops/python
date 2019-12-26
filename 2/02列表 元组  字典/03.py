#列表常用函数

#append在列表的末尾添加值

lists = ['口腔','食道','胃','十二指肠','大肠','小肠','肛门']

lists.append('马应龙')

print(lists)

#clear() 清空列表

lists.clear()

print(lists)

#copy() 复制列表

lists = ['口腔','食道','胃','十二指肠','大肠','小肠','肛门']

result = lists.copy()

print(result)

#检测复制列表和原列表在内存中是否是同一个列表

print(result is lists)


#count() 计算某个值在列表中出现的次数

lists = [1,2,4,6,5,8,1,3,4,7,2,4,7,2,3,7]

result = lists.count(2)

print(result)

#extend() 将一个列表继承另外一个列表 类似列表相加操作

lists1 = ['玉麒麟','智多星','入云龙','大刀']

lists2 = ['豹子头','小旋风','小李广','赤发鬼']

lists1.extend(lists2)

print(lists1)

#index 获取某个值在列表中第一次数次出现的索引值

lists = ['毛头星','混世魔王','浪里白条','菜园子','浪里白条']

result = lists.index('浪里白条')

print(result)


#insert 在列表指定位置之前中插入数据  和append是一套

lists = ['非洲','亚洲','欧洲','沧州','德州']

lists.insert(1,'八宝粥')

print(lists)


#pop 移除列表中的指定索引元素
lists = ['非洲','亚洲','欧洲','沧州','德州']

#result = lists.pop(2)
result = lists.pop()

print(result)

print(lists)

#remove  移除列表中指定的值

lists = ['非洲','亚洲','欧洲','沧州','德州']

lists.remove('沧州')

print(lists)


#reverse() 列表反转操作
lists = ['非洲','亚洲','欧洲','沧州','德州']

lists.reverse()

print(lists)


#sort() 列表排序

'''
nums = [12,1,245,1,35,1,357,56,76,23,475,235,47,254,47,574685,3574]

#数字正序排列
#nums.sort()

#数字倒序排列
nums.sort(reverse = True)

print(nums)
'''

'''
lists = [1,3,6,1,4,8,4,9,0]

#声明一个函数处理列表中的每个值
def yushu(x):
    return x%4

lists.sort(key = yushu)

print(lists)

'''

'''
lists = [1,3,6,1,4,8,4,9,0]

lists.sort(key = lambda x:x%2)

print(lists)
'''


#字符串排序
lists = ['我','合衣而眠','和你','在一起']

lists.sort(key = lambda x:len(x))

print(lists)



#字母字符串
lists = ['D','S','A','Z','Q']

lists.sort(reverse = True)

print(lists)






