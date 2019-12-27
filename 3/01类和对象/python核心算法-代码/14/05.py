#多继承的问题1
class BaBa:
    def say(self):
        print('打死你个龟孙！')


class MaMa:
    def say(self):
        print('打死你个兔崽子！')



#儿子类 继承爸爸和妈妈类

class Son(BaBa,MaMa):
    pass


#实例化儿子对象 调用say方法
erzi = Son()

erzi.say()#继承多个类中存在同名方法，使用继承列表中第一个类的方法