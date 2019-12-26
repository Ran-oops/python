#os.path模块
import os

'''
#os.curdir

xdpath = os.curdir

print(xdpath)

#abspath 转化为绝对路径

jdpath = os.path.abspath(xdpath)

print(jdpath)


#basename() 获取路径中文件名和后缀部分（文件夹路径则获取最后一层文件夹）
#dirname()获取路径中路径

path = 'D:\\nidaye\\nidama'

result = os.path.basename(path)
print(result)

result = os.path.dirname(path)
print(result)

#join() 将两个路径合并成一个

path1 = 'D:\\AAA\\BBB\\'
path2 = 'CCC\\abc.exe'

result = os.path.join(path1,path2)

print(result)


#split() 将路径拆解成dirname+basename的元组
path = 'D:\\nidaye\\nidama\\nibiaomei.txt'

result = os.path.split(path)

print(result)

#splitext()  将路径拆解成文件后缀和其他部分（常用来获取文件后缀）

path = 'D:\\nidaye\\nidama\\nibiaomei.txt'

result = os.path.splitext(path)
print(result)


#getsize() 获取文件的大小（没有获取文件夹大小的函数）

result = os.path.getsize('D:\\FeiQ.exe')
print(result)


#isfile()检测是否是文件

result = os.path.isfile('D:\\file1')
print(result)


#isdir() 检测是否是目录
result = os.path.isdir('D:\\file2.txt')
print(result)

'''

#getctime()  get create time 文件创建时间

result = os.path.getctime('C:\\Users\\xdl\\Desktop\\python03\\11\\01.py')
print(result)


#getmtime()  get modify time  文件修改时间

result = os.path.getmtime('C:\\Users\\xdl\\Desktop\\python03\\11\\01.py')
print(result)

#getatime()  get active time 文件访问时间

result = os.path.getatime('C:\\Users\\xdl\\Desktop\\python03\\11\\01.py')
print(result)


