import shutil


#make_archive归档操作

#result = shutil.make_archive('D:\\py2','tar','C:\\Users\\xdl\\Desktop\\python01')
#print(result)


#unpack_archive解包操作
#result = shutil.unpack_archive('D:\\py2.zip','D:\\py2')
#print(result)


#get_archive_formats()  获取当前系统已经注册的归档文件格式

result = shutil.get_archive_formats()
print(result)


#get_unpack_formats() 获取当前系统已经注册的解包格式

result = shutil.get_unpack_formats()
print(result)
