'''
#输出1行星星

print('★★★★★★★★★')
#输出10行星星
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
print('★★★★★★★★★')
'''


'''
循环格式 while循环


起始的计数变量i

while 条件表达式:
    书写需要循环的python代码
    改变计数变量的值


'''



#声明起始计数变量
num = 0

while num < 10:
    #需要进行循环的代码
    print('★★★★★★★★★',num)
    #改变循环的计数变量
    num += 1


'''
1.声明计数变量num = 0

2.进入while循环判断，判断0<10 是否为真
3.结果为真，执行while代码组中的内容(输出一行星星)
4.将计数变量进行了+1操作 num = 1


5.再次进入while循环判断，判断1<10 是否为真
6.结果为真，执行while代码组中的内容(输出一行星星)
7.将计数变量进行了+1操作  num=2


5.再次进入while循环判断，判断2<10 是否为真
6.结果为真，执行while代码组中的内容(输出一行星星)
7.将计数变量进行了+1操作  num=3

...



5.再次进入while循环判断，判断9<10 是否为真
6.结果为真，执行while代码组中的内容(输出一行星星)
7.将计数变量进行了+1操作  num=10

N.在此进入while循环判断，判断10<10是否为真
N+1.结果为假，循环结束，不再执行循环结构，继续往下执行其他结果



'''


#计算1-1000的和

#声明一个计数的变量(循环)
num = 1

#声明求和的变量
total = 0

#循环结构
while num <= 1000:
    #循环内容
    total += num #total = total + num
    #改变计数变量
    num += 1

#顺序结构部分
print(total)




