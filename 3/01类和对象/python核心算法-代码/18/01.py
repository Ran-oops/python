#断言异常(断言的语句结果为false 就报错)
#assert 5 < 3

#属性错误(访问不存在的成员)
'''
class Human:
    pass

Human.sex
'''

#导入错误（导入了不存在的模块名）
#import abcd

#列表的索引错误(不存在的索引)
#lists = [1,2,3]
#print(lists[100])

#键错误(不存在的键)
#dicts = {'a':1,'b':2}
#print(dicts['c'])

#KeyboardInterrupt  （用户终止程序）
'''
for i in range(0,10000000):
    print(i)
'''

#nameError变量名错误(访问了不存在的变量)
#print(ch)


#FileNotFoundError 找不到文件的错误
#open('a.txt','r')

#语法错误
'''
def ad()：
    pass
'''

#缩进错误
#if True:
#pass

#缩进错误(混用缩进和空格)   弄不出来 自己用sublime自己做
'''
if True:
    pass
'''

#类型错误（不同类型进行运算）
'''
a = 1
b = 'a'

a += b
'''

#除数不能为0
4/0