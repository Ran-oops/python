'''
import girls
print(girls.name)
print(girls.sex)
girls.guang()
girls.chi()
girls.liaohan.say()
'''
'''
#直接导入包   别名模式
import girls as g
print(g.name)
print(g.sex)
g.guang()
g.chi()
g.liaohan.say()
'''
from girls import *
print(name)
print(sex)
guang()
chi()
liaohan.say()