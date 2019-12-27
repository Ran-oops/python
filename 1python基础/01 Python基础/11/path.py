#os.path 模块

import os

#abspath()

#获取当前路径并且转化为绝对路径
path = os.curdir

abspath = os.path.abspath(path)

print(abspath)

#获取上一层路径并且转化为绝对路径

path = os.pardir

abspath = os.path.abspath(path)

print(abspath)


# basename() & dirname()

path = 'C:\\Users\\xdl\\Desktop\\python02\\hhxx.md'

result1 = os.path.basename(path)
print(result1)

result2 = os.path.dirname(path)
print(result2)

#join（）
#basename放在后面，dirname放在前面
result = os.path.join(result2,result1)

print('结果为=',result)


#split()
path =r'C:\Users\xdl\Desktop\python02\hhxx.md'

result = os.path.split(path)

print(result)


