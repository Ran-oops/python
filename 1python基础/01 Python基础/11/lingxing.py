#循环生成菱形的上半部分

'''
i = 10
j = 0

while i > 0:
    
    #输出每一行的空白部分
    print(' '*i,end='')
    #输出每一行的实体部分
    print('@'*j,end='\n')

    #变量的增减
    i -= 1
    j += 2
    
'''


#控制空格字符输出的数量，循环次数的计数变量
i = 10
#控制@符号的输出数量，根据循环次数进行增加
j = 0
#添加循环 设定循环次数
while i>0:
    #输出每一行前半部分的空白字符数量,输出不能换行，因为后面还有一半
    print(' '*i,end = '')
    #输出每一行后半部分的@符号的数量
    print('@'*j)

    #循环变量自减操作
    i -= 1
    #蹭循环的次数改变自己的值
    j += 2
