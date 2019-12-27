#抽象类
import abc
#完成一个用户操作的类
class User(metaclass = abc.ABCMeta):#指定当前类的元类

    #可以具有成员属性
    company = '禽兽与美女公司'
    year = 2017


    #正常方法（丛浩）
    def listUser(self):
        print('列举所有用户信息')

    #非绑定类的方法（欢欢）
    @abc.abstractmethod
    def addUser(self):
        pass


    #绑定类的方法  /静态方法（冰冰）
    @abc.abstractstaticmethod
    def setUser():
        pass


    #类方法（文文）
    @abc.abstractclassmethod
    def delUser(cls):
        pass


#1.抽象类无法直接使用，也无法进行实例化操作
#2.抽象类只能呗其他类继承，然后将其中未完成的方法完成


#欢欢用户类
class HHuser(User):

    #完成非绑定类的方法（欢欢）
    def addUser(self):
        print('添加用户操作！')



#冰冰用户类
class BBuser(HHuser):
    # 完成绑定类的方法  /静态方法（冰冰）
    @staticmethod
    def setUser():
        print('设置用户操作！')


#文文用户类
class WWuser(BBuser):
    # 完成类方法（文文）
    @classmethod
    def delUser(cls):
        print('删除用户的操作！')


#文文类已经完成了所有抽象方法
u = WWuser()
u.addUser()

WWuser.setUser()

WWuser.delUser()