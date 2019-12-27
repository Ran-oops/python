#单例设计模式

#一个类只能实例化一个对象

class YuZhenFeng:
    #类中添加一个属性  记录是否创建对象
    obj = None

    #魔术方法  new 控制对象的创建
    def __new__(cls):
        #检测对象是否创建
        if cls.obj == None:
            #实例化对象并且存入类中
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            #不是第一次创建对象  直接返回类中存储的那个第一次创建的对象
            return cls.obj



#实例化对象
one = YuZhenFeng()
print(one)

two = YuZhenFeng()
print(two)

three = YuZhenFeng()
print(three)

four = YuZhenFeng()
print(four)

five = YuZhenFeng()
print(five)

six = YuZhenFeng()
print(six)