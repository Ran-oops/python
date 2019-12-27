#集合的遍历

sets = {'联想','微软','戴尔','惠普','华硕','微星','神舟','雷神'}

#遍历操作

for i in sets:
    print(i)


#二级集合

sets = {
        ('联想','IBM'),
        ('戴尔','外星人'),
        ('微星','雷神'),
        ('华硕','惠普')
}

#遍历操作
for v1,v2 in sets:
    print(v1,v2)



#推导式

sets = {23,64,7,3,8,37,79,80,82}

#推导式
result = {i for i in sets}

print(result)

#带运算的推导式
result = {i*3 for i in sets}

print(result)

#带有判断条件的推导式

result = {i for i in sets if i %2 ==0}

print(result)


#多循环推导式
sets1 = {'2','4','6','8','10'}

set2 = {'1','3','5','7','9'}

result = {i+j for i in sets1 for j in set2}

print(result)

#带有判断的多循环推导式

sets1 = {'12','4','6','8','10'}

set2 = {'1','13','5','17','9'}


result = {i+j for i in sets1 for j in set2 if len(i)==len(j) and len(i) == 2}

print(result)


