
#声明一个函数
def func(num):
    #声明一个变量(局部变量,当前当次调用函数有效)
    a = 250

    print(a)

    #改变变量a
    a += num

    print(a)


#调用函数func
func(10)  # a是第一次  


#再次调用函数
func(20) #  a是第二次
    


    
