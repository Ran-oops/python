#导入模块
import shutil

'''
#归档操作
result = shutil.make_archive('C:\\Users\\xdl\\Desktop\\py01','tar','C:\\Users\\xdl\\Desktop\\python01')

print(result)
'''


'''
#解包操作

result = shutil.unpack_archive('C:\\Users\\xdl\\Desktop\\py01.zip','C:\\Users\\xdl\\Desktop\\py01')
print(result)
'''

#获取允许的归档格式get_archive_formats()

result = shutil.get_archive_formats()

print(result)


#获取允许的解包格式get_unpack_formats()

result = shutil.get_unpack_formats()

print(result)
