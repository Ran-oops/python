#10行10列的星星

def mystar(maxhang,maxlie):

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
mystar(3,4)# 将第一个参数3 赋值给maxhang  第二个参数4 赋值给maxlie

mystar(6,6)# 将第一个参数6 赋值给maxhang  第二个参数6 赋值给maxlie

mystar(5,3)# 将第一个参数5 赋值给maxhang  第二个参数3 赋值给maxlie

h = 8
l = 9

mystar(h,l)




