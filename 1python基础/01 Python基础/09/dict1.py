#创建空字典

#dict1 = {}
dict1 = dict()

print(type(dict1))
print(dict1)


#创建一个值的字典  键 + 值 =>键值对/元素

dict1 = {'leader':'丛浩'}

print(type(dict1))
print(dict1)

#创建多个值的字典：

#方法1
dict1 = {'teacher':'丛浩','boss':'王晶晶','banzhang':'马艺楠'}

print(type(dict1))
print(dict1)

#方法2:
dict1 = dict({'teacher':'丛浩','boss':'王晶晶','banzhang':'马艺楠'})

print(type(dict1))
print(dict1)

#方法3：
dict1 = dict(teacher='丛浩',boss = '王晶晶',banzhang = '马艺楠')
print(type(dict1))
print(dict1)

#方法4:

dict1 = dict([('teacher','丛浩'),('boss','王晶晶'),('banzhang','马艺楠')])

print(type(dict1))
print(dict1)

#方法5：
dict1 = dict(zip(('teacher','boss','banzhang'),('丛浩','王晶晶','马艺楠')))

print(type(dict1))
print(dict1)

