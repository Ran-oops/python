#导入模块
import os

#exists() 检测一个文件或者文件夹是否促存在

path = 'D:\\py03\\new.exe'

path2 = 'D:\\py03\\old'

result = os.path.exists(path2)

print(result)


#isabs() 检测一个路径是否是一个绝对路经

path = 'py03\\new.exe'

path2 = 'D:\\py03\\old\\how'

result = os.path.isabs(path)

print(result)


#islink() 检测文件是否是一个链接(window没用)

path = 'C:\\Users\\xdl\\Desktop\\cmd.link'

result = os.path.islink(path)

print(result)

#samefile() 检测2个路径是否指向同一个文件

path1 = '..\\new.exe'

path2 = 'C:\\Users\\xdl\\Desktop\\python03\\12\\new.exe'

result = os.path.samefile(path1,path2)

print(result)
