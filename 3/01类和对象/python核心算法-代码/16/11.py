class Animal:
    pass

class Atom:
    pass

class Human(Animal,Atom):
    '''
    这是一个类的文档
    '''
    #属性
    sex = 'man'
    age = 18
    name = '刚单'


    def eat(self):
        print('金粒餐，yoxi～')
        print(Human.__name__)


#__dict__ 获取类或者对象的所属成员
print(Human.__dict__)
hh = Human()
print(hh.__dict__)

#__doc__ 获取类文档
print(Human.__doc__)


#__bases__ 获取类的继承列表
print(Human.__bases__)

#__name__ 在类中表示类名称的字符串
hh.eat()

#获取当前文件的标志  ，当前文件就是直接运行的文件，值固定为__main__
print(__name__)