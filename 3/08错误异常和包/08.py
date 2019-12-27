
#导入一个包中的模块1
'''
import animal.fish
import animal.dog

#使用包中的鱼的名字
print(animal.fish.name)
#使用包中的鱼的方法
animal.fish.swimming()

#使用包中的狗的成员
print(animal.dog.name)
animal.dog.say()
animal.dog.EatShit.eat()
'''

'''
#导入一个包中的模块2
import animal.dog as d

print(d.name)
d.say()
d.EatShit.eat()

'''

#导入一个包中的模块3

from animal.cat import *

print(name)
say()
getMouse.run()