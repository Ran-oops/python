#python2.7

#所有的类必须默认继承object类，该类是所有类的父类

# class Human(object):
#     pass
#
# print(Human)
# rl = Human()
# print(rl)



#python3

class Human:
    pass

print(Human)
rl = Human()
# print(rl)

#isinstance（对象,类） 检测一个对象是否是指定类的对象

#rl（对象） ->Human类的实例 ->Human类默认继承object

result = isinstance(rl,object)
print(result)

#issubclass() 检测一个类是否是另一个类的子类  (任何类都是object类的子类)

result = issubclass(Human,object)
print(result)