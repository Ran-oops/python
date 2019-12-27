import os

#获取当前所有系统环境变量信息
'''
result = os.environ

print(result)


#获取指定名称的环境变量 path

result = os.environ['PATH']

print(result)

#借助字典操作 添加或者设置环境变量

os.environ['PATH'] += ';D:\\'

result = os.environ['PATH']

re=result.split(';')

print(re)

#尝试执行D:/下面的命令
'''
os.system('feiQ')


#os.environ自身没有特殊操作方法，都是借助字典的方法

result = os.environ.get('PATH')

print(result)
