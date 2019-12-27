
'''
def demo():
    #局部变量
    x = 5
    y = 9

    #内部函数
    def inner1():
        pass

    def inner2():
        pass


    #闭包返回的函数
    def all():
        return [y,inner1,inner2]

    #返回闭包需要的函数
    return all


#调用函数与
bb = demo()

print(bb.__closure__)
'''



def test():
    x = 5

    def inner(b):
        
        return x + b

    return inner


#调用函数
bb = test()

result = bb(10)
print(result)
