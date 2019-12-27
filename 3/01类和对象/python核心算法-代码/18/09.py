#直接导入包
import girls

'''
#直接导入包 相当于导入 __init__.py文件的内容
print(girls.name)
girls.guang()
girls.chi()

girls.LiaoHan.say()

'''

'''
##直接导入包  别名模式
import girls as g

print(g.name)
g.chi()
g.LiaoHan.say()
'''


#from ..import 模式
from  girls import *

print(name)
print(sex)
guang()
chi()
LiaoHan.say()