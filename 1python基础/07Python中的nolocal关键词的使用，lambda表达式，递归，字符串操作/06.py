'''
#性别判断的函数
def sex(num):
    #判断传入的数字是0还是1 1为男  0为女
    if num == 0:
        return '姑娘'
    else:
        return '爷们'


#调用函数
result = sex(0)

print(result)
'''

#lambda表达式
sex = lambda num: '爷们' if num == 1 else '姑娘'

#调用函数

result = sex(1)

print(result)
