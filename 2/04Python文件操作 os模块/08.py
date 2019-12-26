#os.environ

#导入os模块
import os

#查看所有环境变量
#print(os.environ)


#查看path环境变量
#print(os.environ['PATH'])

#print(os.environ['PATH'].split(';'))

#添加系统环境变量
#

os.environ['PATH']= os.environ['PATH']+';'+'D:\\'
print(os.environ['PATH'])


#实验操作
os.system('feiq')
