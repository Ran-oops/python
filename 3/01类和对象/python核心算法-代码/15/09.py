'''
class 制作蛋糕类：

    def 和面（）：
        pass

    def 发酵():
        pass

    def 烘烤():
        pass

    def 切形状():
        pass

    def 摸奶油():
        pass

    def 放水果():
        pass

    def 包装():
        pass

    def 组合蛋糕():
        制作蛋糕对象.和面()
        制作蛋糕对象.发酵()
        制作蛋糕对象.烘烤()
        制作蛋糕对象.切形状()
        制作蛋糕对象.摸奶油()
        制作蛋糕对象.放水果()
        制作蛋糕对象.包装()


#制作蛋糕

制作蛋糕对象 =制作蛋糕（）

制作蛋糕对象.组合蛋糕()#->制作蛋糕对象()

最后得到一个做好的蛋糕



'''

class DoCake:

    def hm(self):
        print('和面')

    def fj(self):
        print('发酵')

    def hk(self):
        print('烘烤')

    def qxz(self):
        print('切形状')

    def mny(self):
        print('抹奶油')

    def fsg(self):
        print('放水果')

    def bz(self):
        print('包装')
        return '做好的蛋糕'

    def __call__(self):
        self.hm()
        self.fj()
        self.hk()
        self.qxz()
        self.mny()
        self.fsg()
        result = dk.bz()
        return result


#实例化对象
dk = DoCake()


#简洁的方法
result = dk()
print(result)
