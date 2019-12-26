#导入模块
import os

#curdir属性  .表示当前文件夹current directory
print(os.curdir)


#pardir属性 表示上一层文件夹 parent directory
print(os.pardir)


#新建文件操作
#在当前文件夹下创建
#open('./cur.txt','w')

#在当前文件夹下的human文件夹中创建
#open('.\\human\\1.txt','w')

#在当前文件夹的上层文件夹创建
#open('../par.txt','w')

#在当前文件夹的上层文件夹的上层文件夹中创建
#open('../../par.txt','w')


#C:/window/abc/123.txt  < = > C:\\window\\abc\\123.txt  完全等价


#path os中的一个子模块 包含很多和路径相关的功能

#print(os.path)


#name 获取当前系统的名称（内核名称）
print(os.name)


#sep 获取系统路径的分隔符号

print(os.sep)

#extsep 获取文件名称和后缀之间的分隔符
print(os.extsep)

#linesep获取当前系统的换行符号
print(repr(os.linesep))
