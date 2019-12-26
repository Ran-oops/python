#for in 遍历

list1 = ['吴相俭','马艺楠','李雪','王媛春','阴亚会']

for i in list1:
    print(i)


#while循环遍历

i = 0
while i<len(list1):
    print(list1[i])
    i += 1

#二级列表的遍历

lists = [
            ['唐伟','3.5'],
            ['糖葫芦','4'],
            ['糖豆','0.5'],
            ['唐嫣','1000'],
            ['糖醋鲤鱼','65']
        ]


for one,two in lists:
    print(one)
    print(two)

#非同等长度的二级列表的遍历

lists = [
        ['赵杰','女','175cm','55kg'],
        ['张然然','女','180cm'],
        ['陈磊','男','硬'],
        ['韩琳琪','男','软']
    ]

#外层循环遍历第一级
for out in lists:
    #内层循环遍历第二季
    for inner in out:
        print(inner)

