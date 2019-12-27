#for...in循环

'''
#列表（有顺序）
students = ['高越','张亮','吴磊','郭磊','骆铜磊']


#输出列表所有的内容
#print(len(students))

index = 0
while index < len(students):
    #输出每个值
    print(students[index])
    #变量+1
    index += 1
'''

'''
#集合（无顺序）
students = {'王凯','王雷雨','王晓雨','王蒙','王中正','王广胜'}

for one  in students:
    #输出每一个值
    print(one)
'''

'''
#字典的遍历
dicts = {'shuai':'任泽权','bigeye':'牛广林','face':'张鹏程','hei':'吴升宇'}

for i in dicts:
    #获取字典的键
    print(i)
    #获取字典的值
    print(dicts[i])
'''


#字符串
strval = 'if you feel my love'

for onechar in strval:
    print(onechar)
