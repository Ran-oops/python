'''
#列表（有顺序）
# 索引          0           1           2           3
gamelist = ['英雄联盟','王者荣耀','穿越火线','DNF地下城与勇士']

print(type(gamelist))

#尝试修改列表（可以修改）
gamelist[1] = '王者农药'

print(gamelist)

#通过索引值获取指定的数据
print(gamelist[1])



#元组（有顺序）
#索引           0         1           2        3          4         5
avgirlist = ('苍老师','观月雏乃','泷泽罗拉','樱井莉亚','白关美','白石茉莉奈')

print(type(avgirlist))

#尝试修改元组（不可以修改）
#avgirlist[2] = '波多野结衣'

print(avgirlist)

print(avgirlist[5])
'''

'''
#字典（没有顺序）

room3320 = {'shuai':'任泽权','mini':'吴升宇','plus':'王永君','bigeye':'牛广林','face':'张鹏程'}

print(type(room3320))

print(room3320)

#通过键来进行操作

print(room3320['face'])
'''


#集合（没有顺序）

girls = {'李丛丛','吕欣','王娇娇','兰婉婷','杨惠钧','李亚','周光丽','万玲云','游可欣','徐影','李艳玲','其他姑娘'}

print(type(girls))

print(girls)



#() , []  {}到底是谁的标志
flag = ()

print(type(flag))
