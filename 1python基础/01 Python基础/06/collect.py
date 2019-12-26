#制作一个可以计算任意个数字的和的函数
'''
def mysum(*args):
    #声明一个用于计算和的变量
    total = 0
    
    num = 0
    while num<len(args):
        #将形参接受的参数元组中的每个值加入total
        total = total + args[num]
        num += 1

    #循环结束后 输出和
    print(total)


mysum(3,5,1,23,5,6,2,7,3,3,6,5,2,34,132,234,679,780)
'''


#检测收集参数收集的规则
def myargs(no1,no2,*args):
    #检测no1接受的实参
    print(no1)
    #检测no2接受的实参
    print(no2)
    #检测args接受的实参
    print(args)
    pass
    


#调用函数
myargs(1,2,3,4,5,6,7,8,9,my = 100)
