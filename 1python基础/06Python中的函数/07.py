#break语句（跳出循环）
'''
i = 0
while i<100:
    #判断是否遇到了44
    if i == 44:
        #停止循环
        break
    
    print(i)
    i += 1

'''
#continue语句（数据过滤）

'''
i = 0
while i<100:
    #带4的不要->代码 num % 10 ==4   num // 10 ==4
    if i % 10 ==4 or i// 10 ==4:
        #进行变量 +1 操作
        i += 1
        #跳过本次循环，开始下一次的循环
        continue
    
    print(i)
    i += 1

'''


#在for..in循环中使用break和continue
'''
#continue

lists = ['江志学','李亚','白立鹏','张家明','周光丽','刘壮']

for one in lists:
    #找妹子   李亚    周光丽
    if one == '李亚' or  one == '周光丽':
        #跳过当前循环
        continue

    print(one)
'''

#break

sets = {'梨','香蕉','菠萝','苹果','炸弹','哈密瓜','西瓜','黄瓜'}


for i in sets:
    #检测用户第几次碰到炸弹
    if i == '炸弹':
        print('你按下了炸弹！')
        #终止循环
        break
    print(i)

