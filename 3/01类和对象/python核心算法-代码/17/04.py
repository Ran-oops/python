#多态
import abc
#定义规则 （抽象类）

class Animal(metaclass=abc.ABCMeta):

    #定义叫方法
    @abc.abstractmethod
    def jiao(self):
        pass

    #定义尿方法
    @abc.abstractmethod
    def niao(self):
        pass


#声明小狗类
class Dog(Animal):
    # 定义叫方法
    def jiao(self):
        print('汪汪～～')

    # 定义尿方法
    def niao(self):
        print('抬起后腿尿～～')



#声明小猫类
class Cat(Animal):
    # 定义叫方法
    def jiao(self):
        print('喵喵～')

    # 定义尿方法
    def niao(self):
        print('蹲着尿～')



#声明小伟类
class XiaoWei(Animal):
    # 定义叫方法
    def jiao(self):
        print('呀咩跌')

    # 定义尿方法
    def niao(self):
        print('站成一个“卜”字尿')




#行为类
class Action:

    #用于接收对象的成员属性
    obj = None


    @classmethod
    def say(cls):
        cls.obj.jiao()

    @classmethod
    def pee(cls):
        cls.obj.niao()


#实例化小狗对象
dog = Dog()
#实例化小猫对象
cat = Cat()
#实例化小伟对象
xw = XiaoWei()

#将对象传入类中
#Action.obj = dog
#Action.obj = cat
Action.obj = xw

#调用行为类中的叫方法
Action.say()
Action.pee()
