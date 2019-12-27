import sys
print(sys.path)

#导入模块方法1
'''
#导入模块（模块名就是文件名）
import myfile

#使用模块中的变量
#print(myfile.color)

#使用模块中的函数
#myfile.myfunc()

#使用模块中的类
#print(myfile.Human.age)
#print(myfile.Human.sex)
#myfile.Human.cry()
'''

'''
#导入模块方法2

import myfile as m

#使用模块中的变量
print(m.color)

#使用模块中的函数
m.myfunc()

#使用模块中的类
print(m.Human.sex)
print(m.Human.age)
m.Human.cry()
'''

'''
#导入模块方法3：
#将模块中的某个内容 直接导入全局环境使用（有风险，绝对不能够和系统内建函数同名或者其他自带变量和类同名）

from myfile import myfunc

myfunc()
'''

'''
#导入模块方法4：
#将模块中的多个内容

from myfile import color,myfunc

print(color)
myfunc()
'''

#导入模块方法5：
#一次导入模块中的所有信息

from myfile import *

print(color)
myfunc()
print(Human.sex)
Human.say()
