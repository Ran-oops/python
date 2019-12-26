#for ...in

tuple1 = ('电风扇','洗衣机','手电筒','电灯泡','电视机')

for i in tuple1:
    print(i)


#while遍历

i = 0
while i< len(tuple1):
    print(tuple1[i])
    i += 1

#多级元组的遍历(不要求二级元组长度一样)

tuple1 = (
        ('马艺楠','女','165','45kg'),
        ('李雪','女','160','40kg'),
        ('吴相俭','女','165.5','50kg')
    )

#遍历一级元组

for i in tuple1:
    #遍历二级元组
    for j in i:
        
        print(j)


#相同长度的多级列表
tuple1 = (
        ('马艺楠','女','165','45kg'),
        ('李雪','女','160','40kg'),
        ('吴相俭','女','165.5','50kg')
    )

for name,sex,height,weight in tuple1:
    print(name,sex,height,weight)


#直接获取二级元组的值
print(tuple1[1][3])

