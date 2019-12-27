#非关键字参数，关键字参数，非关键字收集参数，关键字收集参数共存

'''
num 非关键字参数
name 关键字参数
*fargs 非关键字收集参数
**args 关键字收集参数

'''

def argsall(num,name,*a,**args):
    # print(num)
    # print(name)
    print(a)
    # print(args)
    pass


#调用函数传参
argsall(100,200,300,400,500,sex='男',age=18)
