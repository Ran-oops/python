
#声明函数

def outer():

    #变量（对于outer而言是局部变量）
    num = 99

    #声明一个内部函数
    def inner():

        #nonlocal关键字（1.声明当前变量不是当前函数的局部变量，2，也不是全局变量）
        nonlocal num

        #修改操作
        num += 1

        print(num)


    #调用inner
    inner()


#调用外部函数
outer()
