#os模块

#导入os模块
import os

'''
#getcwd() 获取当前默认的工作目录/文件夹

result = os.getcwd()

print(result)

#chdir() 修改当前工作目录

os.chdir('D:\\py03')

result = os.getcwd()

print(result)
#新建文件
f = open('new.exe','w')
f.close()


#listdir() 获取指定目录中所有文件和文件夹名称组成的列表

alllist = os.listdir('C:\\Users\\xdl\\Desktop\\python03\\11')

print(alllist)




#mkdir() 创建文件夹

#result = os.mkdir('nidaye')
result = os.mkdir('D:\\py03\\nidaniang')
print(result)



#makedirs() 递归式创建文件夹
result = os.makedirs('ren\\man\\woman\\child')
print(result)


#rmdir()删除文件夹（只能删除空目录）
#result = os.rmdir('nidaye')
result = os.rmdir('D:\\py03\\nidaniang')
print(result)


#removedirs() 递归式删除文件夹（只能删除空目录）

os.removedirs('ren\\man\\woman')


#rename() 修改文件或者文件夹名称
#文件夹修改
#result = os.rename('ren','human')
#文件修改
result = os.rename('3.txt','233.txt')
print(result)



#stat() 获取文件信息

result = os.stat('01.py')

print(result)

'''





