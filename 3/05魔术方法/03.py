#水果类
class Fruit:
    pass


#南北类
class South:
    pass

class North:
    pass



#礼物非礼物
class Gift:
    pass

class NotGift:
    pass




#苹果类
class Apple(Fruit,North,Gift):
    pass

#橘子
class Orange(Fruit,South,Gift):
    pass

#香蕉
class Banana(Fruit,South,NotGift):
    pass

#梨
class Pear(Fruit,North,NotGift):
    pass


#mixin设计模式   多继承的应用！