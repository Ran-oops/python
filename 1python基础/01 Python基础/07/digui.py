
#递归函数



def tubie(num):

    #1.输出num
    print(num)

    #2.判断条件，不改变num
    if num >0:
        tubie(num-1)
    else:
        print('================')


    #3.输出num
    print(num)


#调用递归函数
tubie(3)

'''
#tubie(3)

def tubie(3):

    #1.输出num
    print(3)

    #2.判断条件，不改变num
    if 3 >0:
        tubie(3-1) #调用tubie（2）
    


    #3.输出num   #等待tubie(2)执行完毕
    print(3)


调用tubie（2）
def tubie(2):

    #1.输出num
    print(2)

    #2.判断条件，不改变num
    if 2 >0:
        tubie(2-1) #调用tubie(1)


    #3.输出num #等待tubie(1)执行完毕
    print(2)

#调用tubie(1)
def tubie(1):

    #1.输出num
    print(1)

    #2.判断条件，不改变num
    if 1 >0:
        tubie(1-1) #调用tubie(0)
  

    #3.输出num  #等待土鳖(0)执行完毕
    print(1)


#调用tubie(0)
def tubie(0):

    #1.输出num
    print(num)

    #2.判断条件，不改变num
    if 0 >0:
       
    else:
        print('================')


    #3.输出num
    print(0)


3
2
1
0
===========
0
1
2
3

'''

