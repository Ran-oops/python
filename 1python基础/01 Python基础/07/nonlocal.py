

#声明一个外部函数
def outer():

    #声明一个变量(肯定不是全局变量)
    x = 5
    
    #声明一个内部函数
    def inner():
        nonlocal x#声明x不是局部变量
        x += 9
        print(x)

    #调用函数
    inner()



#调用outer
outer()

        
    
