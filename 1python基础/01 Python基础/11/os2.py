import os

#os.path 代表一个子模块
print(os.path)

#os.curdir 表示当前目录 （相对路径）
print(os.curdir)

#os.pardir 表示上一层文件夹的路径（相对路径）
print(os.pardir)

#创建文件
#fp = open('./my.txt','w')# .可以省略 相对路径
fp = open('C:\\Users\\xdl\\Desktop\\python02\\11\\absmy.txt','w')
fp.close()

#创建文件
#fp = open('../die.txt','w')# '..不可以省略 相对路径
fp = open('C:\\Users\\xdl\\Desktop\\python02\\absdie.txt','w')
fp.close()


#os.name
print(os.name)


#os.sep 获取当前系统的路径分隔符号

print(os.sep)


#os.extsep 获取当前系统中文件名和后缀名之间的分隔符

print(os.extsep)

#os.linesep 获取系统换行符号

print(os.linesep)


