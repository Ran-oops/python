#声明一个递归函数


def num(i):
    #1.输出变量i
    print(i)

    #2.判断变量i是否>0
    if i > 0:
        num(i - 1)
    else:
        print('---------')

    #3.输出变量i
    print(i)


#调用函数
num(3)



'''

def num(3):
    #1.输出变量i
    print(3)

    #2.判断变量i是否>0
    if 3 > 0:
        num(3 - 1)#num(2)
    

    #3.输出变量i
    print(3) #等待 num(3-1)执行完毕


num(2)

def num(2):
    #1.输出变量i
    print(2)

    #2.判断变量i是否>0
    if 2 > 0:
        num(2 - 1)#num(1)
   

    #3.输出变量i
    print(2)#等待num(2-1)执行完毕


num(1)

def num(1):
    #1.输出变量i
    print(1)

    #2.判断变量i是否>0
    if 1 > 0:
        num(1 - 1)#num(0)
    
    #3.输出变量i
    print(1)#等待num(1-1)执行完毕


num(0)

def num(0):
    #1.输出变量i
    print(0)

    #2.判断变量i是否>0
    if 0 > 0:
       # num(i - 1)
    else:
        print('---------')

    #3.输出变量i
    print(0)
'''

'''
3
2
1
0
-------------
0
1
2
3


'''
