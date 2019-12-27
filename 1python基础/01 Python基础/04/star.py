'''
#1行10列星星
print('★★★★★★★★★★')

#输出10行10列的星星
num = 0

while num<10:
    print('★★★★★★★★★★')
    num += 1

'''

'''
#只有1个星星  生成1行10列★

num = 0
while num<10:
    print('★',end = '')
    num += 1
'''

'''
#10行10列
#循环1行内容生成10行
hang = 0

while hang<10:
    #输出一行
    #----1行10列--------
    lie = 0 #重点

    while lie<10:
        print('★',end='')
        lie += 1
    #-------------------
    #断开当前行 加个回车\n
    print('\n',end = '')
    #行变量增加
    hang += 1
'''



'''
#10行10列  13579 实心星星  246810 空心星星(取余运算  分支   循环)
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆ 
'''


'''
#10行10列 隔行变色

hang = 0

while hang<10:

    #输出1行
    #生成1行10列
    lie = 0
    while lie<10:

        #在此处检测当前行数
        if hang %2 == 0:
            print('★',end='')
        else:
            print('☆',end='')
            
        
        lie += 1


    #回车
    print('\n',end='')

    #hang变量增加
    hang += 1
    
'''


'''

#10行10列 隔列变色

hang = 0

while hang<10:
    #s输出1行内容
    lie = 0
    while lie<10:
        #判断当前列数
        if lie %2 ==0:
            print('★',end = '')
        else:
            print('☆',end = '')
            
        lie += 1

    #回车换行
    print('\n',end='')
    #行变量+1
    hang +=1

'''

'''
#单个循环实现10行10列

num = 0
while num<100:
    print('★',end ='')
    #找到指定的位置添加\n字符
    if num % 10 == 9:
        print('\n',end ='')
    
    num += 1
'''

'''
#单个循环10行10 +隔行变色

num = 0

while num<100:
    #判断当前输出时的行数
    hang = num // 10  #0123456789

    if hang % 2 == 0:
        print('★',end='')
    else:
        print('☆',end='')
    
    
    #检测是否是换行位置
    if num % 10 == 9:
        print('\n',end = '')
    num += 1

'''


'''
#单个循环隔列变色

num = 0

while num < 100:

    #判断是奇数列还是偶数列
    if num % 2 == 0:
        print('★',end = '')
    else:
        print('☆',end = '')
        
    #检测换行位置
    if num % 10 == 9:
        print('\n',end = '')
    num += 1

'''




