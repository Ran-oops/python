import os

#splitext

filename = 'iandteacher.avi'

result = os.path.splitext(filename)

print(result)


#getsize()

path = 'C:\\Users\\xdl\\Desktop\\python资源.md'

result = os.path.getsize(path)

print(result)


#isfile()
path = 'C:\\Users\\xdl\\Desktop\\python资源.md'

result= os.path.isfile(path)
print(result)


#isdir()

result = os.path.isdir(path)
print(result)


#getctime,getatime,getmtime()
path = 'C:\\Users\\xdl\\Desktop\\python资源.md'

result = os.path.getctime(path)
print(result)

result = os.path.getmtime(path)
print(result)

result= os.path.getatime(path)
print(result)


#exists()

path = 'C:\\Users\\xdl\\Desktop\\python02\\12\\getdirsize.py'

result = os.path.exists(path)

print(result)


#isabs()

#path = 'C:\\Users\\xdl\\Desktop\\python02\\12\\getdirsize.py'
path = './ABC/DIE.JPG'

result = os.path.isabs(path)

print(result)


#islink检测一个路径是否是链接

path = 'C:\\Users\\xdl\\Desktop\\python书籍 - 快捷方式.lnk'

result = os.path.islink(path)

print(result)


#samefile()

path1 = './getdirsize.py'

path2 = 'C:\\Users\\xdl\\Desktop\\python02\\12\\getdirsize.py'

result = os.path.samefile(path1,path2)

print(result)




