import shutil

'''
#copy()  复制文件

result = shutil.copy('d:\\a.txt','d:\\demo\\b.txt')
print(result)


#copy2() 复制文件，保留原有文件的元数据


result = shutil.copy2('d:\\a.txt','d:\\demo\\c.txt')
print(result)


#copyfileobj()复制文件的内容

result = shutil.copyfileobj(open('d:\\demo\\python资源.md','r'),open('d:\\demo\\result.txt','w'))
print(result)


#copyfile()  将一个文件的内容复制到另外一个文件当中

result = shutil.copyfile('D:\\demo\\python资源.md','d:\\demo\\d.txt')

print(result)
'''
'''

#copy能复制文件夹么？

result = shutil.copytree('d:\\demo','d:\\demo1')
print(result)


#copystat()复制文件状态

result = shutil.copystat('C:\\Users\\xdl\\Desktop\\第一期文档\\19-模块和包.md','D:\\demo\\a.txt')
print(result)


#rmtree() 移除整个目录

result = shutil.rmtree('D:\\demo')
print(result)

'''

#move() 移动文件或目录

#result = shutil.move('D:\\a.txt','D:\\Download\\aa.txt')
#result = shutil.move('D:\\ccc','D:\\Download\\ccc')

#print(result)

'''
#which() 检测命令对应的文件路径

result = shutil.which('cmd')

print(result)
'''


#disk_usage() 检测磁盘使用信息

result = shutil.disk_usage('D:')
print(result)
