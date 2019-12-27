#导入模块
import shutil
'''
#copy() 复制文件
result = shutil.copy('.\\new.exe','.\\test\\mynew.exe')
print(result)


#copy2() 复制文件，保留元数据
result = shutil.copy2('.\\new.exe','.\\test\\yournew.exe')
print(result)

#copyfileobj() 复制文件内容

result = shutil.copyfileobj(open('.\\01.txt','r'),open('.\\test\\33.py','w'))

print(result)


#copyfile() 复制文件内容

result = shutil.copyfile('.\\01.txt','.\\test\\34.txt')
print(result)
 

#copytree() 复制整个文件夹

result = shutil.copytree('D:\\Download','C:\\Users\\xdl\\Desktop\\DL')
print(result)



#rmtree 删除整个目录

result = shutil.rmtree('C:\\Users\\xdl\\Desktop\\DL')
print(result)


#move() 移动文件或者目录

result = shutil.move('.\\new.exe','.\\test\\12new.exe')

print(result)


#which() 检测一个命令所在的目录
result = shutil.which('ping')

print(result)

#disk_usage()#获取磁盘使用信息
result = shutil.disk_usage('D:')

print(result)

'''
