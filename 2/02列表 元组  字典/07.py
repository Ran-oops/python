#元组的遍历

tuple1 = ('陆展博','林婉瑜','胡一菲','曾小贤','吕子乔','陈美嘉','关谷神奇')


#while循环遍历
#获取长度
cd = len(tuple1)

i = 0

while i<cd:
    print(tuple1[i])
    i += 1


#for ..in循环遍历

for one in tuple1:
    print(one)


#多级元组的遍历


#长度相等的二级元组
tuple1 = (

    ('李丛丛','178cm','187斤'),
    ('吕欣','187cm','280kg'),
    ('王娇娇','165mm','500g'),
    ('兰婉婷','160cm','80斤')
)

for name,height,weight in tuple1:
    print(name,height,weight)


#长度不等的二级元组

tuple1 = (
    ('杨惠钧','女','男人','158cm','98kg'),
    ('李亚','女','乐器'),
    ('周光丽','女',18,'yellow'),
    ('游可欣','女','男朋友','50kg')
)

for one in tuple1:
    #遍历二级元组
    for info in one:
        print(info)


#访问二级元组或者列表中的信息
print(tuple1[2][3])
