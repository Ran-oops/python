#水果类

class Fruit:
    pass


#按照地域划分

#南方水果
class SouthFruit(Fruit):
    pass


#北方水果
class NorthFruit(Fruit):
    pass


#按是否可以送礼

#礼物水果
#南方礼物水果
class SouthGiftFruit(SouthFruit):
    pass
#北方礼物水果
class NortGiftFruit(NorthFruit):
    pass

#非礼物水果
#南方非礼物水果
class SouthNotGiftFruit(SouthFruit):
    pass
#北方非礼物水果
class NorthNotGiftFruit(NorthFruit):
    pass




#苹果类
class Apple(NorthGiftFruit):
    pass

#橘子
class Orange(SouthGiftFruit):
    pass


#香蕉类
class Banana(SouthNotGiftFruit):
    pass

#梨
class Pear(NorthNotGiftFruit):
    pass


