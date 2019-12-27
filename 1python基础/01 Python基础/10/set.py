#创建空集合

set1 = set()

print(type(set1))
print(set1)


#创建多个元素的集合

set1 = {1,3,5,3,7,1,7,2,68,9,2,7,21}

print(type(set1))
print(set1)


#in & not in

set1 = {'傅元超','王硕','唐伟','贾禄','李雪','陈磊','付彬'}

result =  '王硕' in set1

print(result)

result = '王硕' not in set1

print(result)

#len()
set1 = {99,66,55,222,77,898,22}

result = len(set1)

print(result)


#max()

result = max(set1)

print(result)

#min()
result = min(set1)
print(result)


#普通集合遍历

set1 = {'TFBOYS','EXO','鹿晗','吴一凡','黄子韬'}

for i in set1:
    print(i)


#多级集合遍历

set1 = {('易杨千禧','王俊凯'),('EXO','鹿晗'),('吴一凡','黄子韬')}

for x,y in set1:
    print(x)
    print(y)


#推导式1

set1 = {'胡一菲','刘亦菲','王菲','咖啡'}

set2 = {'^_^'+i for i in set1}

print(set2)

#推导式2

set1 = {'胡一菲','刘亦菲','王菲','咖啡'}

set2 = {i for i in set1 if len(i) == 3}

print(set2)

#推导式3
set1 = {'胡一菲','刘亦菲','王菲','咖啡'}

set2 = {'霍建华','胡歌','陈伟霆','冠希'}

result = {i+j for i in set1 for j in set2}

print(result)

#推导式4
set1 = {'胡一菲','刘亦菲','王菲','咖啡'}

set2 = {'霍建华','胡歌','陈伟霆','冠希'}

result = {i+j for i in set1 for j in set2 if len(i)==len(j)}

print(result)

