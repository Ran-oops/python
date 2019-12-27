#列表推导式

lists = ['李亚','周光丽','李艳玲','邓玉杰','赵美新']

#最简单的列表推导式
result = [i for i in lists]

print(result)

#带有运算的列表推导式
result = [girl+'^_^' for girl in lists]

print(result)

#带有条件判断的列表推导式
nums = [1,2,3,65,2,7,1,4,8,4,9]

result = [i for i in nums if i % 2 == 1]

print(result)


#多循环推导式

boys = ['吴升宇','雍建凯','徐达','张鸿喜']

girls = ['徐影','游可欣','万玲云','周光丽']


result = [b+'<->'+g for b in boys for g in girls]

print(result)


#卖鞋

size = [37,38,39,40,41,42,43,44]

color = ['red','green','blue','cyan','white']


result = [str(s) +'--'+c for s in size  for c in color]

print(result)   


#多循环推导式带有判断条件的格式

boys = ['吴升宇','雍建凯','徐达','张鸿喜']

girls = ['徐影','游可欣','万玲云','周光丽']


result = [b +'--'+ g for b in boys for g in girls if boys.index(b) == girls.index(g) ]

print(result)



print(boys.index('徐达'))




list1 = [str(i) +'*'+str(j) +'='+str(i*j)  for i  in range(1,10)  for j in  range(1,i+1)]
print(list1)

for  i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%2d' % (j,i,i*j),end='')
    print('')
