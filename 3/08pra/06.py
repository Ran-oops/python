'''
import myfile
print(myfile.color)
myfile.myfunc()
print(myfile.human.age)
print(myfile.human.sex)
myfile.human.cry()
'''
'''
#导入模块方法2
import myfile as m 
#使用模块中的变量
print(m.color)
m.myfunc()
print(m.human.age)
print(m.human.sex)
m.human.cry()
'''
'''
#导入模块方法3
#将模块中的某个内容  直接导入全局环境使用（有风险，绝对不能和系统的内建函数同名或其他自带变量和类同名）
from myfile import myfunc
myfunc()
'''
from myfile import *
print(color)
myfunc()
print(human.sex)
human.say()