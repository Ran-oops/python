#人类

class Human:
    #成员属性
    name = '狗单'
    sex = 'nan'
    age = 18

    #成员方法

    #魔术方法  实例化对象过程中触发

    def __new__(cls,color,height):
        print(cls)
        print(color)
        print(height)
        print('new方法被触发')
        #程序制作对象都是object类中的__new__提供的对象制作功能，我们自己的类都是默认继承object中的new方法来制作对象的
        return object.__new__(cls)

    #测试参数  new魔术方法和init魔术方法的参数必须一只
    def __init__(self,color,height):
        pass


    def say(self):
        print('美女，坐在我的bian上把')

    def cry(self):
        print('姑娘讨厌我～555～～～')


#实例化对象
yzf = Human('yellow','185cm')
print(yzf)

