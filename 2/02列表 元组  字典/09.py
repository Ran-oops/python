#创建字典

#1.创建空字典

#dict1 = {}

dict1 = dict()

print(type(dict1))

print(dict1)


#2.创建具有多个元素的字典

#方法1：
dict1 = {'shuai':'任泽权','bigeye':'牛广林','face':'张鹏程'}

print(dict1)

#方法2：
dict2 = dict({'shuai':'任泽权','bigeye':'牛广林','face':'张鹏程'})

print(dict2)

#方法3:

dict3 = dict(shuai = '任泽权',bigeye = '牛广林',face = '张鹏程')

print(dict3)

#方法4：

lists = [
    ['shuai','任泽权'],
    ['bigeye','牛广林'],
    ['face','张鹏程']
]

dict4 = dict(lists)

print(dict4)


tuple1 = (
    ('shuai','任泽权'),
    ('bigeye','牛广林'),
    ('face','张鹏程')
)

dict4 = dict(tuple1)

print(dict4)


#方法5

key = ('shuai','bigeye','face')
value = ('任泽权','牛广林','张鹏程')

dict5 = dict(zip(key,value))

print(dict5)
