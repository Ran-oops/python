#N行N列的星星

def mystar(maxhang = 10,maxlie = 10):

    #声明最大行数变量
    #maxhang = 5
    #声明最大列数变量
    #maxlie = 8
    
    hang = 0
    while hang<maxhang:
        #输出1行
        lie = 0
        while lie<maxlie:
            print('★',end = '')
            lie += 1

        #每行之后添加回车
        print('\n',end = '')
        #行变量+1
        hang += 1


#调用函数
'''
#在形参出设置形参的值即使调用时不存在实参也不会报错！
mystar()
mystar()
'''


mystar()
mystar()
mystar()
mystar()
mystar(5,5)

