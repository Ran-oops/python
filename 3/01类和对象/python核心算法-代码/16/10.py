#类的常用函数
#issubclass()检测一个类是否是另外一个类的子类

class Father:
    pass

class Son(Father):
    pass

result = issubclass(Son,Father)
print(result)


#isinstance() 检测一个对象是当否是指定类的实例
fa = Father()

#result = isinstance(fa,Father)
result = isinstance(fa,(Father,Son))
print(result)

#hasattr()检测是否具有指定的成员
class Human:
    sex = 'man'
    age = 18
    def say(self):
        print('11111111111')

ll = Human()
result = hasattr(ll,'color')
print(result)


#getattr() 获取某个成员的值
#result = getattr(ll,'age')#相当 对象.age
result = getattr(ll,'color','black')
print(result)

#setattr() 设置成员的值
setattr(ll,'age',38) #相当于 对象.age = 38
print(ll.age)

#delattr() 删除对象成员
print(ll.__dict__)
delattr(ll,'age')#相当于 del.age
print(ll.__dict__)


