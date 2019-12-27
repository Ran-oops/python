'''
#max()

lists = [3,35,7,1,576,45,6,1234,456,124]

result = max(lists)
print(result)


result = max(3,35,7,1,576,45,6,1234,456,124)
print(result)


#min()

lists = [3,35,7,1,576,45,6,1234,456,124]

result = min(lists)
print(result)


result = min(3,35,7,1,576,45,6,1234,456,124)
print(result)


#range() 产生连续数据的序列

#1个参数
result = range(100)
print(result)

#2个参数
result = range(5,25)
print(result)

#3个参数
result = range(5,50,5)
print(result)

for i in result:
    print(i)



print(hex(255))
print(oct(64))
print(bin(10))
'''
#repr()
str1 = '内置外置混合痔'
print(str1)

result = repr(str1)
print(result)

#eval() 将一个字符串当作python代码执行

result = eval(repr(str1))
print(result)

eval('print("abc")')
'''

#声明变量
a = 1
b = 2
c = 3
d = 4

#print(locals())


def demo():
    
    sisiter = 'girl'
    print(locals())

demo()
'''

