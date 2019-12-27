"""
#声明一个lambda表达式

mylamb = lambda x,y:x+y

'''
相当于一下函数
def func(x,y):
    return x + y


'''
#调用函数
result = mylamb(4,5)
print(result)
"""


''''''
#再来一个 分支版本

mylamb= lambda sex : '有胡子' if sex == 'man' else '没胡子'

result = mylamb('woman')

print(result)


''''
#调用函数版本

mylamb = lambda x:type(x)

result = mylamb('拾元')

print(result)
'''
