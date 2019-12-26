#Numner类型
'''
#整型  integer  int 就是整数


#十进制声明整型  0～9

num = 123

print(type(num))

print(num)


#二进制声明整型  0～1

numb = 0b1001

print(type(numb))

print(numb)


#八进制整型声明  0～7

numo = 0o177

print(type(numo))

print(numo)


#十六进制整型声明 0～9A-F  A~F表示10-15

numx = 0x11AF

print(type(numx))

print(numx)
'''


'''
#浮点型 float  就是小数类型


#小数表示法

num1 = 3.141592653

print(type(num1))

print(num1)


#num2 = 1/3  除法运算 并不是表示小数的方式

#科学计数法

num2 = 314e-2  #314 * 10的负二次方

print(type(num2))

print(num2)
'''

'''
#布尔类型  只有2个值 True和False

#var = True
var = False

print(type(var))

print(var)

#用于判断
if False:
    print('巧玲老师有对象')


num1 = 9
result = num1 + True #True是用1来表示    False是用0来表示的
print(result)


#通过判断获取布尔值

result = 3 < 5
print(result)
'''


#复数 Complex 指虚数和实数的集合

#使用复数表达式声明复数

num = 123 + 2j

print(type(num))

print(num)


#使用声明复数的专用功能

num2 = complex(250,20)

print(type(num2))

print(num2)



