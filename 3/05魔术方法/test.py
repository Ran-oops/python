#人类
class Human:
    #制作人类的时候得到一个猴子对象
    def __new__(cls):
        return object.__new__(Monkey)

#猴子类
class Monkey:
    pass


#实例化人类 得到猴子对象
one = Human()
print(one)