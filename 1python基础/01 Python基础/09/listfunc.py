#append() 向列表中添加元素

list1 = ['丛浩','丛老湿','丛叫兽','丛禽兽']

list1.append('丛圣人')

print(list1)


#clear() 清空列表

list1 = ['丛浩','丛老湿','丛叫兽','丛禽兽']

list1.clear()

print(list1)


#copy() 复制列表

list1 = ['巴达兽','天使兽','神圣天使兽']

list2 = list1.copy()

print(list1)

print(list2)


#count() 计算某个元素出现的次数

list1 = [1,3,6,2,5,6,43,289,1,6,3,8,1,78,5,89,2,79,23,1,4,5,2,5]

result = list1.count(1)

print(result)

#extend() 将一个列列表继承另一个列表

list1 = ['巴鲁兽','仙人掌兽','花仙兽']
list2 = ['格玛兽','海狮兽','祖顿兽']

list1.extend(list2)

print(list1)

#index() 获取值在列表中的索引
list1 = ['巴鲁兽','仙人掌兽','花仙兽']

i = list1.index('花仙兽')

print(i)

#insert() 在指定位置之前插入值

list1 = ['加布兽','兽人加鲁鲁','钢铁加鲁鲁']

list1.insert(1,'加鲁鲁兽')

print(list1)

#pop() 在列表的默认移除一个元素
list1 =['丛浩','丛老湿','丛叫兽','丛禽兽']
 
#list1.pop() 
list1.pop(2)

print(list1)


#remove() 移除列表中指定的值
list1 =['丛浩','丛老湿','丛叫兽','丛良','丛禽兽']

list1.remove('丛良')

print(list1)

#reverse() 列表反转
list1 =['丛浩','丛老湿','丛叫兽','丛良','丛禽兽']

list1.reverse()

print(list1)

#sort()
list1 = [2,2,6,12,5,3,7,13,26,3,8,2,8,237,34,6]

#list1.sort()
#list1.sort(reverse=True)
print(list1)


list2 = ['S','G','H','A','a','z','m','i']

#list2.sort()
#将值进行指定的处理之后在排序
list2.sort(key = str.upper)

print(list2)


