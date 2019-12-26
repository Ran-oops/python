
#全局环境中声明变量
x = 99

y = 88

z = 77


#locals()  打印当前环境当中的变量

result = locals()

print(result)


#检测是否声明了x变量

result = 'x' in locals()

print(result)

if result:
    print('x 已经声明，值为',x)



#局部环境

def py03():
    #局部变量
    a = 1
    b = 2
    c = 3

    #获取当前环境变量
    result = locals()
    print(result)


#调用函数
py03()
