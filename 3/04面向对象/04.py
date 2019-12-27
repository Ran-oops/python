#多继承

#爷爷类
class YeYe:
    def damajiang(self):
        print('四川麻将写真馆～')

#奶奶类
class NaiNai:
    def dapuke(self):
        print('炸金花～')

#姥爷类
class LaoYe:
    def doudizhu(self):
        print('四个二带大小王')

#姥姥类
class LaoLao:
    def dezhoupuke(self):
        print('性感荷官在线发牌～')


#爸爸类
class BaBa(YeYe):
    def tuipaijiu(self):
        print('虎头～')

#妈妈类
class MaMa(LaoLao):
    def yaoshaizi(self):
        print('6666~')

#老吴类
class LaoWu:
    def yaoweixin(self):
        print('美女，约不～')

#儿子类
class Son(LaoWu,BaBa,NaiNai,LaoYe,MaMa):
    def duma(self):
        print('11号快点跑！')


#实例化儿子类对象（赌神）

erzi = Son()

erzi.damajiang()
erzi.dapuke()
erzi.dezhoupuke()
erzi.doudizhu()
erzi.duma()
erzi.tuipaijiu()
erzi.yaoshaizi()
erzi.yaoweixin()